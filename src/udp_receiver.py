from PyQt5.QtNetwork import QUdpSocket, QHostAddress, QNetworkDatagram

class UDP_Receiver:

    def __init__(self, udp_port :int, ip = "127.0.0.1"):

        # Set up UDP socket
        self.UDP_IP = ip
        self.UDP_PORT = udp_port

    def __enter__(self):
        # Create socket and bind to address
        self.udp_socket = QUdpSocket()
        self.udp_socket.bind(QHostAddress.LocalHost, self.UDP_PORT)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_socket()

    def receive_datagram(self) -> QNetworkDatagram:
        """ Receive datagram from UDP socket """
        while not self.udp_socket.hasPendingDatagrams():
            pass
        datagram = self.udp_socket.receiveDatagram(self.udp_socket.pendingDatagramSize())
        return datagram

    def close_socket(self):
        """ Close UDP socket """
        self.udp_socket.close()