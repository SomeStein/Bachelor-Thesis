from Animation import load_matrizes_from_csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


set0 = np.array(load_matrizes_from_csv("PDSim-System/Resources/RW_150x1_a20_s300_i10000_SE", 1))
set1 = np.array(load_matrizes_from_csv("PDSim-System/Resources/RW_150x1_a20_s300_i10000_fr0", 1))
set2 = np.array(load_matrizes_from_csv("PDSim-System/Resources/RW_150x1_a20_s300_i10000_fr1", 1))
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


#3 subplots of bars of the sets 0 to 2 
# def plot(i):

#     print(i)
    
#     axes[0].clear()
#     axes[1].clear()
#     axes[2].clear()
    
#     X = list(range(60))
    
#     axes[0].set_ylim(0,2.5)
#     axes[1].set_ylim(0,2.5)
#     axes[2].set_ylim(0,2.5)
    
    
#     axes[0].set_title("Sequential")
#     axes[1].set_title("Friction: 0")
#     axes[2].set_title("Friction: 1")
    
#     axes[0].bar(X,set0[i][0])
#     axes[1].bar(X,set1[i][0])
#     axes[2].bar(X,set2[i][0])

#     for ax in fig.get_axes():
#         ax.label_outer()

# fig, axes = plt.subplots(1, 3, figsize=(6, 2), dpi=250)

def plot(i):
   print(i)
   axe.clear()
   axe.set_ylim(-0.4,0.4)
   axe.set_title("comparison friction \n step: {}".format(i))
   axe.set_xlabel("position")
   axe.set_ylabel("difference in population density")
   X = list(range(150))
   axe.bar(X,set1[i][0]-set2[i][0])
   
        
fig, axe = plt.subplots(1,1)    
  
animation = FuncAnimation(fig, plot, 301)
#animation.save("ThesisLatex/content/figures/RW_" + "comparison_friction.gif", PillowWriter(fps=5))
animation.save("PDSim-System/Resources/" + "comparison_friction_w150_a20.gif", PillowWriter(fps = 24))
   
#plt.savefig( "ThesisLatex/content/figures/pgf_figs/" + "comparison_friction0_friction1.pgf",bbox_inches='tight', pad_inches=0)

#plt.show()
