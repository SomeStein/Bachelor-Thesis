
from RW import RandomWalkGrid
from Animation import generate_animation
import numpy as np
from itertools import chain
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

height = 1
n_iterations = 30000

parameters = [ (30, 400, [(i,0) for i in range(10,20)]*2)]

for width, steps, initial_data in parameters:

   model = RandomWalkGrid(width, height, initial_data=initial_data)
   
   model.simulate(n_steps=steps, n_iterations=n_iterations,
                  size_exclusion=False, parallel=False, friction=0, folder_path=f"Resources", force_simulation=True)
   generate_animation(model.last_save_path, model.width, model.height, len(model.agents), n_iterations,
                      vmax=2.5, save_path=0, frame_rate=10, fixed_z_height=3.5, cmap="viridis", image_size=5, use_surface=False)
   
   model.simulate(n_steps=steps, n_iterations=n_iterations,
                  size_exclusion=True, parallel=False, friction=0, folder_path=f"Resources", force_simulation=True)
   generate_animation(model.last_save_path, model.width, model.height, len(model.agents), n_iterations,
                      vmax=2.5, save_path=0, frame_rate=10, fixed_z_height=3.5, cmap="viridis", image_size=5, use_surface=False)
   
   model.simulate(n_steps=steps, n_iterations=n_iterations,
                  size_exclusion=True, parallel=True, friction=0, folder_path=f"Resources", force_simulation=True)
   generate_animation(model.last_save_path, model.width, model.height, len(model.agents), n_iterations,
                      vmax=2.5, save_path=0, frame_rate=10, fixed_z_height=3.5, cmap="viridis", image_size=5, use_surface=False)
   
   model.simulate(n_steps=steps, n_iterations=n_iterations,
                  size_exclusion=True, parallel=True, friction=1, folder_path=f"Resources", force_simulation=True)
   generate_animation(model.last_save_path, model.width, model.height, len(model.agents), n_iterations,
                      vmax=2.5, save_path=0, frame_rate=10, fixed_z_height=3.5, cmap="viridis", image_size=5, use_surface=False)

   

