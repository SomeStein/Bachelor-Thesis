import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import time

start = time.time()

n_walkers = 100
n_steps = 1000
n_iterations = 1
n_matrix = 10

frame_list = np.zeros((n_steps,n_matrix,n_matrix),dtype=int)

dirs = np.array([
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
    [0,0]
],dtype=int)

def move(vec): 
   return (vec + random.choice(dirs))%n_matrix

for k in range(n_iterations):
   walkers = np.array([[5,5]for i in range(n_walkers)],dtype=int)
   for k in range(n_steps):
      walkers_next = np.array(list(map(move, walkers)),dtype=int)
      # check if there are recurrences
      for j1 in range(len(walkers)):
         for j2 in range(j1+1, len(walkers)):
            if np.equal(walkers_next[j1],walkers_next[j2]).all():
               walkers_next[j2] = walkers[j2]

      walkers = walkers_next
      for walker in walkers:
         frame_list[k,walker[0],walker[1]] +=1

      #print(frame_list[k])
      #print()


print(time.time()-start)
      


