from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
from matplotlib import cm
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

    x = np.outer(np.linspace(0,board_size,board_size), np.ones(board_size)) 
    y = x.copy().T

    # Update Function for Animation
    def update(i):
        fig.clear()
        ax = plt.axes(projection ='3d')
        ax.set_title(f'2D Random Walk {size_exclusion} SE')
        z = iterated_boards[i*anim_speed].clip(0,n_iter*n_walkers/(board_size*board_size)*100)
        ax.plot_surface(x, y, z,vmin = 0, vmax=n_iter*n_walkers/(board_size*board_size)*10, cmap=cm.coolwarm,)
        ax.set_zlim(0,n_iter*n_walkers/(board_size*board_size)*20)
        

    # Animation
    fig, ax = plt.subplots(figsize=(6, 6))
    animation = FuncAnimation(
        fig=fig,
        func=update,
        frames=int(n_steps/anim_speed)
    )

    animation.save(
        f'Resources/Solves/{name}RW2D{size_exclusion}SE.gif', PillowWriter(fps=24))

    print()
    print("Animation was saved under ",
          f'Resources/Solves/{name}RW2D{size_exclusion}SE.gif\n')
