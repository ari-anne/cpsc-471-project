import os, sys
import constants as const
import time

# keep sending data until all bytes are sent
def send_data(sock, data):
    data = data.encode("utf-8")
    sentBytes = 0
    while len(data) > sentBytes:
        sentBytes += sock.send(data[sentBytes:])


# keep receiving data until all bytes are received
def receive_data(sock, size):
                  
        return sock.recv(size).decode("utf-8")
        
# make data size fit in fixed header size
def size_padding(data, size):
    data = str(data)
    while len(data) < size:
        data = "0" + data
    return data

def getFromServer(sock, fileName):
        #Send name of file to receive
        sendName = fileName.encode()
        sock.send(sendName)

        #Receive content size
        contentSize = sock.recv(40)
        contentSize = contentSize.decode()
        contentSize = int(contentSize)

        #Create var to hold incoming data
        full_msg = ""
        while True:
                msg = sock.recv(40)
                full_msg += msg.decode()
                if len(full_msg)==contentSize:
                        sock.send("1".encode())
                        print("Sent True")
                        break

        #Open file path and create file of received data
        fpath = os.path.join(const.CLIENT_FOLDER, fileName)
        fData = open(fpath, "w")
        fData.write(full_msg)

        print("File name is: " + fileName)
        print("Number of bytes transferred: " + str(contentSize))

        return 0

def giveFromServer(sock):
        #Receive what file to send
        fileName = sock.recv(40)
        fileName = fileName.decode()
        
        #Find file and store content for sending
        fpath = os.path.join(const.SERVER_FOLDER, fileName)
        fData = open(fpath)
        content = fData.read()
        
        #Get content length and send content
        contentSize = str(len(content)).encode()
        sock.send(contentSize)
        
        #Send content in .500s intervals until confirmed that all data has been sent
        while True:
                content = content.encode()
                sock.send(content)
                dataRecv = sock.recv(40)
                dataRecv = dataRecv.decode()
                if dataRecv == "1":
                        print("File sent successfully!")
                        break
                time.sleep(.500)
                
        return 0