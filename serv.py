import socket, os, sys, subprocess

COMMANDS = ["get", "put", "ls", "quit"]
HEADER = 20
BUFFER = 2048

# To run: python3 serv.py <PORT>
if (len(sys.argv) != 2):
    print("Usage: python3 " + sys.argv[0] + " <PORT>")
    sys.exit()

port = sys.argv[1]

try:
    # bind port and start listening for connections
    servSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servSocket.bind(('', int(port)))
    servSocket.listen(1)
except Exception as e:
    print(e)
    sys.exit()

while True:
    # keep listening for connections until user ends process
    print("Listening on port " + port)
    cliSocket, addr = servSocket.accept()
    print("Connected to: " + addr[0])

    while True:
        query = cliSocket.recv(BUFFER).decode("ascii").split("||")
        print(query)

        # get <FILE NAME>
        # downloads <FILE NAME> from the server
        if(query[0] == COMMANDS[0]):
            print("get not implemented yet")

        # put <FILE NAME>
        # uploads <FILE NAME> to the server
        elif(query[0] == COMMANDS[1]):
            print("put not implemented yet")

        # ls
        # lists files on the server
        elif(query[0] == COMMANDS[2]):
            files = os.listdir("./servFiles")
            # print(files)
            response = ""
            for file in files:
                response += file + "  "
            cliSocket.send(response[:-2].encode("ascii"))

        # quit
        # disconnects from the server and exits
        elif(query[0] == COMMANDS[3]):
            print("Closing connection")
            cliSocket.close()
            break

        else:
            print("Invalid command. Closing connection")
            cliSocket.close()
            break


def recieve_file(cliSocket):
    # create new channel to transfer data
    # indicate success or fail
    # print file name and number of bytes transferred
    # tear down connection

    # try:
    #     dataSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     dataSocket.bind(('', 0))
    #     dataSocket.listen(1)
    # except Exception as e:
    #     print(e)
    #     return
    return ""
    

def send_file():
    # create new channel to transfer data
    # indicate success or fail
    # print file name and number of bytes transferred
    # tear down connection
    return ""
