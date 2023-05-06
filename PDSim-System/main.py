
from RW import RandomWalkGrid
from Animation import generate_animation
import numpy as np 

"""
This is the main script that should be used for simulating. 
workflow is:
   * defining a Grid (dimensions)
   * the grid class can: 
   show its current state (terminal, matplot), 
   save its current state (path, current_step), 
   simulate (algorithm parameters, num_steps, save_path, num_iterations) #show current iteration state in terminal
   * render a matplot animation from filepaths (subplots dimensions, size, paths for subplots, matrix or graph)

"""

width = 150
height = 1
steps = 300
n_iterations = 10000

initial_data = [(i, 0) for i in range(70,80)]*2
# initial_data = [(0,0),(1,0),(2,0),(3,0),(4,0),
#                       (1,1),(2,1),      (4,1),
#                 (0,2),(1,2),(2,2),(3,2),(4,2),
#                 (0,3),(1,3),      (3,3),(4,3),
#                 (0,4),(1,4),(2,4),(3,4),(4,4)]

model = RandomWalkGrid(width, height, initial_data=initial_data)

model.simulate(n_steps=steps, n_iterations=n_iterations,
               size_exclusion=True, parallel=False, friction=1, force_simulation=True)

model.simulate(n_steps=steps, n_iterations=n_iterations,
               size_exclusion=True, parallel=True, friction=0, force_simulation=True)

model.simulate(n_steps=steps, n_iterations=n_iterations,
               size_exclusion=True, parallel=True, friction=1, force_simulation=True)

