import Walker
import json

print("\nStarting main...\n")

# Loading parameters for simulation
with open('Resources/parameters.json') as json_file:
    parameters = json.load(json_file)
parameter_values = list(parameters.values())


# Calculating boards
iterated_boards = Walker.calc_iterated_boards(parameter_values)


# Saving iterated boards as CSV
#Walker.export_as_csv(iterated_boards, parameter_values)


# Create animation
Walker.animate(iterated_boards, parameter_values)
