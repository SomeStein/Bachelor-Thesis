
from RW import RandomWalkGrid
from Animation import generate_animation

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

width = 50
height = 50
n_iterations=10000

initial_data = [(int(width/2), int(height/2)) for i in range(100)]

model = RandomWalkGrid(width, height, initial_data=initial_data)

model.simulate(n_steps=500, n_iterations = n_iterations, size_exclusion=True,
               parallel=True, friction=0)

generate_animation(model.last_save_path, model.width,
                   model.height, model.n_agents, vmax = 3000, n_iterations = n_iterations)
