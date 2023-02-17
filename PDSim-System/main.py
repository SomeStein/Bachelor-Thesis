
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

width = 100
height = 100
n_iterations = 100000

#initial_data = [(int(width/2), int(height/2)) for i in range(100)]
initial_data = [(50,50)]

model = RandomWalkGrid(width, height, initial_data=initial_data)

model.simulate(n_steps=1000, n_iterations=n_iterations,
               size_exclusion=True, parallel=False, friction=0)

generate_animation(model.last_save_path, model.width,
                   model.height, model.n_agents, vmax=1, frame_rate = 24, n_iterations=n_iterations, use_surface=True, fixed_z_height=2)

# generate_animation("PDSim-System/Resources/RW_100x1_a60_s480_i10000_fr0", model.width,
#                    model.height, model.n_agents, vmax = 4, n_iterations = n_iterations)
