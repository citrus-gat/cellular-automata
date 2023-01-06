import argparse
# import numpy as np
# import matplotlib.pyplot as plt

def digits_to_bin(d3: int, d2: int, d1: int) -> int:
    return (d3 << 2) | (d2 << 1) | d1 

def n_digit_of_bin(num: int, n: int) -> int: 
    return (num >> n) & 1


def main():
    parser = argparse.ArgumentParser(
        prog='onedca',
        description='One dimensional cellular automaton.')
    parser.add_argument('-r', '--rule', dest='rule', type=int, default=122, 
                        help='the rule for the cellular automaton.')
    parser.add_argument('-w', '--width', dest='width', type=int, default=15,
                        help='the width of the board (default: 15)')
    parser.add_argument('-s', '--step', dest='step', type=int, default=15, 
                        help='number of steps or iteration (default: 15)')
    parser.add_argument('-b', '--boundary', dest='boundary', type=int, default=0, choices=[0,1,2], 
                        help='the boundary behavior.\n\
                            \t 0 - ignore boundary; \n\
                            \t 1 - treat out-of-bound cells as empty; \n\
                            \t 2 - wrap the boundary as a circular array')
    args = parser.parse_args()

    width = args.width
    center = int(width/2) + 1
    step = args.step
    rule = args.rule
    boundary = args.boundary

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