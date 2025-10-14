#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
def callback(msg):
	rospy.loginfo("I heard %s", msg.data)
rospy.init_node('listener')
rospy.Subscriber('even_numbers', Int32, callback, queue_size=10)
rospy.spin()
