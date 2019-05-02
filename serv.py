import os, sys
import constants as const
from data_handling import send_data, receive_data, size_padding
from socket_functions import bind


def receive_file(sock):
    # create new socket for data transfer
    servSocket = bind()

    # send port number to client
    servPort = servSocket.getsockname()[1]
    send_data(sock, str(servPort))

    # accept client connection
    print("Listening on port " + str(servPort))
    dataSocket, addr = servSocket.accept()
    print("Connected to: " + addr[0])

    # get payload sizes
    fileNameSize = receive_data(dataSocket, const.HEADER_SIZE)
    fileDataSize = receive_data(dataSocket, const.HEADER_SIZE)

    # error checking
    if fileNameSize == "":
        print("Failed to receive file name size")
        return

    if fileDataSize == "":
        print("Failed to receive file data size")
        return

    # read payload
    fileName = receive_data(dataSocket, int(fileNameSize))
    fileData = receive_data(dataSocket, int(fileDataSize))

    # write file
    filePath = const.SERVER_FOLDER + fileName
    userFile = open(filePath, "w")
    userFile.write(fileData)

    print(fileName + " received")
    print("File size: " + fileDataSize)

    # close file and connection
    userFile.close()
    dataSocket.close()
    print("Data transfer connection closed")
    

def run(args):
    # To run: python3 serv.py <PORT>
    if len(args) != 2:
        print("Usage: python3 " + args[0] + " <PORT>")
        sys.exit()

    port = args[1]

    # bind socket to a port
    servSocket = bind(int(port))
    if not servSocket:
        print("Failed bind to a port")
        sys.exit()

    while True:
        # keep listening for connections until user ends process
        print("Listening on port " + port)
        cliSocket, addr = servSocket.accept()
        print("Connected to: " + addr[0])

        while True:
            query = receive_data(cliSocket, const.HEADER_SIZE)
            # print(query)

            # get <FILE NAME>
            # sends <FILE NAME> to client
            if query == const.COMMANDS[0]:
                print("get not implemented yet")

            # put <FILE NAME>
            # downloads <FILE NAME> from client
            elif query == const.COMMANDS[1]:
                receive_file(cliSocket)

            # ls
            # lists files on the server
            elif query == const.COMMANDS[2]:
                # get file names from folder
                files = os.listdir(const.SERVER_FOLDER)
                response = ""
                for file in files:
                    response += file + "  "
                response = response[:-2]

                # send response
                responseSize = size_padding(len(response), const.HEADER_SIZE)
                data = responseSize + response
                send_data(cliSocket, data)

            # quit
            # closes the connection
            elif query == const.COMMANDS[3]:
                cliSocket.close()
                print("Connection closed")
                break

            else:
                print("Invalid command. Closing connection")
                cliSocket.close()
                break


if __name__ == '__main__':
    run(sys.argv)