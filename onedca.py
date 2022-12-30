# import numpy as np
# import matplotlib.pyplot as plt

def digits_to_bin(d3: int, d2: int, d1: int) -> int:
    return (d3 << 2) | (d2 << 1) | d1 

def n_digit_of_bin(num: int, n: int) -> int: 
    return (num >> n) & 1


def main():
    width = 15
    center = int(width/2) + 1
    step = 15
    rule = 122

    initial_pattern = [0]*width 
    initial_pattern[center] = 1
    # initialize grid 
    grid = [ [0]*width for _ in range(step)]
    grid[0] = list(initial_pattern)

    for i in range(1, step):   
        row = grid[i]     
        last_row = grid[i-1]
        # The grid is viewed as a flatted torus
        # Determine the left most cell 
        pattern = digits_to_bin(last_row[-1], last_row[0], last_row[1])
        row[0] = n_digit_of_bin(rule, pattern)
        # Determine the right most cell 
        pattern = digits_to_bin(last_row[width-2], last_row[width-1], last_row[0])
        row[width-1] = n_digit_of_bin(rule, pattern)
        # Determine the cells in between 
        for j in range(1, width-1):
            pattern = digits_to_bin(*last_row[j-1:j+2])
            row[j] = n_digit_of_bin(rule, pattern)
        
    # Visualize the matrix 
    for row in grid:
        for cell in row:
            symbol = '□' if cell == 0 else '■'
            print(symbol, end='')
        print()

if __name__ == '__main__':
    main()