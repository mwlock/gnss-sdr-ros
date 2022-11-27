#!/usr/bin/env python

import rospy
import socket
from gnss_sdr.msg import GNSSSynchro
from gnss_sdr.msg import Observables

from std_msgs.msg import String

from GNSS_synchro import Gnss_Synchro_UDP

def talker():

    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('GNSSPVT_UDP', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # Create and connect to local UDP endpoint
    UDP_IP = "127.0.0.1"
    UDP_PORT = 1234
    gnss_pvt = Gnss_PVT_UDP(udp_port=UDP_PORT, ip=UDP_IP)
    rospy.loginfo(f"UDP target : {UDP_IP}:{UDP_PORT}")
    rospy.loginfo("Opened UDP socket")

    while not rospy.is_shutdown():
        # Receive data from UDP endpoint
        # data, addr = sock.recvfrom(1050) # buffer size is 1024 bytes
        # rospy.loginfo(f"received message: {data}")

        data = gnss_pvt.receive()
        rospy.loginfo(f"received message: {data}")

        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass