from progressBar import *
import numpy as np
import random as r
import time
import math
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


class Agent:
    def __init__(self, x, bs):

        self.pos = x
        self.board_size = bs

    def __str__(self) -> str:
        return f"{self.pos}"

    def move(self, frame, SE):

        step = r.randint(-1, 1)
        step = (self.pos + step) % self.board_size

        if SE == "without" or frame[step] == 0:
            frame[self.pos] -= 1
            self.pos = step
            frame[self.pos] += 1

name = "test0"
board_size = 100
n_steps = 1000
n_iter = 2000
n_agents = 30
size_exclusion = "with"

initial_pos = [math.floor(board_size/2) for j in range(n_agents)]

agents = []
frames = []
added_frames = []
zero_frame = np.zeros(board_size,dtype=int)

for i in range(n_iter):
   frames.append(zero_frame.copy())
   agents.append([])
   for j in range(n_agents):
      agent = Agent(initial_pos[j], board_size)
      agents[i].append(agent)
      frames[i][initial_pos[j]] += 1

for k in range(n_steps):
   added_frames.append(sum(frames))
   for i in range(n_iter):
      #r.shuffle(agents[i])
      for j in range(n_agents):
         agents[i][j].move(frames[i], size_exclusion)
         
   print(f"calculating frame: {k}")

# Update Function for Animation
def update(i):
   fig.clear()
   ax = plt.axes()
   ax.set_title(f'1D Random Walk {size_exclusion} SE\n{n_agents} walkers, {n_iter} iterations, {n_steps} steps')
   x = np.arange(board_size)
   y = added_frames[i]/n_iter
   ax.bar(x,y)
   ax.set_ylim([0,n_agents/2])
   print(i)
   

# Animation
fig, ax = plt.subplots(figsize=(8, 8))
animation = FuncAnimation(
   fig=fig,
   func=update,
   frames=int(n_steps)
)

animation.save(f'Resources/Solves/{name}RW1D{size_exclusion}SEunscrambled.gif', PillowWriter(fps=24))

print()
print("Animation was saved under ",f'Resources/Solves/{name}RW1D{size_exclusion}SE.gif\n')