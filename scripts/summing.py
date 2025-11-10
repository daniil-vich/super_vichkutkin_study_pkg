#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray, Int32

def callback(data):
    s = sum(data.data)
    pub.publish(s)
if __name__ == "__main__":
    rospy.init_node('summing_node')
    pub = rospy.Publisher('output_summing', Int32, queue_size=10)
    sub = rospy.Subscriber('output_polynomial', Int32MultiArray, callback)+
    rospy.spin()
