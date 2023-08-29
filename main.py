import numpy as np

def Loss(theta):
    return theta**2 - theta * 4 + 10

def DerLoss(theta):
    return 2 * theta - 4

theta = -5
alpha = 0.01
es = 0.0001

while True:
    theta = theta - alpha * DerLoss(theta)
    if (abs(DerLoss(theta)) < es):
        break
print(Loss(theta))
print(theta)