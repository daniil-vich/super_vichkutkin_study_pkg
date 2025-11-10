#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Int32MultiArray, Int32

def callback(data):
    rospy.loginfo("Final result: %d", data.data)
    rospy.signal_shutdown("gotovo")

if __name__ == "__main__":
    rospy.init_node('request_node')
    
    if len(sys.argv) != 4:
        sys.exit(1)
        
    try:
        nums = [int(x) for x in sys.argv[1:4]]
    except:
        sys.exit(1)

    
    pub = rospy.Publisher('input_polynomial', Int32MultiArray, queue_size=10, latch=True)
    sub = rospy.Subscriber('output_summing', Int32, callback)
    
    rospy.sleep(2)
    pub.publish(Int32MultiArray(data=nums))
    rospy.spin()

