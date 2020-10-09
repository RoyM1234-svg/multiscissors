import socket


class Network():
    # PORT = 5050
    # SERVER = "192.168.0.107"
    # FORMAT = "utf-8"
    # ADDR = (SERVER,PORT)
    # DISCONNECT_MESSAGE = "!DISCONNECT"

    # client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # client.connect(ADDR)

    # def send(msg):
    #     message = msg.encode(FORMAT)
    #     msg_length = len(message)
    #     send_length = str(msg_length).encode(FORMAT)
    #     send_length += b' ' * (HEADER - len(send_length))
    #     client.send(send_length)
    #     client.send(message)
    #     print(client.recv(2048).decode(FORMAT))
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.0.107"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.id = self.connect()
        self.format = "utf-8"

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
            print(reply)
            return reply
        except socket.error as e:
            return str(e)

n = Network()
n.send(n.id + ":rock")
print(n.id)

