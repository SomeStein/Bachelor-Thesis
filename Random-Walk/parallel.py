import numpy as np 
import pandas as pd
import random
import time

start = time.time()

n_walkers = 100
n_steps = 800
n_iterations = 100
n_matrix = 50

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

for i in range(n_iterations):
   walkers = np.array([[5,5]for j in range(n_walkers)],dtype=int)
   for k in range(n_steps):
      walkers_next = np.array(list(map(move, walkers)),dtype=int)
      # check if there are recurrences
      for j1 in range(len(walkers)):
         walkerj1 = walkers_next[j1]
         for j2 in range(j1+1, len(walkers)):
            if np.equal(walkerj1,walkers_next[j2]).all():
               walkers_next[j2] = walkers[j2]
         frame_list[k,walkerj1[0],walkerj1[1]] +=1
      walkers = walkers_next
   print(i,time.time()-start)

print(time.time()-start)

dataframe = pd.DataFrame(list(frame_list.reshape((n_steps*n_matrix,n_matrix))))
dataframe.to_csv(f'Resources/Data/parallelRW2D.csv')
      


