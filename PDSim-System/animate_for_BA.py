from Animation import load_matrizes_from_csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


set0 = np.array(load_matrizes_from_csv("PDSim-System/Resources/RW_60x60_a1200_s400_i1000_SE", 60))
set1 = np.array(load_matrizes_from_csv("PDSim-System/Resources/RW_60x60_a1200_s400_i1000_fr0", 60))
set2 = np.array(load_matrizes_from_csv("PDSim-System/Resources/RW_60x60_a1200_s400_i1000_fr1", 60))
# set3 = np.array(load_matrizes_from_csv("PDSim-System/Resources/RW_100x100_a800_s400_i100_fr0.3", 100))
# set4 = np.array(load_matrizes_from_csv("PDSim-System/Resources/RW_100x100_a800_s400_i100_fr0.6", 100))
# set5 = np.array(load_matrizes_from_csv("PDSim-System/Resources/RW_100x100_a800_s400_i100_fr1", 100))

def HeatSolver(dt, dx, t_max, x_max, k, initial_data):
   s = k*dt/dx**2
   x = np.arange(0, x_max+dx, dx)
   t = np.arange(0, t_max+dt, dt)
   r = len(t)
   c = len(x)
   T = np.zeros([r, c])
   if initial_data:
      T[0] = np.array(initial_data)
   else: 
      T[0, int(c/3):int(2*c/3)] = 1
   for n in range(0, r-1):
      j = 0
      T[n+1, j] = T[n, j] + s*(T[n, -1] - 2*T[n, j] + T[n, -1])
      for j in range(1, c-1):
         T[n+1, j] = T[n, j] + s*(T[n, j-1] - 2*T[n, j] + T[n, j+1])
      j = c-1
      T[n+1, j] = T[n, j] + s*(T[n, j-1] - 2*T[n, j] + T[n, j-1])

   return x, T, r, s

#x, T, r, s = HeatSolver(dt = 0.1, dx = 1, t_max= 300, x_max= 59, k = 1/3, initial_data= [ 0 if i < 20 or i >= 40 else 3 for i in range(60)])


cb = 0

def plot(i):

    print(i)

    global cb
    if cb:
        cb.remove()
    
    matrizes = []

    matrizes.append(np.absolute(set2[i]-set1[i])) 
    matrizes.append(np.absolute(set2[i+50]-set1[i+50]))
    matrizes.append(np.absolute(set2[i+300]-set1[i+300]))
    # matrizes.append(set2[i])
    # matrizes.append(set3[i])
    # matrizes.append(set4[i])
    # matrizes.append(set5[i])
    
    max = np.array(matrizes).max()
    #max = np.absolute(np.subtract(matrizes[0],matrizes[1])).max()
    
    axes[0].clear()
    # axes[0,0].clear()
    # axes[1,0].clear()
    # axes[0,2].clear()
    # axes[1,2].clear()
    # axes[1,1].clear()
    
    mat = axes[0].matshow(matrizes[0],cmap = "viridis",vmax = max,vmin = 0)
    axes[1].matshow(matrizes[1],cmap = "viridis",vmax = max,vmin = 0)
    axes[2].matshow(matrizes[2],cmap = "viridis",vmax = max,vmin = 0)
    # axes[0,1].matshow(matrizes[1],cmap = "viridis",vmax = max)
    # axes[0,2].matshow(matrizes[2],cmap = "viridis",vmax = max)
    # axes[1,0].matshow(matrizes[3],cmap = "viridis",vmax = max)
    # axes[1,1].matshow(matrizes[4],cmap = "viridis",vmax = max)
    # axes[1,2].matshow(matrizes[5],cmap = "viridis",vmax = max)
    axes[0].set_title(f"Step 0")
    axes[1].set_title(f"Step 50")
    axes[2].set_title(f"Step 300")
    # axes[0,1].set_title(f"Sequential")
    # axes[0,2].set_title(f"friction 0")
    # axes[1,0].set_title(f"friction 0.3")
    # axes[1,1].set_title(f"friction 0.6")
    # axes[1,2].set_title(f"friction 1")
    cb = fig.colorbar(mat, ax = axes, fraction=0.02, pad=0.04, label = "difference in density")

    for ax in fig.get_axes():
        ax.label_outer()
        
fig, axes = plt.subplots(1, 3, figsize=(6, 2), dpi=250)
        
# animation = FuncAnimation(fig, plot, 101)

# animation.save("ThesisLatex/content/figures/RW_" + "comparison_friction.gif", PillowWriter(fps=5))

plot(0)     
plt.savefig( "ThesisLatex/content/figures/pgf_figs/" + "comparison_friction0_friction1.pgf",bbox_inches='tight', pad_inches=0)


