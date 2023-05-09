from Animation import load_matrizes_from_csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

path = "Resources/RW_30x1_a20_s400_i30000"
SI = np.array(load_matrizes_from_csv(path + "_SI", 1))
SEQ = np.array(load_matrizes_from_csv(path + "_SE", 1))
FR0 = np.array(load_matrizes_from_csv(path + "_fr0", 1))
FR1 = np.array(load_matrizes_from_csv(path + "_fr1", 1))

def HeatSolver(dt, dx, t_max, x_max, k, initial_data):
   s = k*dt/dx**2
   s = 1/3
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

x, T, r, s = HeatSolver(dt = 0.1, dx = 1, t_max= 400, x_max= 29, k = 3, initial_data= [ 0 if i < 10 or i >= 20 else 2 for i in range(30)])


def plot(i):
   print(i)
   ax.clear()
   ax.set_ylim(0,2.5)
   #ax.set_xlim(250,350)
   ax.set_title("comparison RW conflict solutions \n step: {}".format(i))
   ax.set_xlabel("position")
   ax.set_ylabel("population density")
   
   ax.plot(T[i], label='PDE solution')
   ax.plot(SI[i][0], label='Size-Inclusion')
   ax.plot(SEQ[i][0], label='Sequential')
   ax.plot(FR0[i][0], label='Friction: 0')
   ax.plot(FR1[i][0], label='Friction: 1')
   
   ax.legend(loc='upper left')

   
        
# fig, ax = plt.subplots(1,1)    
# animation = FuncAnimation(fig, plot, 101)
# animation.save(path + ".gif", PillowWriter(fps = 10))

fig, axes = plt.subplots(1,3, figsize=(9, 4), sharey=True)


step1 = 60
step2 = 120
step3 = 200

axes[0].set_ylim(0,2.5)
axes[0].set_title(" step: {}".format(step1))
axes[0].set_xlabel("position")
axes[0].set_ylabel("population density")
axes[0].plot(T[step1], label='PDE solution')
axes[0].plot(SI[step1][0], label='Size-Inclusion')
axes[0].plot(SEQ[step1][0], label='Sequential')
axes[0].plot(FR0[step1][0], label='Friction: 0')
axes[0].plot(FR1[step1][0], label='Friction: 1')

axes[1].set_ylim(0,2.5)
axes[1].set_title(" step: {}".format(step2))
axes[1].set_xlabel("position")
axes[1].plot(T[step2], label='PDE solution')
axes[1].plot(SI[step2][0], label='Size-Inclusion')
axes[1].plot(SEQ[step2][0], label='Sequential')
axes[1].plot(FR0[step2][0], label='Friction: 0')
axes[1].plot(FR1[step2][0], label='Friction: 1')

axes[2].set_ylim(0,2.5)
axes[2].set_title(" step: {}".format(step3))
axes[2].set_xlabel("position")
axes[2].plot(T[step3], label='PDE solution')
axes[2].plot(SI[step3][0], label='Size-Inclusion')
axes[2].plot(SEQ[step3][0], label='Sequential')
axes[2].plot(FR0[step3][0], label='Friction: 0')
axes[2].plot(FR1[step3][0], label='Friction: 1')

axes[2].legend(loc='upper right')

fig.savefig("/Users/aaronpumm/Paper_RandomWalk/graphics/graphic_1.pgf")
