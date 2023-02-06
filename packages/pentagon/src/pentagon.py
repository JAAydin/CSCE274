#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Twist2DStamped

pub = rospy.Publisher("/lilduckie/car_cmd_switch_node/cmd",Twist2DStamped,queue_size=10)

def pentagonSegment():
    rate = rospy.Rate(1)
    # Traverse side of pentagon
    cmd = Twist2DStamped()
    cmd.v = 0.432
    cmd.omega = 0.0
    cmd.header.stamp = rospy.Time.now()
    pub.publish(cmd)

    rate.sleep()
    # Turn corner
    cmd.v = 0.0
    cmd.omega = 4.0
    cmd.header.stamp = rospy.Time.now()
    pub.publish(cmd)

    rate.sleep()

def stop():
    cmd = Twist2DStamped()
    cmd.v = 0.0
    cmd.omega = 0.0
    cmd.header.stamp = rospy.Time.now()

    pub.publish(cmd)

def idek(): # My duckie was ignoring the first few commands I was sending so I used this to make sure it got all of the commands
    rate = rospy.Rate(1)

    cmd = Twist2DStamped()
    cmd.v = 0.0
    cmd.omega = 0.0
    cmd.header.stamp = rospy.Time.now()
    for i in range(0,10):
        pub.publish(cmd)
        rate.sleep()

try:
    rospy.init_node("pentagon")
    idek()
    for i in range(0,5):
        pentagonSegment()
except rospy.ROSInterruptException:
    pass
finally:
    stop()