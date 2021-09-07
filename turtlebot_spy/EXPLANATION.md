# When there are obstacles

The program written uses a PID controller algorithm to move the turtlebot towards the thief. However, it does not take into account that there could be obstacles in the path.

We first assume the obstacle is non-existent and generate waypoints. Assuming we know the coordinates of the obstacle, we iterate over the line joining each consecutive way points and check if it, and the waypoints, is in the obstacle. If either the line or the waypoints are inside the shape of the obstacle, we remove these waypoints or the line(s) joining them. We then randomly generate a few points on a shape just bigger than the obstacle. We take a specified circle with a maximum radius centred at the closest waypoint (on the robot's side of the obstacle) and search among the randomly generated points if any of them are within this radius.

If there are any, we take the closest point among these and join it to the path. Since this point is outside the obstacle, we can treat this as a regular point in the path, and check if the line joining this waypoint and the next point in the path is inside the obstacle, in which case we repeat this process and continue until we find a path that goes across the obstacle.
