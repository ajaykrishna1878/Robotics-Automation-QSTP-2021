#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, Pose, Quaternion
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist

"""
Agenda:
First find out how to obtain the orientation of the bot
With this orientation, check whether next goal is in the same direction as the bot or opposite
Write an if statement that checks this and if opposite, take the velocity as negative

The main aim is to learn how to obtain the current orientation of the bot
"""

class BotController:
	def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
		self.rate = rospy.Rate(10)
		self.velocity = Twist()
		self.velocity.linear.x = 0
		self.velocity.angular.z = 0
		self.goal_x = 0
		self.goal_y = 0

	def pose_callback(self, msg):

        self.x_pose = msg.pose.pose.position.x
        self.y_pose = msg.pose.pose.position.y
        quaternion = msg.pose.pose.orientation
        (roll, pitch, self.yaw) = euler_from_quaternion([quaternion.x, quaternion.y, quaternion.z, quaternion.w])

    def goal_callback(self, msg):
    	self.goal_x = msg.pose.position.x
    	self.goal_y = msg.pose.position.y

    def get_goal(self):
    	goal_sub = rospy.Subscriber('/thief_pose', PoseStamped, self.goal_callback)

    def calculations(self):
    	odom_sub = rospy.Subscriber('/odom', Odometry, self.pose_callback)
    	self.get_goal()
    	#count = 1
    	
        pid_dist = pid_controller(0.2, 0, 0, 0.5)
        pid_yaw = pid_controller(0.2, 0, 0, 0.5)
        while not rospy.is_shutdown():
            distance = math.sqrt(math.pow((self.goal_x - self.x_pose), 2) + math.pow((self.goal_y - self.y_pose), 2))


            if distance >= 1.:
                psi = math.atan((self.goal_y - self.y_pose)/(self.goal_x - self.x_pose))
                
                if self.goal_y-self.y_pose >= 0 and self.goal_x-self.x_pose >= 0:
                    error = abs(psi) - self.yaw
                elif self.goal_y-self.y_pose <= 0 and self.goal_x-self.x_pose >= 0:
                    error = -abs(psi) - self.yaw
                elif self.goal_y-self.y_pose >= 0 and self.goal_x-self.x_pose < 0:
                    if self.yaw < -0.1:
                        self.yaw += 2 * math.pi
                        error = math.pi - abs(psi) - self.yaw
                        self.yaw = self.yaw - 2*math.pi
                    else:
                        error = math.pi - abs(psi) - self.yaw
                elif self.goal_y-self.y_pose <= 0 and self.goal_x-self.x_pose <= 0:
                    if self.yaw < -0.1:
                        self.yaw += 2 * math.pi
                        error = math.pi + abs(psi) - self.yaw
                        self.yaw = self.yaw - 2*math.pi
                    else:
                        error = math.pi + abs(psi) - self.yaw

                
                out_yaw = pid_yaw.set_current_error(error)
                out_distance = pid_dist.set_current_error(distance)
                self.action(out_distance, out_yaw)

            else:
            	print("Caught you!")

            self.rate.sleep()

    def action(self, d, y):
        self.velocity.linear.x = d
        self.velocity.angular.z = y
        self.pub.publish(self.velocity)

class pid_controller:
    def __init__(self, p, i, d, lim):
        self.kp = p
        self.ki = i
        self.kd = d
        self.lim = lim
        self.prev_error = 0.0
        self.error_int = 0

    def set_current_error(self, error):
        output_p = error * self.kp

        error_diff = error - self.prev_error
        output_d = error_diff * self.kp

        self.error_int = self.error_int + self.prev_error
        output_i = self.ki * self.error_int

        self.prev_error = error
        output = output_p + output_i + output_d

        if output > self.lim:
            output = self.lim
        elif output < (-self.lim):
            output = (-self.lim)

        return output

if __name__ == '__main__':
    rospy.init_node('PID_Controller')
    #if len(sys.argv) == 2:
    #    path = str(sys.argv[1])
    a = BotController()
    a.calculations()
    rospy.spin()