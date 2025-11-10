#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray

def callback(data):
    result = []
    for i, num in enumerate(data.data):
        result.append(num ** i)
    pub.publish(Int32MultiArray(data=result))
if __name__ == "__main__":
    rospy.init_node('polynomial_node')
    pub = rospy.Publisher('output_polynomial', Int32MultiArray, queue_size=10)
    sub = rospy.Subscriber('input_polynomial', Int32MultiArray, callback)
    rospy.spin()
