#!/usr/bin/env python3
import rospy
import tf
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose
import math

rospy.init_node('turtle_carrot_broadcaster')

turtlename = rospy.get_param('~turtle_tf_name')

start_time = rospy.Time.now().to_sec()
rotation_radius = 1.0  
rotation_speed = 1.0  

def handle_turtle_pose(msg):
    br = tf.TransformBroadcaster()
    br_carrot = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")

    current_time = rospy.Time.now().to_sec()
    angle = rotation_speed * (current_time - start_time)

    carrot_x = rotation_radius * math.cos(angle)
    carrot_y = rotation_radius * math.sin(angle)
    carrot_z = 0

    br_carrot.sendTransform((carrot_x, carrot_y, carrot_z),
                           quaternion_from_euler(0, 0, 0),
                           rospy.Time.now(),
                           "carrot",
                           turtlename)

rospy.Subscriber('input_pose',
                 Pose,
                 handle_turtle_pose)

rospy.spin()
