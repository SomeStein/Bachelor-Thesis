import numpy as np
import time

SE = "with"
frame = np.zeros((50,50))
n = 50000000

def check1(SE,frame):
    if SE == "without" or frame[0,0] == 0:   #winner tuple(self.pos)
        return

def check2(SE,frame):   
    if frame[0,0] == 0 or SE == "without" :
        return

def check3(SE,frame):   
    if frame[0,0] == 0:
        return

def check4(SE,frame):   
    return


start1 = time.time()
for i in range(n):
    check1(SE,frame)
end1 = time.time()

start2 = time.time()
for i in range(n):
    check2(SE,frame)
end2 = time.time()

start3 = time.time()
for i in range(n):
    check3(SE,frame)
end3 = time.time()

start4 = time.time()
for i in range(n):
    check4(SE,frame)
end4 = time.time()

print("check 1 took: ", end1-start1, " seconds")
print("check 2 took: ", end2-start2, " seconds")
print("check 3 took: ", end3-start3, " seconds")
print("check 4 took: ", end4-start4, " seconds")