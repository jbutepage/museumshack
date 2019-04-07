import numpy as np
import matplotlib.pyplot as plt
# 0 nothing
# 1 red
# 2 blue
# 3 green


def build_maze():
    maze = np.zeros((6,11))
    maze[0,3]  = 1
    maze[0,9] = 2
    maze[1,0] = 2
    maze[1,1] = 3
    maze[1,2] = 2
    maze[1,3] = 3
    maze[1,4] = 1
    maze[1,5] = 3
    maze[1,6] = 3
    maze[1,7] = 3
    maze[1,9] = 3
    maze[2,1] = 1
    maze[2,3] = 3
    maze[2,7] = 1
    maze[3,1] = 3
    maze[3,3] = 3
    maze[3,4] = 2
    maze[3,5] = 3
    maze[3,6] = 1
    maze[3,7:10] = 3
    maze[3,10] = 1
    maze[4,1] = 2
    maze[4,9] = 2
    maze[5,0] = 1
    maze[5,1:6] = 3
    maze[5,6] = 2
    maze[5,7:] = 3
    maze2 = np.zeros((8,13))
    maze2[0,:] = 3
    maze2[-1,:] = 3
    maze2[:,0] = 3
    maze2[:,-1] = 3
    maze2[1:-1,1:-1] = maze
    
    
    return maze2
    

maze = build_maze()
plt.imshow(maze)