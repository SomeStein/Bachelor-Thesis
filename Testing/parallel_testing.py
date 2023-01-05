import multiprocessing
import numpy as np
import time


if __name__ == '__main__':
    start = time.time()
    print(multiprocessing.cpu_count())
    numbers = list(np.random.randint(low = 11,size=80000000))
    
    # Create a pool of processes to use
    pool = multiprocessing.Pool()

    # Use the map() function to apply the sum_list() function to each chunk of the numbers list in parallel
    result = pool.map(sum, [numbers[i:i+10000000]for i in range(0, len(numbers), 10000000)])
    # Print the result
    print(sum(result))

    print(time.time()-start)
    
    
    
    