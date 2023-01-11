from progressBar import *
import numpy as np
import random as r
import time
import math
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# Agent class for random walk with size exclusion option


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


# heat solver
def FTCS(dt, dy, t_max, y_max, k, T0):
    s = k*dt/dy**2
    y = np.arange(0, y_max+dy, dy)
    t = np.arange(0, t_max+dt, dt)
    r = len(t)
    c = len(y)
    T = np.zeros([r, c])
    T[0, int(49/100*c):int(51/100*c)] = T0
    for n in range(0, r-1):
        print(n, f"von {r-1}")
        j = 0
        T[n+1, j] = T[n, j] + s*(T[n, -1] - 2*T[n, j] + T[n, -1])
        for j in range(1, c-1):
            T[n+1, j] = T[n, j] + s*(T[n, j-1] - 2*T[n, j] + T[n, j+1])
        j = c-1
        T[n+1, j] = T[n, j] + s*(T[n, j-1] - 2*T[n, j] + T[n, j-1])

    return y, T, r, s


# hardcoded parameters for simulation
board_size = 100
n_steps = 1000
n_iter = 100
n_agents = 30
sim_speed = 5

# simulation


def calc_added_frames(size_exclusion, shuffle):
    initial_pos = [math.floor(board_size/2) for j in range(n_agents)]

    agents = []
    frames = []
    added_frames = []
    zero_frame = np.zeros(board_size, dtype=int)

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
            if (shuffle):
                r.shuffle(agents[i])
            for j in range(n_agents):
                agents[i][j].move(frames[i], size_exclusion)

        print(f"calculating frame: {k} of {n_steps}")
    return added_frames


#added_frames_withoutSE = calc_added_frames("without", False)
#added_frames_withSE_seq = calc_added_frames("with", False)
#added_frames_withSE_seq_scrambled = calc_added_frames("with", True)
#added_frames_withSE_parallel = np.loadtxt(open("Resources/Data/parallelRW1Dtest.csv", "rb"), delimiter=",", skiprows=1, usecols=list(range(1, board_size+1)))
added_frames_withSE_parallel = np.loadtxt(open("Resources/Data/parallelRW1Dtest2.csv", "rb"), delimiter=",", skiprows=1, usecols=list(range(1, board_size+1)))

# Update Function for Animation


# def update(i):
#     for ax in axs.flat:
#       ax.clear()
#       ax.set(xlabel='Position x', ylabel='Anzahl Agenten')
#       ax.set_ylim([0, n_agents/2])
#       ax.label_outer()

#     x = np.arange(board_size)

#     y = added_frames_withoutSE[i*sim_speed]/n_iter
#     axs[0, 0].bar(x, y)
#     axs[0, 0].set_title("without SE")

#     y = added_frames_withSE_seq[i*sim_speed]/n_iter
#     axs[0, 1].bar(x, y)
#     axs[0, 1].set_title("with SE")

#     y = added_frames_withSE_seq_scrambled[i*sim_speed]/n_iter
#     axs[1, 0].bar(x, y)
#     axs[1, 0].set_title("with SE scrambled")

#     y = added_frames_withSE_parallel[i*sim_speed]/n_iter
#     axs[1, 1].bar(x, y)
#     axs[1, 1].set_title("with SE parallel")

#     print(i)
dt = 1
dy = 1
k = 0.4
y_max = 100
t_max = 1000
T0 = 15
y, T, r, s = FTCS(dt, dy, t_max, y_max, k, T0)

def update(i):
    ax.clear()
    ax.set(xlabel='Position x', ylabel='Anzahl Agenten')
    ax.set_ylim([0, n_agents/2])
    ax.label_outer()

    x = np.arange(board_size)

    y = added_frames_withSE_parallel[i*sim_speed]/n_iter
    ax.bar(x, y)
    ax.plot(x, T[i*sim_speed, :-1],"r-")
    ax.set_title("Vergleich RW with SE und heat equation in 1D")

    print(i)


# Animation
plt.rc('font', size=20)
fig, ax = plt.subplots(figsize=(8, 8))
#fig.suptitle(f'1D Random Walk \n{n_agents} agents, {n_iter} iterations, {n_steps} steps')
animation = FuncAnimation(
    fig=fig,
    func=update,
    frames=int(n_steps/sim_speed)
)

animation.save(f'Resources/Solves/comparisonRW1DHeatparalleltest.gif', PillowWriter(fps=24))

print()
print("Animation was saved under ", f'Resources/Solves/RW1DSE.gif\n')
