def valInt(*args):
    if len(args) == 1:
        if not isinstance(args[0], int):
            return False
    elif len(args) == 2:
        if not isinstance(args[0], int):
            return False
        if not isinstance(args[1], (list, tuple)) or len(args[1]) != 2:
            raise TypeError("el segundo argumento no cumple el requisito")
        if args[1][0] >= args[1][1]:
            raise ValueError("los valores de segundo argumento no están en forma creciente")
        if isinstance(args[1], list) and not (args[1][0] <= args[0] <= args[1][1]):
            return False
        if isinstance(args[1], tuple) and not (args[1][0] < args[0] < args[1][1]):
            return False
    elif len(args)>2:
            return False
    return True

def valFloat(*args):
    if len(args) == 1:
        if not isinstance(args[0], float):
            return False
    elif len(args) == 2:
        if not isinstance(args[0], float):
            return False
        if not isinstance(args[1], (list, tuple)) or len(args[1]) != 2:
            raise TypeError("el segundo argumento no cumple el requisito")
        if args[1][0] >= args[1][1]:
            raise ValueError("los valores de segundo argumento no están en forma creciente")
        if isinstance(args[1], list) and not (args[1][0] <= args[0] <= args[1][1]):
            return False
        if isinstance(args[1], tuple) and not (args[1][0] < args[0] < args[1][1]):
            return False
    elif len(args)>2:
            return False
    return True

def valComplex(*args):
    if len(args) == 1:
        if not isinstance(args[0], complex):
            return False
    elif len(args) == 2:
        if not isinstance(args[0], complex):
            return False
        if not isinstance(args[1], (list, tuple)) or len(args[1]) != 2:
            raise TypeError("el segundo argumento no cumple el requisito")
        modulo = abs(args[0])
        if args[1][0] >= args[1][1]:
            raise ValueError("los valores de segundo argumento no están en forma creciente")
        if isinstance(args[1], list) and not (args[1][0] <= modulo <= args[1][1]):
            return False
        if isinstance(args[1], tuple) and not (args[1][0] < modulo < args[1][1]):
            return False
    elif len(args)>2:
            return False
    return True

def valList(*args):
    if len(args) == 1:
        if not isinstance(args[0], list):
            return False
    elif len(args)==2 or len(args)>3:
        return False    
    elif len(args) == 3:
        if not isinstance(args[0], list):
            return False
        if args[2]!="values" and args[2]!="len":
            raise ValueError("El tercer argumento debe ser 'len' o 'values'")
        if args[2] == 'values' and args[0]!=args[1]:
            if not isinstance(args[1], list):
                raise TypeError("El segundo argumento debe ser una lista")
            return False
        if args[2] == 'len' and len(args[0]) != args[1]:
            if not isinstance(args[1], int):
                raise TypeError("El segundo argumento debe ser un entero cuando el tercer argumento es 'len'")
            return False   
    return True
