#!/usr/bin/env python3

import rospy
from week2.srv import AngularVelocity, AngularVelocityResponse

def compute_angular_velocity(req):
    return AngularVelocityResponse(0.1 / req.radius)

if __name__ == '__main__':
    rospy.init_node('ang_vel_server')
    serv = rospy.Service('compute_ang_vel', AngularVelocity, compute_angular_velocity)
    print('Server initialised.')
    rospy.spin()