import socket

import monitor_pvt_pb2
import gnss_synchro_pb2
from PyQt5.QtNetwork import QUdpSocket, QHostAddress

class Gnss_Synchro_UDP:

    def __init__(self, ip = "127.0.0.1", udp_port :int = 1234, buffer_size :int = 1500):

        self.UDP_IP = ip
        self.UDP_PORT = udp_port
        self.buffer_size = buffer_size

        # Create socket and bind to address
        self.udp_socket = QUdpSocket()
        self.udp_socket.bind(QHostAddress.LocalHost, self.UDP_PORT)

    def receive(self):
        while not self.udp_socket.hasPendingDatagrams():
            pass
        datagram = self.udp_socket.receiveDatagram(self.udp_socket.pendingDatagramSize())
        output = gnss_synchro_pb2.Observables()
        output.ParseFromString(datagram.data().data())
        # print(f"output is: {output}")
        return output