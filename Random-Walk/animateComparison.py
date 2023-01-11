import pandas as pd
import numpy as np 
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt

#Daten einlesen
dataframe1 = pd.read_csv('Resources/Data/100_Agenten_ohne_SERW2DwithoutSE.csv')
dataframe2 = pd.read_csv('Resources/Data/100_Agenten_mit_SERW2DwithSE.csv')

#Zeilen und Spaltennummern abspalten
boards1 = np.array(dataframe1)[1:,1:]
boards2 = np.array(dataframe2)[1:,1:]
(y,x) = boards1.shape

#letztes fehlerhftes board vergessen
boards1 = boards1[:-x+1,]
boards2 = boards2[:-x+1,]

#in 3D array umwandeln (step, x, y)
boards1 = boards1.reshape((int(y/x),x,x))
boards2 = boards2.reshape((int(y/x),x,x))

def update(i):
   ax1.clear()
   ax2.clear()
   
   ax1.matshow(boards1[i,:,:],vmax = 3)
   ax1.set_title("ohne SE")
   ax2.matshow(boards2[i,:,:], vmax = 3)
   ax2.set_title("mit SE")
   
fig, (ax1,ax2) = plt.subplots(1,2,figsize = (10,5))
fig.suptitle("Vergleich Random Walk mit 100 Agenten")
animation = FuncAnimation(
        fig=fig,
        func=update,
        frames=int(y/x)
    )

animation.save("Resources/Solves/test.gif",PillowWriter(fps = 24))

print("finished!")
