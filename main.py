import numpy as np
import matplotlib.pyplot as plt
def Loss(theta):
    return theta**2 - theta * 4 + 10

theta = np.arange(-4, 8, 0.1)
loss = Loss(theta)
plt.plot(theta, loss)
# plt.show()

def DerLoss(theta):
    return 2 * theta - 4

theta = -4
alpha = 0.01
es = 0.0001

while True:
    theta = theta - alpha * DerLoss(theta)
    plt.plot(theta, Loss(theta), 'ro')
    plt.pause(0.3)
    if abs(DerLoss(theta)) < es:
        break
plt.show()
print(Loss(theta))
print(theta)