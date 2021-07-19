#!/usr/bin/env python3

import rospy
from week2.srv import AngularVelocity
import sys
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

class MoveBot:
    def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.velocity = Twist()
        self.rate = rospy.Rate(5)

    
    def callback(self, msg):
        rospy.wait_for_service('compute_ang_vel')
        try:
            self.the_client = rospy.ServiceProxy('compute_ang_vel', AngularVelocity)
            self.velocity.linear.x = 0.1
            self.data = self.the_client(msg.data)
            self.velocity.angular.z = self.data.ang_vel
            print(self.velocity.angular.z)
        except rospy.ServiceException as e:
            self.velocity.linear.x = 0
            self.velocity.angular.z = 0
            print("Service call failed: %s"%e)
        
    def subscribeToIt(self):
        self.sub = rospy.Subscriber('/radius', Float32, self.callback)
        
    def publishIt(self):
        self.subscribeToIt()
        while not rospy.is_shutdown():
            print("z=", self.velocity.angular.z)
            self.pub.publish(self.velocity)
            self.rate.sleep()
    

if __name__ == '__main__':
    rospy.init_node('turtlebot_velocity')
    object = MoveBot()
    object.publishIt()
