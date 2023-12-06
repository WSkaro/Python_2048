from typing import List
from Checks import *
from Askint import *
import random
import os
 
def Launch_2048():
    #main()
    
    grid_size: int = get_input("Choisissez une taille de grille: ")
    grid_2048: List[List[int]] = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    
    grid_2048 = \
        [
            [2,2,2,2],
            [0,0,0,2],
            [0,0,0,2],
            [0,0,0,2],
        ]
    
    empty_tiles: list[list[int, int]] = list_empty_and_busy_tiles(grid_2048)
    
    add_tiles(grid_2048, empty_tiles)
    add_tiles(grid_2048, empty_tiles)
    
    show_grid(grid_2048)
    
    print(empty_tiles)
    print(grid_2048)
    
    
    run: bool = True
    while run:
        movement(grid_2048, empty_tiles)

def main():
        print("---------------------༼ つ ◕_◕ ༽つ---------------------")
        print("Bienvenue sur ce jeu du 2048 !")

        reponse = input("Souhaitez-vous consulter les règles (Y/N) ? ")
        if reponse.upper() == "Y":
            # Affichage des règles du jeu
            print("---------------------༼ つ ◕_◕ ༽つ---------------------")
            print("Règles :")
            print("- Le but du jeu est d'atteindre la tuile 2048 ou un score aussi proche que possible. - ")
            print("------> - La partie se joue sur une grille de la taille que vous choisissez.")
            print("------> - Vous déplacez les tuiles en combinant celles ayant le même numéro lorsqu'elles sont adjacentes.")
            print("------> - À chaque tour, une nouvelle tuile de 2 ou de 4 apparaît aléatoirement sur la grille.")
            print("------> - Vous pouvez déplacer toutes les tuiles vers le haut, le bas, la gauche ou la droite.")
            print("------> - Lorsque deux tuiles du même numéro entrent en collision lors d'un déplacement, elles fusionnent pour former une tuile ayant le double de la valeur.")
            print("------> - Le jeu se termine lorsque la tuile 2048 est créée ou lorsque la grille est pleine sans possibilité de combiner d'autres tuiles.")
            print("------> - Votre score est la somme des valeurs de toutes les tuiles présentes sur la grille.")
            print("------> - Réfléchissez à chaque mouvement pour combiner les tuiles et atteindre la tuile 2048 !")
            print("---------------------༼ つ ◕_◕ ༽つ---------------------")

def show_grid(grid_2048):
    #os.system("cls" if os.name == "nt" else "clear")
    print("----------༼ つ ◕_◕ ༽つ---------")
    print()
    for i in range(len(grid_2048)):
        print("♥" + "-" * (6 * len(grid_2048) - 1) + "♥")
        print("|", end="")
        for j in range(len(grid_2048)):
            if grid_2048[i][j] == 0:
                print(f"{'':^5}|", end="")
            else:
                print(f"{grid_2048[i][j]:^5}|", end="")
        print()
    print("♥" + "-" * (6 * len(grid_2048) - 1)+ "♥")
    print()
    print("----------༼ つ ◕_◕ ༽つ---------")
    print()


def random_tiles():
    return random.choices([2, 4], weights=[9, 1])[0]


def list_empty_and_busy_tiles(grid_2048) -> list[list[int, int]]:
    empty_tiles: list[list[int, int]] = []

    for i in range(len(grid_2048)):
        for j in range(len(grid_2048[i])):
            if grid_2048[i][j] == 0:
                empty_tiles.append([i, j])

    return empty_tiles


def add_empty_tile(empty_tiles: list[list[int]], i: int, j: int):
    empty_tiles.append([i, j])

def add_tiles(grid_2048, empty_tiles):
    return
    position = random.choice(empty_tiles)
    pos0 = position[0]
    pos1 = position[1]
    empty_tiles.remove(position)
    
    grid_2048[pos0][pos1] = random_tiles()


def update_empty_tile(empty_tiles: list[list[int]], i: int, j: int, new_i: int, new_j: int):
    index: int = empty_tiles.index([i, j])
    empty_tiles[index][0] = new_i
    empty_tiles[index][1] = new_j

def movement(grid_2048, empty_tiles):
    move = check_valid_input()
    
    if move == "m":
        print("Merci d'avoir joué et à bientôt !")
        exit()
    
    if move == "z":
        for i in range(len(grid_2048)):
            k_start_index = 0
            for j in range(1, len(grid_2048[i])):
                if grid_2048[j][i] == 0:
                    continue
                
                for k in range(k_start_index, j):
                    found: bool = False
                    if grid_2048[k][i] == 0:
                        k_start_index = k
                        update_empty_tile(empty_tiles, k, i, j, i)
                        found = True
                        
                    if grid_2048[k][i] == grid_2048[j][i]:
                        add_empty_tile(empty_tiles, j, i)
                        k_start_index += 1
                        found = True
                    
                    if found == False:
                        continue
                    
                    grid_2048[k][i] += grid_2048[j][i]
                    grid_2048[j][i] = 0
                    break


    if move == "q":
        for i in range(len(grid_2048)):
            k_start_index = 0
            for j in range(1, len(grid_2048)):
                if grid_2048[i][j] == 0:
                    continue
                
                for k in range(k_start_index, j):
                    found: bool = False
                    if grid_2048[i][k] == 0:
                        k_start_index = k
                        update_empty_tile(empty_tiles, i, k, i, j)
                        found = True
                        
                    if grid_2048[i][k] == grid_2048[i][j]:
                        add_empty_tile(empty_tiles, i, j)
                        k_start_index += 1
                        found = True
                    
                    if found == False:
                        continue
                    
                    grid_2048[i][k] += grid_2048[i][j]
                    grid_2048[i][j] = 0
                    break

    if move == "s":
        for i in range(len(grid_2048)):
            k_start_index = len(grid_2048) - 1
            for j in range(len(grid_2048[i])):
                if grid_2048[j][i] == 0:
                    continue
                
                for k in range(k_start_index, j, -1):
                    found: bool = False
                    if grid_2048[k][i] == 0:
                        k_start_index = k
                        update_empty_tile(empty_tiles, k, i, j, i)
                        found = True
                        
                    if grid_2048[k][i] == grid_2048[j][i]:
                        add_empty_tile(empty_tiles, j, i)
                        k_start_index -= 1
                        found = True
                    
                    if found == False:
                        continue
                    
                    grid_2048[k][i] += grid_2048[j][i]
                    grid_2048[j][i] = 0
                    break


    if move == "d":
        for i in range(len(grid_2048)):
            k_start_index = len(grid_2048[i]) - 1
            for j in range(len(grid_2048)):
                if grid_2048[i][j] == 0:
                    continue
                
                for k in range(k_start_index, j, -1):
                    found: bool = False
                    if grid_2048[i][k] == 0:
                        k_start_index = k
                        update_empty_tile(empty_tiles, i, k, i, j)
                        found = True
                        
                    if grid_2048[i][k] == grid_2048[i][j]:
                        add_empty_tile(empty_tiles, i, j)
                        k_start_index -= 1
                        found = True
                    
                    if found == False:
                        continue
                    
                    grid_2048[i][k] += grid_2048[i][j]
                    grid_2048[i][j] = 0
                    break


    add_tiles(grid_2048, empty_tiles)
    show_grid(grid_2048)
    print(empty_tiles)

    return grid_2048


Launch_2048()