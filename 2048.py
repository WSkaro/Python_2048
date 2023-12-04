from typing import List
from Askint import *
import random
import os
 
def Launch_2048():
    grid_size: int = get_input("Choisissez une taille de grille: ")
    grid_2048: List[List[int]] = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    
    tiles_probs: list[int] = random_tiles()
        
        
    show_grid(grid_2048)    
    
    #add_tiles(grid_2048)
    
    print(list_empty_tiles(grid_2048))
    print(tiles_probs)
    print(grid_2048)


def show_grid(grid_2048):
    os.system("cls" if os.name == "nt" else "clear")
    n = len(grid_2048)
    for i in range(n):
        print("♥" + "-" * (6*n-1) + "♥")
        print("|", end="")
        for j in range(n):
            if grid_2048[i][j] == 0:
                print(f"{'':^5}|", end="")
            else:
                print(f"{grid_2048[i][j]:^5}|", end="")
        print()
    print("♥" + "-" * (6*n-1)+ "♥")
    print()


def random_tiles():
    tiles_probs: list[int] = []
    prob_2: float = 9 #/10
    prob_4: float = 1 #/10
    
    for _ in range(prob_2):
        tiles_probs.append(2)
    for _ in range(prob_4):
        tiles_probs.append(4)
    return random.choice(tiles_probs)
    

def list_empty_tiles(grid_2048):
    for i in range(len(grid_2048)):
        for j in range(len(grid_2048[i])):
            if grid_2048[i][j] == 0:
                empty_tiles: list[tuple[int, int]] = grid_2048[i][j]                #CA renvoie des INT ta mère uwu
    return empty_tiles


def add_tiles(grid_2048):
    i, j = random.choice(list_empty_tiles(grid_2048))
    grid_2048[i][j] = random_tiles()
    return grid_2048
                

Launch_2048()