import numpy as np
import matplotlib.pyplot as plt

dt = 0.0005
dy = 0.0005
k = 10**(-4)
y_max = 0.1
t_max = 10
T0 = 1000


def FTCS(dt, dy, t_max, y_max, k, T0):
    s = k*dt/dy**2
    y = np.arange(0, y_max+dy, dy)
    t = np.arange(0, t_max+dt, dt)
    r = len(t)
    c = len(y)
    T = np.zeros([r, c])
    T[0,int(c/2)] = T0; 
    for n in range(0, r-1):
        j = 0
        T[n+1, j] = T[n,j] + s*(T[n,-1] - 2*T[n,j] + T[n,-1])
        for j in range(1, c-1):
            T[n+1,j] = T[n,j] + s*(T[n,j-1] - 2*T[n,j] + T[n,j+1])  # as before
        j = c-1 
        T[n+1, j] = T[n,j] + s*(T[n,j-1] - 2*T[n,j] + T[n,j-1])  # note the last term her

    return y,T,r,s

y,T,r,s = FTCS(dt,dy,t_max,y_max,k,T0)

plot_times = np.arange(0.01,t_max,t_max/100)
for t in plot_times:
    plt.plot(y,T[int(t/dt),:])

plt.show()