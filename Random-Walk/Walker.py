
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as r
import time
import math

# WALKER CLASS
class Walker:
    def __init__(self, x, y, bs):

        self.pos = np.array([x, y])
        self.board_size = bs

        # step choices
        self.dirs = np.array([
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
            [0, 0]
        ])

    def __str__(self) -> str:
        return f"{self.pos[0]} {self.pos[1]}"

    def move(self, frame, SE):
        step = r.choice(self.dirs)
        s_x, s_y = (self.pos.copy() + step) % self.board_size

        if frame[s_x, s_y] == 0 or SE == "without":
            frame[self.pos[0], self.pos[1]] -= 1
            self.pos = np.array([s_x, s_y])
            frame[self.pos[0], self.pos[1]] += 1


def calc_iterated_boards(params):
    start = time.time()
    [name,
     board_size,
     n_steps,
     n_walkers,
     n_iter,
     anim_speed,
     size_exclusion,
     ] = params

    zero_frame = np.zeros((board_size, board_size))

    # INITIALIZING ARRAYS
    frames = []
    walkers = []
    added_frames = []
    initFrame = zero_frame.copy()

    for i in range(n_iter):
        frames.append(zero_frame.copy())
        walkers.append([])
        for j in range(n_walkers):
            walkers[i].append(
                Walker(math.floor(board_size/2), math.floor(board_size/2), board_size))
            frames[i][math.floor(board_size/2)][math.floor(board_size/2)] += 1

    # MAIN LOOP
    for k in range(n_steps):
        added_frames.append(sum(frames))
        for i in range(n_iter):
            r.shuffle(walkers[i])
            for j in range(n_walkers):
                walkers[i][j].move(frames[i], size_exclusion)
        print(round(k/n_steps, 3))

    end = time.time() 
    print("crunching took ", end-start, " seconds yummy")

    return added_frames

# CSV EXPORT
def export_as_csv(iterated_boards, params):
    [name,
     board_size,
     n_steps,
     n_walkers,
     n_iter,
     anim_speed,
     size_exclusion,
     ] = params

    dataframe = pd.DataFrame(
        list(np.array(iterated_boards, dtype=int).reshape(board_size*n_steps, board_size)))
    dataframe.to_csv(f'Resources/Data/{name}RW2D{size_exclusion}SE.csv')

    print("Data was saved under ",
      f'Resources/Data/{name}RW2D{size_exclusion}SE.csv')


# ANIMATION
def animate(iterated_boards, params):

    [name,
     board_size,
     n_steps,
     n_walkers,
     n_iter,
     anim_speed,
     size_exclusion, ] = params

    # Update Function for Animation
    def update(i):
        fig.clear()
        ax = fig.add_subplot(111)
        ax.set_title(f'2D Random Walk {size_exclusion} SE')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        map = ax.matshow(iterated_boards[i*anim_speed], cmap='gray', vmin=0,vmax=n_iter*n_walkers/(board_size*board_size)*2)
        cb = fig.colorbar(map)

    # Animation
    fig, ax = plt.subplots(figsize=(6, 6))
    animation = FuncAnimation(
        fig=fig,
        func=update,
        frames=int(n_steps/anim_speed)
    )

    animation.save(
        f'Resources/Solves/{name}RW2D{size_exclusion}SE.gif', PillowWriter(fps=24))
    
    print("Animation was saved under ",
      f'Resources/Solves/{name}RW2D{size_exclusion}SE.gif')

