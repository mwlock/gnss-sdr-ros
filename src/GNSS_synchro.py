import socket

import gnss_synchro_pb2

class Gnss_Synchro_UDP:

    def __init__(self, ip = "127.0.0.1", udp_port :int =1234, buffer_size :int = 1500):

        self.UDP_IP = ip    
        self.UDP_PORT = udp_port
        self.buffer_size = buffer_size

        # Create socket and bind to address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.UDP_IP, self.UDP_PORT))

    def receive(self):
        gnss_synchro = gnss_synchro_pb2.Observables()
        data, addr = self.sock.recvfrom(self.buffer_size)
        # print(data)

        gnss_synchro.ParseFromString(data)

        # try:
        #     obs = gnss_synchro.ParseFromString(data)
        #     print(obs)
        # except:
        #     print("Error parsing message")

        return gnss_synchro
