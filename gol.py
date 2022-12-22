import numpy as np
import matplotlib.pyplot as plt

def main():

    def initialize_grid(indices=[]):
        for (x, y) in indices:
            assert x >= 0 and x < len(grid[0]), print('x =', x)
            assert y >= 0 and y < len(grid), print('y =', y)
            grid[x][y] = 1

    def grid_at(x, y):
        return grid[x][y] if (x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)) else 0 

    def neighbor_count(x, y):
        # Count the number of living neighbors for a given index
        # x, y = idx 
        neighbors = [(x+i, y+j) for i in range(-1, 2) for j in range(-1, 2)]
        count = 0
        for i, j in neighbors:
            if i >= 0 and i < len(grid[0]) and j >= 0 and j < len(grid):
                count += grid[i][j]
        return count - grid[x][y]


    def is_become_live(x, y):
        # Come to live if it has exactly 3 living neighbors
        return neighbor_count(x, y) == 3
    
    def is_stay_live(x, y):
        # Stay live if it has 2 or 3 living neighbors
        nb_count = neighbor_count(x, y)
        return nb_count == 2 or nb_count == 3
    
    n = 9
    iteration = 15
    # n_wrap = n+2
    grid = [[0]*n for i in range(n)]
    init_pattern = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,4)]
    # init_pattern = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,3)]
    # init_pattern = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,3)]
    # init_pattern = [(2,1),(2,2),(2,3)]
    # init_pattern = [(2,0),(2,1),(2,2),(2,3),(2,4)]
    initialize_grid(init_pattern)
    lives = list(init_pattern)
    plt.matshow(grid)
    # plt.colorbar()
    # plt.show()
    plt.pause(1)
    plt.close()

    # print([1]+[2])

    # for x, y in [(5,5)]:
    #     print(grid_at(x,y,grid))

    for _ in range(iteration): 
        grid_next = [grid[i][:] for i in range(len(grid))]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[x][y] == 0 and is_become_live(x,y):
                    grid_next[x][y] = 1
                if grid[x][y] == 1 and not is_stay_live(x, y):
                    grid_next[x][y] = 0
        grid = grid_next

        plt.matshow(grid)
        # plt.colorbar()
        plt.pause(1)
        plt.close()
        # plt.show()
        
    # return 

if __name__ == '__main__':
    main()