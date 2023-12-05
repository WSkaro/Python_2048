from typing import List
from Checks import *
from Askint import *
import random
import os
 
def Launch_2048():
    #main()
    
    grid_size: int = get_input("Choisissez une taille de grille: ")
    grid_2048: List[List[int]] = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    
    empty_tiles: list[tuple[int, int]] = list_empty_and_busy_tiles(grid_2048)
    busy_tiles: list[tuple[int, int]] = []
    
    add_tiles(grid_2048, empty_tiles, busy_tiles)
    add_tiles(grid_2048, empty_tiles, busy_tiles)
    
    show_grid(grid_2048)
    
    print(empty_tiles)
    print(busy_tiles)
    print(grid_2048)
    
    
    run: bool = True
    while run:
        movement(grid_2048, empty_tiles, busy_tiles)

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


def list_empty_and_busy_tiles(grid_2048):
    empty_tiles: list[tuple[int, int]] = []
    for i in range(len(grid_2048)):
        for j in range(len(grid_2048[i])):
            if grid_2048[i][j] == 0:
                empty_tiles.append((i, j))
    return empty_tiles


def add_tiles(grid_2048, empty_tiles, busy_tiles):
    position = random.choice(empty_tiles)
    pos0 = position[0]
    pos1 = position[1]
    busy_tiles.append(position)
    empty_tiles.remove(position)
    
    grid_2048[pos0][pos1] = random_tiles()
    return busy_tiles


def movement(grid_2048, empty_tiles, busy_tiles):
    move = input("Déplacer les tuiles (Z/Q/S/D) ou M pour quitter : ").lower()
    
    if move == "m":
        print("Merci d'avoir joué et à bientôt !")
        exit()
    
    if move == "z":
        for j in range(len(grid_2048[0])):
            for i in range(1, len(grid_2048)):
                if grid_2048[i][j] != 0:
                    for k in range(i, 0, -1):
                        if grid_2048[k - 1][j] == 0:
                            grid_2048[k - 1][j] = grid_2048[k][j]
                            grid_2048[k][j] = 0
                            # Mettre à jour les listes des cases vides et occupées
                            if (k - 1, j) in empty_tiles:
                                print(f"empty & busy avant modif {empty_tiles} ; {busy_tiles}")
                                empty_tiles.remove((k - 1, j))
                                print(f"empty après remove {empty_tiles}")
                                busy_tiles.append((k - 1, j))
                                print(f"busy après append {busy_tiles}")
                            if (k, j) in busy_tiles:
                                busy_tiles.remove((k, j))
                                empty_tiles.append((k, j))
                        elif grid_2048[k - 1][j] == grid_2048[k][j]:
                            grid_2048[k - 1][j] *= 2
                            grid_2048[k][j] = 0
                            # Mettre à jour les listes des cases vides et occupées
                            if (k - 1, j) in busy_tiles:
                                print(f"empty & busy avant modif {empty_tiles} ; {busy_tiles}")
                                busy_tiles.remove((k - 1, j))
                                print(f"busy après remove {busy_tiles}")
                                empty_tiles.append((k - 1, j))
                                print(f"empty après append {empty_tiles}")
                            if (k, j) in busy_tiles:
                                busy_tiles.remove((k, j))
                                empty_tiles.append((k, j))


    if move == "q":
        for i in range(len(grid_2048)):
            for j in range(1, len(grid_2048[i])):
                if grid_2048[i][j] != 0:
                    for k in range(j, 0, -1):
                        if grid_2048[i][k - 1] == 0:
                            grid_2048[i][k - 1] = grid_2048[i][k]
                            grid_2048[i][k] = 0
                        elif grid_2048[i][k - 1] == grid_2048[i][k]:
                            grid_2048[i][k - 1] *= 2
                            grid_2048[i][k] = 0
                            # Mettre à jour les listes des cases vides et occupées
                            """if (k - 1, j) in empty_tiles:
                                empty_tiles.remove((k - 1, j))
                                busy_tiles.append((k - 1, j))
                            if (k, j) in busy_tiles:
                                busy_tiles.remove((k, j))
                                empty_tiles.append((k, j))"""
                        elif grid_2048[k - 1][j] == grid_2048[k][j]:
                            grid_2048[k - 1][j] *= 2
                            grid_2048[k][j] = 0
                            # Mettre à jour les listes des cases vides et occupées
                            """if (k - 1, j) in busy_tiles:
                                busy_tiles.remove((k - 1, j))
                                empty_tiles.append((k - 1, j))
                            if (k, j) in busy_tiles:
                                busy_tiles.remove((k, j))
                                empty_tiles.append((k, j))"""
                            break
                        else:
                            break

    if move == "s":
        for j in range(len(grid_2048[0])):
            for i in range(len(grid_2048) - 2, -1, -1):
                if grid_2048[i][j] != 0:
                    for k in range(i, len(grid_2048) - 1):
                        if grid_2048[k + 1][j] == 0:
                            grid_2048[k + 1][j] = grid_2048[k][j]
                            grid_2048[k][j] = 0
                        elif grid_2048[k + 1][j] == grid_2048[k][j]:
                            grid_2048[k + 1][j] *= 2
                            grid_2048[k][j] = 0
                            # Mettre à jour les listes des cases vides et occupées
                            """if (k - 1, j) in empty_tiles:
                                empty_tiles.remove((k - 1, j))
                                busy_tiles.append((k - 1, j))
                            if (k, j) in busy_tiles:
                                busy_tiles.remove((k, j))
                                empty_tiles.append((k, j))"""
                        elif grid_2048[k - 1][j] == grid_2048[k][j]:
                            grid_2048[k - 1][j] *= 2
                            grid_2048[k][j] = 0
                            # Mettre à jour les listes des cases vides et occupées
                            """if (k - 1, j) in busy_tiles:
                                busy_tiles.remove((k - 1, j))
                                empty_tiles.append((k - 1, j))
                            if (k, j) in busy_tiles:
                                busy_tiles.remove((k, j))
                                empty_tiles.append((k, j))"""
                            break
                        else:
                            break

    if move == "d":
        for i in range(len(grid_2048)):
            for j in range(len(grid_2048[i]) - 2, -1, -1):
                if grid_2048[i][j] != 0:
                    for k in range(j, len(grid_2048[i]) - 1):
                        if grid_2048[i][k + 1] == 0:
                            grid_2048[i][k + 1] = grid_2048[i][k]
                            grid_2048[i][k] = 0
                        elif grid_2048[i][k + 1] == grid_2048[i][k]:
                            grid_2048[i][k + 1] *= 2
                            grid_2048[i][k] = 0
                            # Mettre à jour les listes des cases vides et occupées
                            """if (k - 1, j) in empty_tiles:
                                empty_tiles.remove((k - 1, j))
                                busy_tiles.append((k - 1, j))
                            if (k, j) in busy_tiles:
                                busy_tiles.remove((k, j))
                                empty_tiles.append((k, j))"""
                        elif grid_2048[k - 1][j] == grid_2048[k][j]:
                            grid_2048[k - 1][j] *= 2
                            grid_2048[k][j] = 0
                            # Mettre à jour les listes des cases vides et occupées
                            """if (k - 1, j) in busy_tiles:
                                busy_tiles.remove((k - 1, j))
                                empty_tiles.append((k - 1, j))
                            if (k, j) in busy_tiles:
                                busy_tiles.remove((k, j))
                                empty_tiles.append((k, j))"""
                            break
                        else:
                            break

    # Ajouter une nouvelle tuile et actualiser l'affichage
    add_tiles(grid_2048, empty_tiles, busy_tiles)
    show_grid(grid_2048)
    print(empty_tiles)
    print(busy_tiles) 

    
    return grid_2048
Launch_2048()


"""
def movement(grid_2048, empty_tiles, busy_tiles, all_tiles):
    move = check_valid_input()
    
    if move == "m":
        print("Merci d'avoir joué et à bientôt !")
        exit()
    
    if move == "z":
        for tiles in busy_tiles:
            print(tiles)
            print(tiles[0])
            print(tiles[1])
            print(f"devra être nouv coord{(tiles[0] + 1, tiles[1])}")
            print(grid_2048)
            
            
            while (tiles[0] + 1, tiles[1]) in all_tiles:
                print("while verif")
                next_tile_value = grid_2048[tiles[0]][tiles[1]] 
                print(f"next_tile_value est {next_tile_value}")
                grid_2048[tiles[0]][tiles[1]] = 0
                grid_2048[tiles[0] + 1][tiles[1]] = next_tile_value
                print(f"tiles[0] + 1 est {tiles[0]}")
                grid_2048[tiles[0]][tiles[1]] = next_tile_value
                print(f"grid_2048[tiles[0]][tiles[1]] est {grid_2048[tiles[0]][tiles[1]]}")
    
    if move == "q":
        pass
    
    if move == "s":
        pass
    
    if move == "d":
        pass
    
    
    return grid_2048
    """