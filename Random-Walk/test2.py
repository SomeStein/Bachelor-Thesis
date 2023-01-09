
import numpy
board_size = 100
added_frames = numpy.loadtxt(open("Resources/Data/parallelRW1Dtest.csv", "rb"), delimiter=",", skiprows=1,usecols = list(range(1,board_size)))