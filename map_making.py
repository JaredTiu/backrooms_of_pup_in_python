import numpy as np
from numba import njit

@njit
#this algorithm is for making of the maps. 

def main(size):
    map = np.random.choice(np.array([True, False]), (size, size))
    map[0,:], map[size-1,:], map[:,0], map[:,size-1] = (True, True, True, True)

    x_pos = 1.5
    y_pos = 1.5
    rot = np.pi/4
    x = int(x_pos)
    y = int(y_pos)
    
    map[x][y] = 0