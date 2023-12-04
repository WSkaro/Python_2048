from typing import List
from Askint import *
import random
import os
 
def Launch_2048():
    grid_size: int = get_input("Choisissez une taille de grille: ")

    grid_2048: List[List[int]] = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    
    show_grid(grid_2048)    
    
    add_tiles(grid_2048)
    add_tiles(grid_2048)

    
    print(grid_2048)


def show_grid(grid_2048):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(len(grid_2048)):
        print('')


def random_tiles():
    """
    prob_2: float = 9/10
    prob_4: float = 1/10
    """
    
    tiles_choice: int = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
    return tiles_choice


def add_tiles(grid_2048):
    empty: bool = [(i, j) for i in range(len(grid_2048)) for j in range(len(grid_2048)) if grid_2048[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
        grid_2048[i][j] = random_tiles()
    return grid_2048


Launch_2048()