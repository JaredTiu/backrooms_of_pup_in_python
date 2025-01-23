import pygame
import numpy as np

#this algorithm is for making of the maps. 

def main(size):
    pygame.init()
    WIDTH, HEIGHT = 600, 400 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((20,20,20))
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
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
        
            screen.blit(background, (0, 0))

        return x_pos, y_pos, rotation, map, x_exit, y_exit