import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Random walk function.
def random_walk(N, pr):
    steps = np.random.choice([-1,1], N, pr)
    steps, total = [0]*N, [0]*N
    for i in range(N):
        steps[i] = np.random.choice([-1, 1])
    total = np.cumsum(steps)
    steps = np.insert(steps, 0, 0)
    total = np.insert(total, 0, 0)
    return steps, total

# Random walk example.
N = 1000
p = 0.5
X, Y = random_walk(N, p)

# General figure options.
fig = plt.figure(figsize=(15, 7))
epsilon = max(np.max(Y), abs(np.min(Y)))
ax = plt.axes(xlim = (0, N+10), ylim = (-2*epsilon, 2*epsilon))
line, = ax.plot([], [], lw = 2)
ax.set_title('Random Walk', fontsize=18)
ax.set_xlabel('Steps', fontsize=16)
ax.set_ylabel('Value', fontsize=16)

# Intialisation function.
def init():
    line.set_data([], [])
    return line,

x, y = [], []

# Animation function
def animate(i, N):
    if(i < N):
        x.append(i)
        y.append(Y[i])
        line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, fargs = (N,), init_func = init, frames = 1100, interval = 50, blit = True)
plt.show()
