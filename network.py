import socket
import pickle


class Network():

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.0.107"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.player_num = self.connect()
        self.format = "utf-8"

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def get_player_num(self):
        return self.player_num

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

# n = Network()
# n.send(n.id + ":rock")
# print(n.id)

