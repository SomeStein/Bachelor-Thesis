import numpy as np

initial_data = np.array([(i+25,j+25)  for i in range(-25,25) for j in range(-25,25) if ((i^2+j^2) < 70 and (i^2+j^2) > 30)]*2)
print(initial_data)