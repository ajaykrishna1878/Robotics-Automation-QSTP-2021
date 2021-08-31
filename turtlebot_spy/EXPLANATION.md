## When there are obstacles

The program written uses a PID controller algorithm to move the turtlebot towards the thief. However, it does not take into account that there could be obstacles in the path. Let's look at how to get around the problem of existence of obstacles.

### Using waypoints

As the title says, we can generate a waypoint around the obstacle. Instead of the thief's pose as the goal, we can take this waypoint as the goal first and then after reaching there, the bot can move to the thief's pose.

The following algorithm can be used assuming we know the shape of the obstacle.

'''text
get obstacle_shape

'''
