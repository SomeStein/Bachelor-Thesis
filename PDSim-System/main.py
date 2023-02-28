
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
steps = 300
n_iterations = 1000

initial_data = [(i, j) for i in range(width)
                for j in range(height) if (((i-width/2)**2+(j-height/2)**2) < 380 and ((i-width/2)**2+(j-height/2)**2) > 120)]

model = RandomWalkGrid(width, height, initial_data=initial_data)

model.simulate(n_steps=steps, n_iterations=n_iterations,
               size_exclusion=True, parallel=False, friction=0, force_simulation=True)

generate_animation(model.last_save_path, model.width, model.height, model.n_agents,
                   vmax=1, frame_rate=24, n_iterations=n_iterations, use_surface=False, fixed_z_height=4)
