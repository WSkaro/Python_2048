from typing import List
from Askint import *
import random
import os
 
def Launch_2048():
    grid_size: int = get_input("Choisissez une taille de grille: ")

    grid_2048: List[List[int]] = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    
    show_grid(grid_2048)    

    

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
    return tiles_probs
    

def check_where_tiles_0(grid_2048):
    for i in range(len(grid_2048)):
        for j in range(len(grid_2048[i])):
            if grid_2048[i][j] == 0:
                return True
    return False
                

Launch_2048()