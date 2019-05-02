import socket

# connect to port
def connect(address, port):
    try:
        newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        newSocket.connect((address, port))
        print("Connected to " + address + " on port " + str(port))
    except Exception as e:
        print(e)
        return None
    return newSocket


# bind port and listen for connections
def bind(port=0):
    try:
        newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        newSocket.bind(('', port))
        newSocket.listen(1)
    except Exception as e:
        print(e)
        return None
    return newSocket
