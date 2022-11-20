#!/usr/bin/env python

import rospy
import socket
from gnss_sdr.msg import GNSSSynchro
from gnss_sdr.msg import Observables

from std_msgs.msg import String

def talker():

    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('GNSSSynchro', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # Connect to local UDP endpoint
    UDP_IP = "127.0.0.1"
    UDP_PORT = 1111
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("UDP target IP:", UDP_IP)
    sock.bind((UDP_IP, UDP_PORT))
    print("Opened UDP socket")

    while not rospy.is_shutdown():
        # Receive data from UDP endpoint
        # data, addr = sock.recvfrom(1050) # buffer size is 1024 bytes
        # print("received message: ", data)
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass