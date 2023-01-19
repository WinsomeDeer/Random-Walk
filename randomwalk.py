import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def random_walk(N, pr):
    steps = np.random.choice([-1,1], N, pr)
    total = np.cumsum(steps)
    return steps, total

# Random walk example
N = 100
p = 0.5

X, Y = random_walk(N, p)

# General figure options
fig = plt.figure(figsize=(15, 7))
ax = plt.axes(xlim=(0, N), ylim=(np.min(Y), np.max(Y)))
line, = ax.plot([], [], lw=2)
ax.set_title('2D Random Walk', fontsize=18)
ax.set_xlabel('Steps', fontsize=16)
ax.set_ylabel('Value', fontsize=16)
ax.tick_params(labelsize=12)

def init():
    line.set_data([], [])
    return line,

x, y = [], []

def animate(i):
    x.append(i)
    y.append(Y[i])
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func = init, frames = 500, interval = 1000, blit = True)
plt.show()
