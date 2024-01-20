import numpy as np

d = 5
points = []


def F(w, k):
    return sum([(w.dot(x) - y) ** 2 for x, y in points[k]]) / len(points[k])


def DF(w, k):
    return sum([2 * (w.dot(x) - y) * x for x, y in points[k]]) / len(points[k])


real_w = [1, 6, 3, 9, 3]


def generatePoints(real_w):
    for j in range(10000):
        g = np.random.randn(d) + np.random.randn()
        y = g.dot(real_w)
        points.append(
            (g, y),
        )
    return points
