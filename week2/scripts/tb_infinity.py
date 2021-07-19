#!/usr/bin/env python3

import rospy
from week2.srv import AngularVelocity
import sys
import math
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

class Infinity:
    def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.velocity = Twist()
        self.rate = rospy.Rate(10)
        self.time_period = 0
        self.omega = 0
    
    def callback(self, msg):
        rospy.wait_for_service('compute_ang_vel')
        try:
            self.client_var = rospy.ServiceProxy('compute_ang_vel', AngularVelocity)
            self.data = self.client_var(msg.data)
            self.omega = self.data.ang_vel
            self.time_period = 20 * math.pi / (self.omega) #since rate is 10
        except rospy.ServiceException as e:
            self.velocity.linear.x = 0
            self.velocity.angular.z = 0
            print("Service call failed: %s"%e)

    def subscribeToIt(self):
        self.sub = rospy.Subscriber('/radius', Float32, self.callback)

    
    def publishIt(self):
        self.subscribeToIt()
        self.count = 1
        self.pubcount = 0

        while not rospy.is_shutdown():
            '''
            It takes a few milliseconds after the node starts to get any published messages on /radius.
            This time is the same amount of time as it takes for 5 messages for this node to publish.
            Hence the following if statement is used. pubcount is used since if and the following elif statements clash.
            '''
            if self.count < 5 and self.pubcount == 0:
                self.count += 1
                if self.count == 5:
                    self.count = 0
                    self.pubcount += 1
            elif self.count <= self.time_period / 2 and self.pubcount > 0:
                self.velocity.linear.x = 0.1
                self.velocity.angular.z = self.omega
                self.count += 1
            elif self.count > self.time_period / 2 and self.count <= 3 * self.time_period / 2 and self.pubcount > 0:
                self.velocity.linear.x = 0.1
                self.velocity.angular.z = -self.omega
                self.count += 1
            elif self.count > 3 * self.time_period / 2 and self.count <= 2 * self.time_period and self.pubcount > 0:
                self.velocity.linear.x = 0.1
                self.velocity.angular.z = self.omega
                self.count += 1
                if self.count > 2 * self.time_period:
                    self.count = 0
            #print(self.count)
            self.pub.publish(self.velocity)
            self.rate.sleep()
    

if __name__ == '__main__':
    rospy.init_node('infinity')
    object = Infinity()
    object.publishIt()