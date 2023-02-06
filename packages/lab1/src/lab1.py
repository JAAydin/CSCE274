#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

class Lab1:
    def __init__(self):
        rospy.Subscriber("delta", Float32, self.callback)
        self.pub = rospy.Publisher("total", Float32, queue_size=10)
        self.total = 0

    def callback(self, data):
        self.total += data.data
        self.pub.publish(self.total)

if __name__ == '__main__':
    rospy.init_node('lab1')
    Lab1()

    rospy.spin()
