import time 
import numpy as np
start = time.time()
numbers = list(np.random.randint(low = 11,size=80000000))
print(sum(numbers))
print(time.time()-start)