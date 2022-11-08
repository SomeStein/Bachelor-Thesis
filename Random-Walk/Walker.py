
from progressBar import *
import numpy as np
import random as r
import time
import math

# WALKER CLASS
class Walker:
    def __init__(self, x, y, bs):

        self.pos = np.array([x, y],dtype=int)
        self.board_size = bs

        # step choices
        self.dirs = np.array([
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ],dtype= int)

        self.stay_chance = 1/len(self.dirs)

    def __str__(self) -> str:
        return f"{self.pos[0]} {self.pos[1]}"

    def move(self, frame, SE):

        if r.random() < self.stay_chance:
            return
        step = r.choice(self.dirs)
        step = (self.pos.copy() + step) % self.board_size

        if SE == "without" or frame[step[0],step[1]] == 0:
            frame[self.pos[0],self.pos[1]] -= 1
            self.pos = step
            frame[self.pos[0],self.pos[1]] += 1



# CALCULATION
def calc_iterated_boards(params,initial_pos = 0):

    [name,
     board_size,
     n_steps,
     n_walkers,
     n_iter,
     anim_speed,
     size_exclusion,
     ] = params

    if not initial_pos:
        initial_pos = [[math.floor(board_size/2), math.floor(board_size/2)] for j in range(n_walkers)]

    
    # INITIALIZING ARRAYS
    start = time.time()
    last_time = start
    frames = []
    walkers = []
    added_frames = []
    zero_frame = np.zeros((board_size, board_size),dtype=int)

    for i in range(n_iter):
        frames.append(zero_frame.copy())
        walkers.append([])
        for j in range(n_walkers):
            walker = Walker(initial_pos[j][0], initial_pos[j][1], board_size)
            walkers[i].append(walker)
            frames[i][initial_pos[j][0]][initial_pos[j][1]] += 1

        #progress bar
        if (time.time()-last_time > 0.5 or i == n_iter-1):
            last_time = time.time()
            printProgressBar(i, n_iter-1, start, length=30,
                             prefix="Initializing arrays ")
    


    # MAIN LOOP
    print("Starting Iteration Loop", end="\r")
    start = time.time()
    last_time = start
    frames = np.array(frames,dtype=int)
    for k in range(n_steps):
        added_frames.append(sum(frames))
        for i in range(n_iter):
            r.shuffle(walkers[i])
            for j in range(n_walkers):
                walkers[i][j].move(frames[i], size_exclusion)

        #progress bar
        if (time.time()-last_time > 0.5 or i == n_iter-1):
            last_time = time.time()
            printProgressBar(k, n_steps-1, start, length=30,
                             prefix="Calculating iterations ")

    return np.array(added_frames,dtype=int)
