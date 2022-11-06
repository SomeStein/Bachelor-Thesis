import numpy as np
import time
import Walker


def parallel(params):
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
    start = time.time()
    last_time = start
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
        if (time.time()-last_time > 0.5 or i == n_iter-1):
            last_time = time.time()
            printProgressBar(i, n_iter-1, start, length=30,
                             prefix="Initializing arrays ")
    print("Starting Iteration Loop",end="\r")

    # MAIN LOOP
    start = time.time()
    last_time = start
    for k in range(n_steps):
        added_frames.append(sum(frames))
        for i in range(n_iter):
            r.shuffle(walkers[i])
            for j in range(n_walkers):
                walkers[i][j].move(frames[i], size_exclusion)
        if (time.time()-last_time > 0.5 or i == n_iter-1):
            last_time = time.time()
            printProgressBar(k, n_steps-1, start, length=30,
                             prefix="Calculating iterations ")

    return added_frames
