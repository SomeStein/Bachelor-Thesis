from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
import numpy as np



def animate(iterated_boards, params):

    [name,
     board_size,
     n_steps,
     n_walkers,
     n_iter,
     anim_speed,
     size_exclusion, ] = params

    print("Animating calculated frames", end="\r")

    # Update Function for Animation
    def update(i):
        fig.clear()
        ax = fig.add_subplot(111)
        ax.set_title(f'2D Random Walk {size_exclusion} SE')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        map = ax.matshow(iterated_boards[i*anim_speed], cmap='gray',
                         vmin=0, vmax=n_iter*n_walkers/(board_size*board_size)*2)
        #cb = fig.colorbar(map)

    # Animation
    fig, ax = plt.subplots(figsize=(6, 6))
    animation = FuncAnimation(
        fig=fig,
        func=update,
        frames=int(n_steps/anim_speed)
    )

    animation.save(
        f'Resources/Solves/{name}RW2D{size_exclusion}SE.gif', PillowWriter(fps=24))

    print("\nAnimation was saved under ",
          f'Resources/Solves/{name}RW2D{size_exclusion}SE.gif\n')