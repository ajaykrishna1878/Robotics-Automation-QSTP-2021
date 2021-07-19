#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import rospy
from week2.srv import Trajectory

rospy.init_node('trajectory_client')

def get_trajectory(x, y, theta, v, w):
    rospy.wait_for_service('bot_trajectory')
    the_client = rospy.ServiceProxy('bot_trajectory', Trajectory)
    user_data = the_client(x, y, theta, v, w)
    return user_data.x_points, user_data.y_points

def plot_trajectory(x_points, y_points, v, w):
    plt.title(f"Model: {v}, {w}")
    plt.xlabel("X-Coordinates")
    plt.ylabel("Y-Coordinates")
    plt.plot(x_points, y_points, color = 'r')
    for i in range(len(x_points)):
        plt.scatter(x_points[i], y_points[i], color = 'r')
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) == 6:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        theta = float(sys.argv[3])
        v = float(sys.argv[4])
        w = float(sys.argv[5])
    else:
        print("%s [x y theta v w]"%sys.argv[0])
        sys.exit()
    plot_trajectory(get_trajectory(x, y, theta, v, w)[0], get_trajectory(x, y, theta, v, w)[1], v, w)