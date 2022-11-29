#!/usr/bin/env python

import rospy
import socket

from gnss_sdr_msgs.msg import GNSSSynchro
from gnss_sdr_msgs.msg import Observables
from std_msgs.msg import String

from GNSS_Ros import Gnss_ROS
from udp_receiver import UDP_Receiver

from proto import gnss_synchro_pb2, monitor_pvt_pb2

def publish_gnss_synchro(observables : gnss_synchro_pb2.Observables, pub : rospy.Publisher):
    """ Publish a GNSSSynchro message from a Observables message """

    publish_observables = Observables()

    for synchro in observables.observable:

        gnss_synchro = GNSSSynchro()

        gnss_synchro.system = synchro.system
        gnss_synchro.signal = synchro.signal
        gnss_synchro.prn = synchro.prn
        gnss_synchro.channel_id = synchro.channel_id

        gnss_synchro.acq_delay_samples = synchro.acq_delay_samples
        gnss_synchro.acq_doppler_hz = synchro.acq_doppler_hz
        gnss_synchro.acq_samplestamp_samples = synchro.acq_samplestamp_samples
        gnss_synchro.acq_doppler_step = synchro.acq_doppler_step
        gnss_synchro.flag_valid_acquisition = synchro.flag_valid_acquisition    
        
        gnss_synchro.fs = synchro.fs
        gnss_synchro.prompt_i = synchro.prompt_i
        gnss_synchro.prompt_q = synchro.prompt_q
        gnss_synchro.cn0_db_hz = synchro.cn0_db_hz
        gnss_synchro.carrier_doppler_hz = synchro.carrier_doppler_hz
        gnss_synchro.carrier_phase_rads = synchro.carrier_phase_rads
        gnss_synchro.code_phase_samples = synchro.code_phase_samples
        gnss_synchro.tracking_sample_counter = synchro.tracking_sample_counter
        gnss_synchro.flag_valid_symbol_output = synchro.flag_valid_symbol_output
        gnss_synchro.correlation_length_ms = synchro.correlation_length_ms  

        gnss_synchro.flag_valid_word = synchro.flag_valid_word
        gnss_synchro.tow_at_current_symbol_ms = synchro.tow_at_current_symbol_ms

        gnss_synchro.pseudorange_m = synchro.pseudorange_m
        gnss_synchro.rx_time = synchro.rx_time
        gnss_synchro.flag_valid_pseudorange = synchro.flag_valid_pseudorange
        gnss_synchro.interp_tow_ms = synchro.interp_tow_ms
        gnss_synchro.flag_pll_180_deg_phase_locked = synchro.flag_PLL_180_deg_phase_locked

        publish_observables.observable.append(gnss_synchro)

    pub.publish(publish_observables)

def synchro_ROS():

    pub = rospy.Publisher('gnss/syncrho', Observables, queue_size=10)
    rospy.init_node('GNSSSynchro_UDP', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # Create and connect to local UDP endpoint
    UDP_IP = "127.0.0.1"
    UDP_PORT = 1234

    rospy.loginfo(f"UDP target : {UDP_IP}:{UDP_PORT}")
    rospy.loginfo("Opened UDP socket")
    
    with UDP_Receiver(ip=UDP_IP, udp_port=UDP_PORT) as udp_receiver:
        while not rospy.is_shutdown():

            datagram = udp_receiver.receive_datagram()
            # print(datagram.data().data())
            msg = Gnss_ROS.parse_synchro(datagram)

            publish_gnss_synchro(msg, pub)

            rate.sleep()

if __name__ == '__main__':
    try:
        synchro_ROS()
    except rospy.ROSInterruptException:
        pass