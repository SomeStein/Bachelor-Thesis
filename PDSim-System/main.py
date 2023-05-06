
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
n_iterations = 10000

parameters = [(60,450, [(i, 0) for i in range(20, 40)]),
              (60,450, [(i, 0) for i in range(20, 40)]*2),
              (60,450, [(i, 0) for i in range(20, 40)]*3),
              (600, 2000,  [(i, 0) for i in range(200, 400)]),
              (600, 2000, [(i, 0) for i in range(200, 400)]*2),
              (600, 2000, [(i, 0) for i in range(200, 400)]*3),
              (600, 2000, [(i, 0) for i in range(250, 350)]),
              (600, 2000, [(i, 0) for i in range(290, 310)]),
              (600, 2000, [(i, 0) for i in range(290, 310)]*2),
              (600, 2000, [(i, 0) for i in range(290, 310)]*3),
              (90, 350, [(i, 0)
               for i in chain(range(10, 20), range(40, 50), range(70, 80))]),
              (90, 400, [(i, 0)
               for i in chain(range(10, 20), range(40, 50), range(70, 80))]*2),
              (90, 500, [(i, 0) for i in chain(range(10, 20), range(40, 50), range(70, 80))]*3)]

for i, (width, steps, initial_data) in enumerate(parameters):

   model = RandomWalkGrid(width, height, initial_data=initial_data)

   model.simulate(n_steps=steps, n_iterations=n_iterations,
                  size_exclusion=True, parallel=False, friction=1, path=f"Resources/{i}", force_simulation=True)

   model.simulate(n_steps=steps, n_iterations=n_iterations,
                  size_exclusion=True, parallel=True, friction=0,path=f"Resources/{i+13}", force_simulation=True)

   model.simulate(n_steps=steps, n_iterations=n_iterations,
                  size_exclusion=True, parallel=True, friction=1, path=f"Resources/{i+26}", force_simulation=True)

   generate_animation(model.last_save_path, model.width, model.height, len(model.agents), n_iterations,
                      vmax=3.5, save_path=0, frame_rate=30, fixed_z_height=3.5, cmap="viridis", image_size=5, use_surface=False)

