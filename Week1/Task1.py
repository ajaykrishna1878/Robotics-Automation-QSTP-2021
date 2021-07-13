import numpy as np
import math
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):
        for i in range(0, n):
            self.x += v * math.cos(self.theta) * self.dt
            self.y += v * math.sin(self.theta) * self.dt
            self.theta += w * self.dt
            self.x_points.append(self.x)
            self.y_points.append(self.y)
        return self.x, self.y, self.theta

    def plot(self, v: float, w: float):
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color = 'r', alpha = 0.75)
        for i in range(len(self.x_points)):
            plt.scatter(self.x_points[i], self.y_points[i], color = 'r')
            # print("x coordinate: ", i, round(self.x_points[i], 3))
            # print("y coordinate: ", i, round(self.y_points[i], 3))
        plt.show()
        # plt.savefig(f"Unicycle_{v}_{w}.png")

if __name__ == '__main__':
    print("Unicycle Model Assignment")
    case1 = Unicycle(0, 0, 0, 0.1)
    x1, y1, theta1 = case1.step(1, 0.5, 25)
    # print(round(x1, 3), round(y1, 3), theta1)
    case1.plot(1, 0.5)

    case2 = Unicycle(0, 0, 1.57, 0.2)
    x2, y2, theta2 = case2.step(0.5, 1, 10)
    # print(round(x2, 3), round(y2, 3), theta2)
    case2.plot(0.5, 1)

    case3 = Unicycle(0, 0, 0.77, 0.05)
    x3, y3, theta3 = case3.step(5, 4, 50)
    # print(round(x3, 3), round(y3, 3), theta3)
    case3.plot(5, 4)