import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import time

n = 1000
n_steps = 1000
n_iterations = 1000
n_matrix = 100

frame_list = np.zeros((n_steps+1,n_matrix,n_matrix))

dirs = np.array([
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
    [0,0]
])

def move(vec): 
   return vec + random.choice(dirs)

start_time = time.time()
print("starting loop")
for k in range(n_iterations):
   walkers = np.array([[50,50]for i in range(n)])
   for frame in range(n_steps):
      #walkers = walkers + np.random.choice(dirs, n)
      walkers = np.array(list(map(move, walkers ))).clip(0,99)
      frame_list[frame, walkers[:,0], walkers[:,1]] += 1
   print(f"Iteration {k}/{n_iterations}", end="\r")
   if k == 10:
      print((time.time() - start_time)*n_iterations/10)

frame_list = np.array(frame_list)
