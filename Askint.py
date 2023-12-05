chiffres: str = "0123456789"

def isNumeric(s: str) -> bool:
    """function that checks if a character in the string is a number"""
    global chiffres
    if s == "": return False
    for ch in s:
        if not ch in chiffres:
            return False
    return True

def get_input(message: str, maximum_include=-1) -> int:
    """function which is used for all input of the file,
    in order to not repeat itself with the isNumeric function"""
    valid: bool = False
    while not valid:
        n: str = input(message)
        valid = isNumeric(n)
        if not valid: 
            print("Entrez un NOMBRE !")
        if maximum_include != -1 and int(n) > maximum_include:
            print("too big")
            valid = False
    return int(n)

moves: str = "zqsd"

def isZQSD(s: str) -> bool:
    """function that checks if a character in the string is a z, q, s or d"""
    global moves
    if s == "": return False
    for ch in s:
        if not ch in moves:
            return False
    return True