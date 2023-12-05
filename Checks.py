from Askint import *

def check_valid_input():
    invalid: bool = True
    while invalid:
        invalid = False
        move: str = input("Déplacer les tuiles (Z/Q/S/D) ou M pour quitter : ")
        if len(move) != 1:
            invalid =True
            print("Trop de touches")
        if not isZQSD(move):
            invalid = True
            print(f"{move} n'est pas une touche valide")
    return move