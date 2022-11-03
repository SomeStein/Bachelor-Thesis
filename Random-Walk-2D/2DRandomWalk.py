
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
import random as r
import math
import os
import time

# initial conditions
board_size = (100, 100)
zero_frame = np.zeros(board_size)
n_steps = 5000
n_walkers = 1000
n_iter = 10000
anim_speed = 10

# switch for step choices
switch = {
    1: [1, 0],
    2: [-1, 0],
    3: [0, 1],
    4: [0, -1],
    5: [0,0]
}

# Agent class for random walk
class Walker:
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __str__(self):
        return "walker koordinates: " + str(self.coords)

    def move(self, frame):
        step = switch.get(r.randint(1, len(switch)))
        s_x = (self.x + step[0]) % board_size[0]
        s_y = (self.y + step[1]) % board_size[1]

        if 1: #frame[s_x , s_y] == 0:
            frame[self.x, self.y] = 0
            self.x = s_x
            self.y = s_y

        frame[self.x, self.y] = 1


# für jede iteration neues frame berechnen durch move der walker  new frame = walker.move
# alle frames aus diesem step aus allen iterationen zusammen addieren und in added_frames[n] speichern
frames = []
walkers = []
added_frames = []


for n in range(n_steps):
    if n == 0:
        start = time.time()
    if n == 10:
        delta = time.time() - start
        print("It will take roughly: ", delta*(n_steps-10)/10, " seconds")
    print(n/n_steps)

    added_frame = zero_frame.copy()

    for i in range(n_iter):
        if n == 0:
            frames.append(zero_frame.copy())
            walkers.append([])
        for j in range(n_walkers):
            if n == 0:
                walkers[i].append(
                    Walker(math.floor(board_size[0]/2), math.floor(board_size[1]/2)))
            walkers[i][j].move(frames[i])
        added_frame = np.add(added_frame, frames[i])
    added_frames.append(added_frame)

print("Anzahl der Frames: ", len(frames))
print("Anzahl der Walker: ", len(walkers)*len(walkers[0]))
print("Anzahl der added Frames: ", len(added_frames))

if 1:
    # Update Function for Animation
    def update(i):
        fig.clear()
        ax = fig.add_subplot(111)
        ax.set_title('2D Random walk without SE')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        map = ax.matshow(added_frames[i*anim_speed], cmap='gray',vmin=0, vmax=n_iter*n_walkers/(board_size[0]*board_size[1])*2)
        #cb = fig.colorbar(map)

    # Animation
    fig, ax = plt.subplots(figsize=(6, 6))
    animation = FuncAnimation(
        fig=fig,
        func=update,
        frames=int(n_steps/anim_speed),
        interval=60
    )

    animation.save('Solves/randomWalkTest.gif')
