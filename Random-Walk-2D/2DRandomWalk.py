
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
import random as r
import math
import os
import time

start = time.time()

count1 = 0
count2 = 0

#PARAMETERS
id = 97
board_size = 100
n_steps = 1000
n_walkers = 100
n_iter = 10000
anim_speed = 10
zero_frame = np.zeros((board_size, board_size))

ende1 = time.time()

#WALKER CLASS
class Walker:
    def __init__(self, x, y):

        self.pos = np.array([x, y])

        # step choices
        self.dirs = np.array([
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
            [0, 0]
        ])

    def move(self, frame, count1):
        step = r.choice(self.dirs)
        s_x, s_y = (self.pos + step) % board_size

        if 1: #frame[s_x, s_y] == 0:
            count1 +=1
            frame[self.pos[0], self.pos[1]] = 0
            self.pos = np.array([s_x, s_y])

        frame[self.pos[0], self.pos[1]] = 1
        return count1

ende2 = time.time()

#INITIALIZING ARRAYS
frames = []
walkers = []
added_frames = []

for i in range(n_iter):
    frames.append(zero_frame.copy())
    walkers.append([])
    for j in range(n_walkers):
        walkers[i].append(
            Walker(math.floor(board_size/2), math.floor(board_size/2)))

ende3 = time.time()

#MAIN LOOP
for k in range(n_steps):
    for i in range(n_iter):
        for j in range(n_walkers):
            count1 = walkers[i][j].move(frames[i],count1)
            count2+=1
    added_frames.append(sum(frames))
    print(k/n_steps)

ende4 = time.time()

#ANIMATION
if 1:
    # Update Function for Animation
    def update(i):
        fig.clear()
        ax = fig.add_subplot(111)
        ax.set_title('2D Random walk without SE')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        map = ax.matshow(added_frames[i*anim_speed], cmap='gray', vmin=0,
                         vmax=n_iter*n_walkers/(board_size*board_size)*2)
        #cb = fig.colorbar(map)

    # Animation
    fig, ax = plt.subplots(figsize=(6, 6))
    animation = FuncAnimation(
        fig=fig,
        func=update,
        frames=int(n_steps/anim_speed),
        interval=60
    )

    animation.save(f'Resources/Solves/{id}RandomWalk2D.gif')

ende5 = time.time()

print("\n",f"denied moves: {count2 - count1}")
print("\n","Timing: ")
print(f"Total: {ende5 - start}")
print(f" Loading Parameters: {ende1 - start}")
print(f" Loading Walker class: {ende2 - ende1}")
print(f" Initializing Arrays: {ende3 - ende2}")
print(f" Main Loop: {ende4 - ende3}")
print(f" Animation: {ende5 - ende4}")

