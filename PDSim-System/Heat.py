
import numpy as np

# heat solver

def HeatSolver(dt, dy, t_max, y_max, k, initial_data):
   s = k*dt/dy**2
   y = np.arange(0, y_max+dy, dy)
   t = np.arange(0, t_max+dt, dt)
   r = len(t)
   c = len(y)
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

   return y, T, r, s


dt = 1
dy = 1
k = 0.4
y_max = 100
t_max = 20
T0 = 0

y, T, r, s = HeatSolver(dt, dy, t_max, y_max, k, T0)

print(r, s)
print(y)
print(T[0])
