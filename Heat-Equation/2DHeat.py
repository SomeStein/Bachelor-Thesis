# 2D Transient Heat Equation for steel plate solver via finite-difference scheme
# Author: Leonardo Antonio de Araujo
# E-mail: leonardo.aa88@gmail.com
# Date: 08/04/2020

import numpy as np
import os
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

clear = lambda: os.system('clear')

# Physical parameters
k = 1.172E-5  # steel, 1% carbon
Lx = 0.1  # length
Ly = 0.1  # width

# Numerical parameters
nx = 100  # number of points in x direction
ny = 100  # number of points in y direction
dt = 0.01  # time step
tf = 100  # final time

# Boundary conditions (Dirichlet)
T0 = 100  # internal field

# Computes cell length
dx = Lx/nx
dy = Ly/ny

# Courant numbers
r1 = k*dt/(dx**2)
r2 = k*dt/(dy**2)

if (r1 > 0.5 or r2 > 0.5):
    raise TypeError('Unstable Solution!')

T = np.zeros((nx, ny, int(tf/dt)))

T[int(nx/2), int(ny/2), 0] = T0

# Generate 2D mesh
X = np.linspace(0, Lx, nx, endpoint=True)
Y = np.linspace(0, Ly, ny, endpoint=True)
X, Y = np.meshgrid(X, Y)

# Main time-loop
for t in range(0, int(tf/dt)-1):
    for i in range(0, nx):
        for j in range(0, ny):
            a = (T[(i+1) % nx, j, t]-2*T[i, j, t]+T[i-1, j, t])/dx**2  # d2dx2
            b = (T[i, (j+1) % ny, t]-2*T[i, j, t]+T[i, j-1, t])/dy**2  # d2dy2
            T[i, j, t+1] = k*dt*(a+b)+T[i, j, t]
    
    clear()
    print(str(t) + " von " + str(int(tf/dt)))
    

 # Update Function for Animation


def update(i):
    fig.clear()
    ax = fig.add_subplot(111)
    ax.set_title('2D Heat equation with periodic BC')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    map = ax.matshow(T[:, :, i*10], cmap='gray', vmin=0, vmax=T0/(nx*ny)*2)
    clear()
    print(str(i) + " von " + str(int(tf/dt/10)-1))
    
    #cb = fig.colorbar(map)

# Animation
fig, ax = plt.subplots(figsize=(6, 6))
animation = FuncAnimation(
    fig=fig,
    func=update,
    frames=int(tf/dt/10)-1,
    interval=60
)

animation.save('Solves/Heat2DTest.gif')

