import numpy as np 
import pandas as pd
import random 
import time

start = time.time()

n_walkers = 30
n_steps = 1000
n_iterations = 100
board_size = 100

frame_list = np.zeros((n_steps,board_size),dtype=int)

def move(pos): 
   return (pos + random.randint(-1, 1))%board_size

for i in range(n_iterations):
   walkers = np.array([ int(board_size/2) for j in range(n_walkers)],dtype=int)
   for k in range(n_steps):
      walkers_next = np.array(list(map(move, walkers)),dtype=int)
      # check if there are recurrences
      random.shuffle(walkers)
      for j1 in range(len(walkers)):
         walkerj1 = walkers_next[j1]
         for j2 in range(j1+1, n_walkers):
            if walkerj1 == walkers_next[j2]:
               walkers_next[j2] = walkers[j2]
         frame_list[k,walkerj1] +=1
      walkers = walkers_next
   print(i,time.time()-start)

print(time.time()-start)

dataframe = pd.DataFrame(list(frame_list.reshape((n_steps,board_size))))
dataframe.to_csv(f'Resources/Data/parallelRW1Dtest2.csv')