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

# Ejemplos de uso:
#print(valInt(4))  # True
#print(valInt(4.0))  # False
#print(valInt(4, (4, 10)))  # False
#print(valInt(4, [3, 9]))  # True
#print(valInt(4, [4, 10]))  # True
#print(valInt(4, [4, 5], 3)) # False
#print(valInt(4, [10, 4]))  # ValueError
#print(valInt(4, 5))  # TypeError

#Ejemplos de uso:
#print(valFloat(4.0)) #True
#print(valFloat(4)) #False
#print(valFloat(4.4,(4.4,10))) #False
#print(valFloat(4.4,(4,10))) #True
#print(valFloat(4.1,[4.1,9.05])) #True
#print(valFloat(4.2,[4,10])) #True
#print(valFloat(4.2, [4,5], 3)) # False
#print(valFloat(4.4,[10,4])) #ValueError
#print(valFloat(4.0,5)) #TypeError

# Ejemplos de uso
#print(valComplex(3+4j)) #True
#print(valComplex(4.0)) #False
#print(valComplex(3+4j,(5,10))) #False
#print(valComplex(3+4j,[5,10])) #True
#print(valComplex(3+4j,[4,10])) #True
#print(valComplex(3+4j, [4, 5], 3)) # False
#print(valComplex(3+4j,[10,4])) #ValueError
#print(valComplex(3+4j,5)) #TypeError

# Ejemplos de uso:
#print(valList([1, 2, 3]))  # True
#print(valList([1, 2, 3], [1, 2, 3], 'values'))  # True
#print(valList([1, 2, 3], [1, 2, 4], 'values'))  # False
#print(valList([1, 2, 3], 3, 'values'))  # TypeError
#print(valList([1, 2, 3], 3, 'len'))  # True
#print(valList([1, 2, 3], 2, 'len'))  # False
#print(valList([1, 2, 3], [4, 5, 6])) # False
#print(valList(4, [4, 5, 6], 3, 4, 5)) # False
#print(valList([1, 2, 3], 2.5, 'len'))  #typeError
#print(valList([1, 2, 3], [1, 2, 3], 'length'))  # ValueError