import numpy as np

class HeatSolver: #Model to solve 1D and 2D Heatequation 
   
   def __init__(self, width=1, height=1):
      self.width = width
      self.height = height
      
      
"""
model2 = HeatSolver(10, 10)
model2.show_current_state("matplotlib")
model2.show_current_state("terminal")
model2.simulate(initial_data = Data2, n_steps = 100, path = "PDSim-System/Resources/TEST2" )

model4 = HeatSolver(10)
model4.show_current_state("matplotlib")
model4.show_current_state("terminal")
model4.simulate(initial_data = Data4, n_steps = 100, path = "PDSim-System/Resources/TEST4" )
"""
      