import numpy as np
d = 5
def F(w):
    return sum([(w.dot(x)-y)**2 for x,y in points])/len(points)
def dF(w):
    return sum([2*(w.dot(x)-y)*x for x,y in points])/len(points)

realW = [1,2,3,4,5]
def generate_points(realW):
    for j in range(10000):
        g = np.random.randn(d) + np.random.randn()
        y = g.dot(realW)
        points.append((g,y))
    return points
points = generate_points(realW)

def training(a):
    alpha = 0.001
    for i in range(50):
        v = F(a)
        derivative = dF(a)
        a = a - alpha * derivative
        print('Iteration {}, a = {}')
    return a

w= np.zeros(b)
w = training(w)
