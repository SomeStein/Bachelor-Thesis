import sys 
import os

#adding solver paths
sys.path.append(os.path.abspath("PDSim-System/solvers/RandomWalkSolver"))
sys.path.append(os.path.abspath("PDSim-System/solvers/HeatEquationSolver"))

from board import Board

board = Board((100,20),True, "von neumann", True)

# board.calculate(1000, 10000, 100)

# board.render(vm = 3, simspeed = 24, size = (10,10))

# board.save 

