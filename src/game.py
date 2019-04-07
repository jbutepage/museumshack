import numpy as np
import matplotlib.pyplot as plt
from states_helper import build_maze_2, build_maze

# maze = build_maze()

maze = build_maze_2()
plt.imshow(maze)
plt.show()

states = {}