import argparse

def digits_to_bin(d3: int, d2: int, d1: int) -> int:
    return (d3 << 2) | (d2 << 1) | d1 

def n_digit_of_bin(num: int, n: int) -> int: 
    return (num >> n) & 1

def get_cell(d3: int, d2: int, d1: int, rule: int) -> int:
    pattern = digits_to_bin(d3, d2, d1)
    return n_digit_of_bin(rule, pattern)


def main():
    boundary_texts = ['ignore boundary', 'treat out-of-bound cells as empty', 'wrap the boundary as a circular array']
    newline_char = '\n'
    tab_char = '\t'
    parser = argparse.ArgumentParser(
        prog='onedca',
        description='One dimensional cellular automaton.')
    parser.add_argument('-r', '--rule', dest='rule', type=int, default=122, 
                        help='the rule for the cellular automaton (default: rule 122)')
    parser.add_argument('-w', '--width', dest='width', type=int, default=31, 
                        help='the width of the board (default: 31)')
    parser.add_argument('-s', '--step', dest='step', type=int, default=15, 
                        help='number of steps or iteration (default: 15)')
    parser.add_argument('-b', '--boundary', dest='boundary', type=int, default=0, choices=[0,1,2], 
                        help=f'the boundary behavior.{newline_char} {tab_char} 0 - {boundary_texts[0]}; {newline_char}\
                            {tab_char} 1 - {boundary_texts[1]}; {newline_char}\
                            \t 2 - {boundary_texts[2]}')
    args = parser.parse_args()

    width = args.width
    # center = int(width/2) + 1
    center = int(width/2)
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
        
        # Determine the boundary cells based on indicated boundary behavior
        if boundary == 0:   # Ignore boundary
            pass            # Do nothing 
        elif boundary == 1: # Treat boundary as empty (0)
            row[0] = get_cell(0, last_row[0], last_row[1], rule)
            row[width-1] = get_cell(last_row[width-2], last_row[width-1], 0, rule)
        else: # The grid is viewed as a flatted torus
            row[0] = get_cell(last_row[-1], last_row[0], last_row[1], rule)
            row[width-1] = get_cell(last_row[width-2], last_row[width-1], last_row[0], rule)
        # Determine the cells in between 
        for j in range(1, width-1):
            row[j] = get_cell(*last_row[j-1:j+2], rule)
        
    # Visualize the matrix 
    print('Rule', rule, '   ', boundary_texts[boundary])
    for row in grid:
        for cell in row:
            symbol = '◻' if cell == 0 else '◼'
            print(symbol, end='')
        print()

if __name__ == '__main__':
    main()