import socket, os, sys

COMMANDS = ["get", "put", "ls", "quit"]
HEADER = 20
BUFFER = 2048

# To run: python3 cli.py <SERVER> <PORT>
if (len(sys.argv) != 3):
    print("Usage: python3 " + sys.argv[0] + " <SERVER> <PORT>")
    sys.exit()

server = sys.argv[1]
port = sys.argv[2]

try:
    cliSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliSocket.connect((server, int(port)))
    print("Connected to " + server + " on port " + port)
except Exception as e:
    print(e)
    sys.exit()

query = ""

while True:
    query = (input("ftp> ")).lower().split()
    print(query)

    # get <FILE NAME>
    # downloads <FILE NAME> from the server
    if (query[0] == COMMANDS[0]):
        if (len(query) != 2):
            print("Usage: get <FILE NAME>")
        else:
            req = query[0] + "||" + query[1]
            cliSocket.send(req.encode("ascii"))
        
    # put <FILE NAME>
    # uploads <FILE NAME> to the server
    elif (query[0] == COMMANDS[1]):
        if (len(query) != 2):
            print("Usage: put <FILE NAME>")
        else:
            file = open("./cliFiles/" + query[1], "r")
            req = query[0] + "||" + query[1]
            # bytes = file.read(BUFFER)
            cliSocket.send(req.encode("ascii"))
        
    # ls
    # lists files on the server
    elif (query[0] == COMMANDS[2]):
        cliSocket.send(query[0].encode("ascii"))
        response = cliSocket.recv(BUFFER)
        print(response)
    
    # quit
    # disconnects from the server and exits
    elif (query[0] == COMMANDS[3]):
        cliSocket.send(query[0].encode("ascii"))
        break
    
    else:
        print("Invalid command")