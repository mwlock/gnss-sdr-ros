#!/usr/bin/env python

import rospy
import socket

from gnss_sdr.msg import MonitorPvt

from GNSS_Ros import Gnss_ROS
from udp_receiver import UDP_Receiver

from proto import monitor_pvt_pb2

def publish_gnss_pvt(pvt : monitor_pvt_pb2.MonitorPvt, pub : rospy.Publisher):
    """ Publish a GNSSSynchro message from a Observables message """

    monitor_pvt = MonitorPvt()

    monitor_pvt.tow_at_current_symbol_ms = pvt.tow_at_current_symbol_ms 
    monitor_pvt.week = pvt.week 
    monitor_pvt.rx_time = pvt.rx_time 
    monitor_pvt.user_clk_offset = pvt.user_clk_offset 
    monitor_pvt.pos_x = pvt.pos_x 
    monitor_pvt.pos_y = pvt.pos_y 
    monitor_pvt.pos_z = pvt.pos_z 
    monitor_pvt.vel_x = pvt.vel_x 
    monitor_pvt.vel_y = pvt.vel_y 
    monitor_pvt.vel_z = pvt.vel_z 
    monitor_pvt.cov_xx = pvt.cov_xx 
    monitor_pvt.cov_yy = pvt.cov_yy 
    monitor_pvt.cov_zz = pvt.cov_zz 
    monitor_pvt.cov_xy = pvt.cov_xy 
    monitor_pvt.cov_yz = pvt.cov_yz 
    monitor_pvt.cov_zx = pvt.cov_zx 
    monitor_pvt.latitude = pvt.latitude 
    monitor_pvt.longitude = pvt.longitude 
    monitor_pvt.height = pvt.height 
    monitor_pvt.valid_sats = pvt.valid_sats 
    monitor_pvt.solution_status = pvt.solution_status 
    monitor_pvt.solution_type = pvt.solution_type 
    monitor_pvt.ar_ratio_factor = pvt.ar_ratio_factor 
    monitor_pvt.ar_ratio_threshold = pvt.ar_ratio_threshold 
    monitor_pvt.gdop = pvt.gdop 
    monitor_pvt.pdop = pvt.pdop 
    monitor_pvt.hdop = pvt.hdop 
    monitor_pvt.vdop = pvt.vdop 

    pub.publish(monitor_pvt)

def pvt_ROS():

    pub = rospy.Publisher('/gnss-synchro/pvt', MonitorPvt, queue_size=10)
    rospy.init_node('GNSSPVT_UDP', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # Create and connect to local UDP endpoint
    UDP_IP = "127.0.0.1"
    UDP_PORT = 1111

    rospy.loginfo(f"UDP target : {UDP_IP}:{UDP_PORT}")
    rospy.loginfo("Opened UDP socket")
    
    with UDP_Receiver(ip=UDP_IP, udp_port=UDP_PORT) as udp_receiver:
        while not rospy.is_shutdown():

            datagram = udp_receiver.receive_datagram()
            # print(datagram.data().data())
            msg = Gnss_ROS.parse_pvt(datagram)

            publish_gnss_pvt(msg, pub)

            rate.sleep()

if __name__ == '__main__':
    try:
        pvt_ROS()
    except rospy.ROSInterruptException:
        pass