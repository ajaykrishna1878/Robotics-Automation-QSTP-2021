# When there are obstacles

The program written uses a PID controller algorithm to move the turtlebot towards the thief. However, it does not take into account that there could be obstacles in the path.

We first assume the obstacle is non-existent and generate waypoints. We iterate over the line joining each consecutive way points and check if it, and the waypoints, is in the obstacle. If either the line or the waypoints are inside the shape of the obstacle, we remove these waypoints or the line(s) joining them.

We then randomly generate a few points on a shape just bigger than the obstacle. We take a specified circle with a maximum radius centred at the closest waypoint to the obstacle and search among the randomly generated points if any of them are within this radius.

If there are any, we take the closest point among these and join it to the path. Since this point is outside the obstacle, we can treat this as a regular point in the path, and check if the line joining this waypoint and the next point in the path is inside the obstacle, in which case we repeat this process and continue until we find a path that goes across the obstacle.

```text
i = 0
r = r
# some specified radius
obstacle = [set of coordinates describing the obstacle]

while i < len(waypoints)+1:
  if waypoints[i] is in obstacle or line joining waypoints[i] and waypoints[i+1] is in obstacle:
    i = i - 1
    points = [randomly generate points in shape of obstacles]
    
    for j in range(len(points)):
      if points[j] is in circle of radius r centred at waypoints[i]:
        waypoints.append(points[j])
```
