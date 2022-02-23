import matplotlib.pyplot as plt
from time import sleep
import numpy as np

theta = [x+1 for x in range(5)]
r = np.sin(theta)

fig = plt.figure()

fig.set_facecolor('tab:blue')

ax = fig.add_subplot(111, polar=True)
ax.set_autoscale_on(True)
ax.set_facecolor('tab:blue')

c = ax.scatter(theta, ['10cm','30cm','60cm','90cm','100cm'], c=r, s=30, cmap='hsv', alpha=1)
x = [x for x in range(5)]

line, = ax.plot([1,1,1,1,1],[0,1,2,3,4],color='red')
ax.set_thetamin(0)
ax.set_thetamax(180)
n,forw=0.1,True
ss = 0
import random
while True:
    if forw:n+=0.1
    else:n=n-0.1
    ss+=1
    print(ss,forw)
    c.set_offsets(np.c_[n,1])
    if n >= 3:
        forw = False
    elif n < 0 and not forw:
        forw = True
    line.set_xdata([n for x in range(5)])
    ax.relim()
    plt.draw()
    plt.pause(0.20)

