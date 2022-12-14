from Walker import *
from csvExport import *
from animation import *
import json

print("\nStarting main...\n")

# Loading parameters for simulation
with open('Resources/parameters.json') as json_file:
    runs = json.load(json_file)

for run in range(len(runs)):

    parameters = runs[f"run{run}"]
    parameter_values = list(parameters.values())

    # Calculating boards
    iterated_boards = calc_iterated_boards(parameter_values)

    # Saving iterated boards as CSV
    export_as_csv(iterated_boards, parameter_values)

    # Create animation
    iterated_boards = iterated_boards/parameters["n_iter"]
    animate(iterated_boards, parameter_values)
