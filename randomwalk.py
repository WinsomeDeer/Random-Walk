import numpy as np
import random
import matplotlib as plt
# Class for the random walk.
class Random_walk:
  # Constructor.
  def __init__(self, n, p, start):
    self.prob = p
    self.steps = n
    self.total = start
  # Compute one step.
  def one_step(self):
    if random.choice([-1,1]) == 1:
      self.total += 1
    else:
      self.total -= 1
  
