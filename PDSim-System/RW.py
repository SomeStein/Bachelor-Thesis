
# Imports
import numpy as np
import pandas as pd
import os
import time
import random


# helping function that gives a progressBar in terminal
def printProgressBar(iteration, total, starting_time, prefix='', suffix='', decimals=2, length=30, fill='#', printEnd="\r"):

   percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                    (iteration / float(total)))
   filledLength = int(length * iteration // total)
   bar = fill * filledLength + '-' * (length - filledLength)
   eta = int((time.time()-starting_time)*(total/(iteration+1)-1))
   eta = time.strftime('%H:%M:%S', time.gmtime(eta))
   print(f'\r{prefix} |{bar}| {percent}% {suffix}',
         f"ETA: {eta}", end=printEnd)
   if iteration >= total:
      print(f'{prefix} |{bar}| {percent}% {suffix} ',
            f"({round((time.time()-starting_time),5)} seconds)")

# helping function to find indeces of all occourances of an element in a list
def find_indices(list_to_check, item_to_find):
   indices = []
   for idx, value in enumerate(list_to_check):
      if value == item_to_find:
         indices.append(idx)
   return indices


class RandomWalkGrid:  # Grid class for random walk agents

   # constructor of the Grid class
   def __init__(self,  width=1, height=1, initial_data=0, name="Grid"):

      self.height = height
      self.width = width
      self.name = name

      if not initial_data:
         self.n_agents = width*height
         self.initial_data = [(int(width/2), int(height/2))
                              for i in range(self.n_agents)]

      else:
         self.n_agents = len(initial_data)
         self.initial_data = initial_data

      self.agents = np.array(self.initial_data)

      # create the grid array with name state
      self.state = np.zeros((height, width), dtype=int)

      # spawn agents
      for agent in self.agents:
         self.state[agent[1], agent[0]] += 1

      self.choices = [(0, 0)]

      if self.width > 1:
         self.choices.append((1, 0))
         self.choices.append((-1, 0))

      if self.height > 1:
         self.choices.append((0, 1))
         self.choices.append((0, -1))

   # shows its current state in terminal or as matplotlib render
   def show_current_state(self, location="terminal"):

      if (location == "terminal"):
         # Clear the console before showing the grid
         os.system('clear')

         # Create a 2D list to represent the grid
         grid = [['.'] * self.width for i in range(self.height)]

         # Add agent positions to the grid
         for agent in self.agents:
            grid[agent[1]][agent[0]] = 'x'

         # Print the grid to the console
         for row in grid:
            print(' '.join(row))
         return

      elif (location == "matplotlib"):
         return

      print(f"option {location} not available")

   # gives string for print function
   def __str__(self) -> str:
      # os.system('clear')
      return f"{self.name} - height: {self.height}, width: {self.width} \n\n" + str(self.state) + "\n"

   #algo without size exclusion
   def size_inclusion(self):
      for i in range(self.n_agents):

         dx, dy = random.choice(self.choices)
         x = (self.agents[i][0] + dx) % self.width
         y = (self.agents[i][1] + dy) % self.height

         self.state[self.agents[i][1], self.agents[i][0]] -= 1
         self.agents[i] = (x, y)
         self.state[y, x] += 1

      return self.state
      
   #algo for sequentially updating agents
   def sequential(self):
      
      for i in range(self.n_agents):

            dx, dy = random.choice(self.choices)
            x = (self.agents[i][0] + dx) % self.width
            y = (self.agents[i][1] + dy) % self.height

            if (self.state[y, x] == 0):
               
               
               self.state[self.agents[i][1], self.agents[i][0]] -= 1
               self.agents[i] = (x, y)
               self.state[y, x] += 1
               

      return self.state
   
   #algo for friction based conflict solving
   def parallel(self,friction):
      
      already_checked = []
      desired = []
      gotten = [0]*len(self.agents)

      #choose desired position for every agent
      for i in range(self.n_agents):

         dx, dy = random.choice(self.choices)
         x = (self.agents[i][0] + dx) % self.width
         y = (self.agents[i][1] + dy) % self.height
         desired.append((x, y))
         
      #check for conflicts and resolve them also create a list for the new positions
      for i in range(self.n_agents):
           
         if not i in already_checked:
            if self.state[desired[i][1], desired[i][0]] == 0:           
               if desired.count(desired[i]) == 1:
                  
                  gotten[i] = desired[i]

               else:
                  
                  indices = find_indices(desired, desired[i])
                  already_checked += indices
                  for index in indices:
                     gotten[index] = self.agents[index]
                  
                  if random.random() > friction:
      
                     index = random.choice(indices)
                     gotten[index] = desired[index]
            else:
               
               gotten[i] = self.agents[i]      
                  
                  
      #update positions of agents based on "gotten" list 
      for i in range(self.n_agents):
         agent = self.agents[i]
         gotten_pos = gotten[i]
         
         self.state[agent[1], agent[0]] -= 1
         self.agents[i] = gotten_pos
         self.state[agent[1], agent[0]] += 1

      return self.state
      
    # update position of agents according to parameters
   def update(self, size_exclusion=False, parallel=False, friction=0):
      
      if size_exclusion:
         if parallel:
            return self.parallel(friction)
         else: 
            return self.sequential()
      else:
         return self.size_inclusion()

   # makes a monte carlo simulation saves everything in desired path and gives status updates of the simulation in terminal
   def simulate(self, n_steps=1, n_iterations=1, size_exclusion=False, parallel=False, friction=0, folder_path=None, force_simulation = False):

      #clearing terminal
      os.system("clear")
      
      if not folder_path:
         folder_path = "PDSim-System/Resources"
      if size_exclusion and parallel:
         path = folder_path + f"/RW_{self.width}x{self.height}_a{self.n_agents}_s{n_steps}_i{n_iterations}_fr{friction}"
         
      elif size_exclusion:
         path = folder_path + f"/RW_{self.width}x{self.height}_a{self.n_agents}_s{n_steps}_i{n_iterations}_SE"
         
      else:
         path = folder_path +  f"/RW_{self.width}x{self.height}_a{self.n_agents}_s{n_steps}_i{n_iterations}_SI"
            
            
      self.last_save_path = path
            
      if os.path.isfile(path) and not force_simulation:
         return
            
      # initializing boards
      sums = []
      boards = []
      for i in range(n_iterations):
         boards.append(RandomWalkGrid(
             self.width, self.height, self.initial_data, f"{i}"))

      sum = np.zeros((self.height, self.width))
      for i in range(n_iterations):
         sum += boards[i].state
      sums.append(sum)
      
      # starting time for ETA estimation
      start = time.time()

      # Main Loop
      for k in range(n_steps):

         # initializing sum board
         iteration_sum = np.zeros((self.height, self.width))

         # go through every iteration and calculate one step
         for i in range(n_iterations):

            # add calculated board to sum board
            iteration_sum += boards[i].update(size_exclusion,
                                              parallel, friction)

            # print progress bar
            printProgressBar(k*n_iterations+i+1, n_steps*n_iterations, start)

         # appending calculated sum board for step k to sums list
         sums.append(iteration_sum)

      # after finishing calculation take mean of values 
      sums = np.array(sums)/n_iterations

      # saving data to csv file on path
      if path:
         pd.DataFrame(sums.reshape((self.height*(n_steps+1), self.width))
                      ).to_csv(path, header=None, index=None)

