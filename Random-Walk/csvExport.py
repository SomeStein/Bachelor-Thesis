import pandas as pd
import numpy as np

def export_as_csv(iterated_boards, params):
    [name,
     board_size,
     n_steps,
     n_walkers,
     n_iter,
     anim_speed,
     size_exclusion,
     ] = params

    print("Saving Data as CSV file", end="\r")

    dataframe = pd.DataFrame(
        list(np.array(iterated_boards, dtype=int).reshape(board_size*n_steps, board_size)))
    dataframe.to_csv(f'Resources/Data/{name}RW2D{size_exclusion}SE.csv')

    print("\nData was saved under ",
          f'Resources/Data/{name}RW2D{size_exclusion}SE.csv')