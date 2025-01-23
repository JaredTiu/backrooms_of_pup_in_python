import numpy as np
from numba import njit

@njit
#this algorithm is for making of the maps. 

def main(size):
    map = np.random.choice(np.array([True, False]), (size, size))
    map[0,:], map[size-1,:], map[:,0], map[:,size-1] = (True, True, True, True)

    x_pos = 1.5
    y_pos = 1.5
    rotation = np.pi/4
    x = int(x_pos)
    y = int(y_pos)
    
    map[x][y] = 0

    count = 0 
    while True: 
        x_test = x
        y_test = y
        if np.random.choice(np.array([True, False])):
            x_test += np.random.choice(np.array([-1, 1]))
        else: 
            y_test += np.random.choice(np.array([-1, 1]))

        if (x_test > 0) and (x_test < size-1) and (y_test > 0 ) and (y_test < size-1):
            if map[x_test][y_test] == 0 or count > 5:
                count = 0
                x = (x_test)
                y = (y_test)
                map[x][y] = 0
                if x == size-2:
                    x_exit = x
                    y_exit = y
                    break
            else: 
                count += 1