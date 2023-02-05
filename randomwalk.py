import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# Random walk function.
class two_dim_rw:
    # Constructor
    def __init__(self, N, pr):
        self.N = N
        self.prob = pr
        self.x, self. y = self.random_walk
    # Methods.
    def random_walk(self):
        steps, total = [0]*self.N, [0]*self.N
        for i in range(self.N):
            steps[i] = np.random.choice([-1, 1])
        total = np.cumsum(steps)
        steps = np.insert(steps, 0, 0)
        total = np.insert(total, 0, 0)
        return steps, total
    # Intialisation function.
    #def init(self):
    #    line.set_data([], [])
    #    return line,
    # Animation function
    def animate(self, i):
        if(i <= self.N):
            self.x.append(i)
            self.y.append(self.y[i])
            line.set_data(self.x, self.y)
        return line,
# Main function
def main():
    N = 100
    p = 0.25
    X = two_dim_rw(N, p)
    # General figure options.
    fig = plt.figure(figsize = (15, 7))
    epsilon = max(np.max(X.y), abs(np.min(X.y)))
    ax = plt.axes(xlim = (0, N+10), ylim = (-2*epsilon, 2*epsilon))
    line, = ax.plot([], [], lw = 2)
    ax.set_title('Random Walk', fontsize = 18)
    ax.set_xlabel('Steps', fontsize = 16)
    ax.set_ylabel('Value', fontsize = 16)
    ax.tick_params(labelsize=12)
    ani = animation.FuncAnimation(fig, X.animate(), fargs = (N,), init_func = init, frames = 500, interval = 50, blit = True)
    plt.show()

if __name__ == '__main__':
    main()
