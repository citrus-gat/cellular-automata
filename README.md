# One Dimensional Cellular Automaton 

## Description 
According to [Wolfram|Alpha](https://www.wolframalpha.com/examples/science-and-technology/computational-sciences/cellular-automata), a cellular automaton is 
> A simple model capable of complex behavior [...], a computational system where many identical cells on a lattice update their color according to a local and constant rule of evolution. Cellular automata have been shown to exhibit diverse behaviors, including chaos and complexity. 

The program `onedca` simulates simple one-dimensional cellular automata. In the initial step, a black cell is placed in the middle of the first row. In a consecutive step, a new row is added. A cell in the new row is determined by the cell above it and the neighbor of that cell, as well as the rule number of the cellular automaton. 

For example, rule 122 generates the following pattern in 15 steps: 

◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◼◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◼◻◼◻◻◻◻◻◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◻◻◻◻◻◼◻◼◻◼◻◻◻◻◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◻◻◻◻◼◻◼◻◼◻◼◻◻◻◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◻◻◻◼◻◼◻◼◻◼◻◼◻◻◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◻◻◼◻◼◻◼◻◼◻◼◻◼◻◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◻◻◻◻◻◻\
◻◻◻◻◻◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◻◻◻◻◻\
◻◻◻◻◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◻◻◻◻\
◻◻◻◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◻◻◻\
◻◻◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◻◻\
◻◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◻\
◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻


## Usage 
Running `python3 onedca.py` outputs the cellular automaton of rule 122 on a 31 × 15 grid, as shown in the above example. 

To specify the rules, pass the program with the optional `--rule` or `-r` argument followed by an integer in range 0 - 255. 

To control width or length of the grid, use the optional argument `--width` or `-w` followed by a positive integer to specify the width, and `--step` or `-s` followed by a positive integer to specify the length of the grid (that is, the steps it generates). 

The program supports three methods to determine the boundary cells, which can be specified in the `--boundary` or `-b` argument: 

- `-b 0`: ignore the boundary cells and set them all to white  
- `-b 1`: treat the left neighbor of a left-most cell and the right neighbor of a right-most cell as a white cell
- `-b 2`: wrap around by treating the left neighbor of a left-most cell as the right-most cell, and the right neighbor of a right-most cell as the left-most cell; that is, view the row as a circular array, or gluing the left and right edges together. 

Usages and help texts can be viewed in the `--help` or `-h` argument. 

## Examples 

```python3 onedca.py -r 30 -b 2```

Rule 30     wrap the boundary as a circular array\
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◼◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◼◼◼◻◻◻◻◻◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◻◻◻◻◻◼◼◻◻◼◻◻◻◻◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◻◻◻◻◼◼◻◼◼◼◼◻◻◻◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◻◻◻◼◼◻◻◼◻◻◻◼◻◻◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◻◻◼◼◻◼◼◼◼◻◼◼◼◻◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◻◼◼◻◻◼◻◻◻◻◼◻◻◼◻◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◻◼◼◻◼◼◼◼◻◻◼◼◼◼◼◼◻◻◻◻◻◻◻◻\
◻◻◻◻◻◻◻◼◼◻◻◼◻◻◻◼◼◼◻◻◻◻◻◼◻◻◻◻◻◻◻\
◻◻◻◻◻◻◼◼◻◼◼◼◼◻◼◼◻◻◼◻◻◻◼◼◼◻◻◻◻◻◻\
◻◻◻◻◻◼◼◻◻◼◻◻◻◻◼◻◼◼◼◼◻◼◼◻◻◼◻◻◻◻◻\
◻◻◻◻◼◼◻◼◼◼◼◻◻◼◼◻◼◻◻◻◻◼◻◼◼◼◼◻◻◻◻\
◻◻◻◼◼◻◻◼◻◻◻◼◼◼◻◻◼◼◻◻◼◼◻◼◻◻◻◼◻◻◻\
◻◻◼◼◻◼◼◼◼◻◼◼◻◻◼◼◼◻◼◼◼◻◻◼◼◻◼◼◼◻◻\
◻◼◼◻◻◼◻◻◻◻◼◻◼◼◼◻◻◻◼◻◻◼◼◼◻◻◼◻◻◼◻

<br/>

```python3 onedca.py -r 121```

Rule 121     ignore boundary\
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◼◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻\
◻◼◼◼◼◼◼◼◼◼◼◼◼◼◻◻◼◼◼◼◼◼◼◼◼◼◼◼◼◼◻\
◻◼◻◻◻◻◻◻◻◻◻◻◻◼◼◻◼◻◻◻◻◻◻◻◻◻◻◻◻◼◻\
◻◻◼◼◼◼◼◼◼◼◼◼◻◼◼◼◻◼◼◼◼◼◼◼◼◼◼◼◻◻◻\
◻◻◼◻◻◻◻◻◻◻◻◼◼◼◻◼◼◼◻◻◻◻◻◻◻◻◻◼◼◼◻\
◻◻◻◼◼◼◼◼◼◼◻◼◻◼◼◼◻◼◼◼◼◼◼◼◼◼◻◼◻◼◻\
◻◼◻◼◻◻◻◻◻◼◼◻◼◼◻◼◼◼◻◻◻◻◻◻◻◼◼◻◼◻◻\
◻◻◼◻◼◼◼◼◻◼◼◼◼◼◼◼◻◼◼◼◼◼◼◼◻◼◼◼◻◼◻\
◻◻◻◼◼◻◻◼◼◼◻◻◻◻◻◼◼◼◻◻◻◻◻◼◼◼◻◼◼◻◻\
◻◼◻◼◼◼◻◼◻◼◼◼◼◼◻◼◻◼◼◼◼◼◻◼◻◼◼◼◼◼◻\
◻◻◼◼◻◼◼◻◼◼◻◻◻◼◼◻◼◼◻◻◻◼◼◻◼◼◻◻◻◼◻\
◻◻◼◼◼◼◼◼◼◼◼◼◻◼◼◼◼◼◼◼◻◼◼◼◼◼◼◼◻◻◻\
◻◻◼◻◻◻◻◻◻◻◻◼◼◼◻◻◻◻◻◼◼◼◻◻◻◻◻◼◼◼◻\
◻◻◻◼◼◼◼◼◼◼◻◼◻◼◼◼◼◼◻◼◻◼◼◼◼◼◻◼◻◼◻\
◻◼◻◼◻◻◻◻◻◼◼◻◼◼◻◻◻◼◼◻◼◼◻◻◻◼◼◻◼◻◻

<br/>

```python3 onedca.py -r 121 -b 1```

Rule 121     treat out-of-bound cells as empty\
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◼◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻\
◼◼◼◼◼◼◼◼◼◼◼◼◼◼◻◻◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼\
◼◻◻◻◻◻◻◻◻◻◻◻◻◼◼◻◼◻◻◻◻◻◻◻◻◻◻◻◻◻◼\
◻◼◼◼◼◼◼◼◼◼◼◼◻◼◼◼◻◼◼◼◼◼◼◼◼◼◼◼◼◻◻\
◻◼◻◻◻◻◻◻◻◻◻◼◼◼◻◼◼◼◻◻◻◻◻◻◻◻◻◻◼◼◼\
◻◻◼◼◼◼◼◼◼◼◻◼◻◼◼◼◻◼◼◼◼◼◼◼◼◼◼◻◼◻◼\
◼◻◼◻◻◻◻◻◻◼◼◻◼◼◻◼◼◼◻◻◻◻◻◻◻◻◼◼◻◼◻\
◻◼◻◼◼◼◼◼◻◼◼◼◼◼◼◼◻◼◼◼◼◼◼◼◼◻◼◼◼◻◼\
◻◻◼◼◻◻◻◼◼◼◻◻◻◻◻◼◼◼◻◻◻◻◻◻◼◼◼◻◼◼◻\
◼◻◼◼◼◼◻◼◻◼◼◼◼◼◻◼◻◼◼◼◼◼◼◻◼◻◼◼◼◼◼\
◻◼◼◻◻◼◼◻◼◼◻◻◻◼◼◻◼◼◻◻◻◻◼◼◻◼◼◻◻◻◼\
◻◼◼◼◻◼◼◼◼◼◼◼◻◼◼◼◼◼◼◼◼◻◼◼◼◼◼◼◼◻◻\
◻◼◻◼◼◼◻◻◻◻◻◼◼◼◻◻◻◻◻◻◼◼◼◻◻◻◻◻◼◼◼\
◻◻◼◼◻◼◼◼◼◼◻◼◻◼◼◼◼◼◼◻◼◻◼◼◼◼◼◻◼◻◼\
◼◻◼◼◼◼◻◻◻◼◼◻◼◼◻◻◻◻◼◼◻◼◼◻◻◻◼◼◻◼◻

<br/>

```python3 onedca.py -r 121 -b 2```

Rule 121     wrap the boundary as a circular array\
◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◼◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻\
◼◼◼◼◼◼◼◼◼◼◼◼◼◼◻◻◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼\
◻◻◻◻◻◻◻◻◻◻◻◻◻◼◼◻◼◻◻◻◻◻◻◻◻◻◻◻◻◻◻\
◼◼◼◼◼◼◼◼◼◼◼◼◻◼◼◼◻◼◼◼◼◼◼◼◼◼◼◼◼◼◼\
◻◻◻◻◻◻◻◻◻◻◻◼◼◼◻◼◼◼◻◻◻◻◻◻◻◻◻◻◻◻◻\
◼◼◼◼◼◼◼◼◼◼◻◼◻◼◼◼◻◼◼◼◼◼◼◼◼◼◼◼◼◼◼\
◻◻◻◻◻◻◻◻◻◼◼◻◼◼◻◼◼◼◻◻◻◻◻◻◻◻◻◻◻◻◻\
◼◼◼◼◼◼◼◼◻◼◼◼◼◼◼◼◻◼◼◼◼◼◼◼◼◼◼◼◼◼◼\
◻◻◻◻◻◻◻◼◼◼◻◻◻◻◻◼◼◼◻◻◻◻◻◻◻◻◻◻◻◻◻\
◼◼◼◼◼◼◻◼◻◼◼◼◼◼◻◼◻◼◼◼◼◼◼◼◼◼◼◼◼◼◼\
◻◻◻◻◻◼◼◻◼◼◻◻◻◼◼◻◼◼◻◻◻◻◻◻◻◻◻◻◻◻◻\
◼◼◼◼◻◼◼◼◼◼◼◼◻◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼\
◻◻◻◼◼◼◻◻◻◻◻◼◼◼◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻\
◼◼◻◼◻◼◼◼◼◼◻◼◻◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼\
◻◼◼◻◼◼◻◻◻◼◼◻◼◼◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻◻

## Thank you 
