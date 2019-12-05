import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def polar_dynamics_x(r1, r2, theta1, theta2):
    x_coord = (r1*np.sin(theta1)) + (r2*np.sin(theta2))
    return x_coord

def polar_dynamics_y(r1, r2, theta1, theta2):
    y_coord = -((r1*np.cos(theta1)) + (r2*np.cos(theta2)))
    return y_coord

def polar_values():
    x = list()
    y = list()
    theta1_values = np.arange(-180, 180, 1)  # (-67, 68, 1)
    theta2_values = np.arange(-100, 100, 1)  # (113, 248, 1)
    for theta1 in theta1_values:
        for theta2 in theta2_values:
            x.append(polar_dynamics_x(48, 48, theta1*(np.pi/180), theta2*(np.pi/180)))
            y.append(polar_dynamics_y(48, 48, theta1*(np.pi/180), theta2*(np.pi/180)))
            yield x, y

def animate(i):
    try:
        content = next(instance)
        sc.set_offsets(np.c_[content[0], content[1]])
    except:
        pass

x = list()
y = list()

instance = polar_values()
fig = plt.figure(figsize = (10, 10))
ax1 = fig.add_subplot()
sc = ax1.scatter(x, y)
plt.xlim(-100, 100)
plt.ylim(-100, 100)  # (-50, 50)
ani = animation.FuncAnimation(fig, animate, frames = 1, interval = 1)
plt.show()
