#!/usr/bin/env python3

import rospy
import math
from week2.srv import Trajectory, TrajectoryResponse

class BotTrajectory:
    def __init__(self):
        self.dt = 0.05
        self.n = 50

    def server(self, request):
        self.request = request
        self.x = request.x
        self.y = request.y
        self.v = request.v
        self.w = request.w
        self.theta = request.theta
        self.x_points = [self.x]
        self.y_points = [self.y]
        for i in range(0, (self.n) - 1):
            self.x += self.v * math.cos(self.theta) * self.dt
            self.y += self.v * math.sin(self.theta) * self.dt
            self.x_points.append(self.x)
            self.y_points.append(self.y)
            self.theta += self.w * self.dt
        return TrajectoryResponse(x_points=(self.x_points), y_points=(self.y_points))

if __name__ == '__main__':
    rospy.init_node('trajectory_server')
    bot = BotTrajectory()
    serv = rospy.Service('bot_trajectory', Trajectory, bot.server)
    print('Server initialised.')
    rospy.spin()