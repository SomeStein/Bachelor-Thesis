from RW import RandomWalkGrid
from Animation import generate_animation

model = RandomWalkGrid(30, 1, [(i,0) for i in range(10,20)])

print(model)
for k in range(2):
   print(model.update(True,True,0.5))