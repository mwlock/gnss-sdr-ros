from proto import gnss_synchro_pb2, monitor_pvt_pb2
from PyQt5.QtNetwork import QUdpSocket, QHostAddress, QNetworkDatagram

class Gnss_ROS:

    def __init__(self):
        pass

    @staticmethod
    def parse_synchro(datagram : QNetworkDatagram) -> gnss_synchro_pb2.Observables:
        """ Parse a GNSSSynchro message from a QNetworkDatagram """
        output = gnss_synchro_pb2.Observables()
        output.ParseFromString(datagram.data().data())
        return output

    @staticmethod
    def parse_pvt(datagram: QNetworkDatagram) -> monitor_pvt_pb2.MonitorPvt:
        """ Parse a MonitorPvt message from a QNetworkDatagram """
        output = monitor_pvt_pb2.MonitorPvt()
        output.ParseFromString(datagram.data().data())
        return output