import constants as const

# keep sending data until all bytes are sent
def send_data(sock, data):
    data = data.encode("utf-8")
    sentBytes = 0
    while len(data) > sentBytes:
        sentBytes += sock.send(data[sentBytes:])


# keep receiving data until all bytes are received
def receive_data(sock, size):
    # recvBuff = ""

    # while len(recvBuff) <  size:
    #     tmpBuff = sock.recv(size).decode("utf-8")

    #     if not tmpBuff:
    #         break

    #     recvBuff += tmpBuff

    # print(recvBuff)
    # return recvBuff

    return sock.recv(size).decode("utf-8")


# make data size fit in fixed header size
def size_padding(data, size):
    data = str(data)
    while len(data) < size:
        data = "0" + data
    return data
    