import numpy as np
from numba import njit

@njit
#this algorithm is for making of the maps. 

def main(size):
    map = np.random.choice(np.array([True, False]), (size, size))
    map[0,:], map[size-1,:], map[:,0], map[:,size-1] = (True, True, True, True)