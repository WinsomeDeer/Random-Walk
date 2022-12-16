import numpy as np
import random
import matplotlib as plt
# Class for the random walk.
class Random_walk:
    # Constructor.
    def __init__(self, n, pr, start):
        self.prob = pr
        self.end = n
        self.total = start
        self.steps = 0
    # Compute one walk.
    def walk(self):
        self.steps = 0
        while(self.steps < self.end):
            self.total += np.random.choice([1,-1], p = [self.prob, 1-self.prob])
            self.steps += 1
        return self.total
    # Compute the number of steps till a certain total is hit.
    def walk_till(self, target):
        self.total = 0
        self.steps = 0
        while(self.total != target):
            self.total += np.random.choice([1,-1], p = [self.prob, 1-self.prob])
            self.steps += 1
        return self.steps
