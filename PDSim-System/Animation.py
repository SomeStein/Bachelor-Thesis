
# imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.animation import FuncAnimation, PillowWriter

# surpressing scientific notation for numpy matrizes
np.set_printoptions(suppress=True)


# function that loads matrizes from csv
def load_matrizes_from_csv(data_path, height):

   # Load data from CSV file
   data = np.genfromtxt(data_path, delimiter=',')

   # Calculate the number of matrices in the data array
   num_matrices = int(len(data) / height)

   matrizes = []

   # Iterate over each matrix in the data array
   for i in range(num_matrices):
      matrix = np.array(data[i*height:(i+1)*height, :])
      matrizes.append(matrix)

   return matrizes


# function that generates an animation with given parameters

def exponential_cmap(min_val, max_val, gamma):
   norm = mcolors.Normalize(vmin=min_val, vmax=max_val)
   return mcolors.LinearSegmentedColormap.from_list('exp_cmap', [(norm(0.0), "blue"), (norm(0.5 ** gamma), "green"), (norm(1.0), "red")])


def generate_animation(source_path, matrix_width, matrix_height, n_agents, n_iterations, vmax = 1, save_path = 0, frame_rate=24, fixed_z_height=1000, cmap = "viridis", image_size=5, use_surface=False):

   matrices = load_matrizes_from_csv(source_path, matrix_height)
   if not save_path:
      save_path = source_path+".gif"

   fig = plt.figure(figsize=(image_size, image_size))

   def animate(i):
      print(f"\rframe {i} out of {len(matrices)-1}",end="\r")
      fig.clf()
      if use_surface:
         ax = fig.add_subplot(111, projection='3d')
      else:
         ax = fig.add_subplot(111)

      ax.set_title('Frame %d' % i)

      if matrix_height == 1:
         X = list(range(matrix_width))
         Y = matrices[i][0]
         ax.plot(X,Y)
         ax.set_ylim(0,vmax)
         
      elif use_surface:
         X, Y = np.meshgrid(
             range(matrices[i].shape[0]), range(matrices[i].shape[1]))
         ax.plot_surface(X, Y, matrices[i], cmap=cmap, vmin=0, vmax = vmax)
         ax.set_zlim(0, fixed_z_height)
      else:
         ax.matshow(matrices[i], cmap=cmap, vmin=0, vmax = vmax)

   animation = FuncAnimation(fig, animate, frames=len(
       matrices))

   animation.save(save_path, PillowWriter(fps=frame_rate))

