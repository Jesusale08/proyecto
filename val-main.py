import proyecto.validaciones as val

valInt = val.valInt
valFloat = val.valFloat
valComplex = val.valComplex
valList = val.valList

# Ejemplos de uso:
print(valInt(4))  # True
print(valInt(4.0))  # False
print(valInt(4, (4, 10)))  # False
print(valInt(4, [3, 9]))  # True
print(valInt(4, [4, 10]))  # True
print(valInt(4, [4, 5], 3)) # False
print(valInt(4, [10, 4]))  # ValueError
#print(valInt(4, 5))  # TypeError

#Ejemplos de uso:
print(valFloat(4.0)) #True
print(valFloat(4)) #False
print(valFloat(4.4,(4.4,10))) #False
print(valFloat(4.4,(4,10))) #True
print(valFloat(4.1,[4.1,9.05])) #True
print(valFloat(4.2,[4,10])) #True
print(valFloat(4.2, [4,5], 3)) # False
#print(valFloat(4.4,[10,4])) #ValueError
#print(valFloat(4.0,5)) #TypeError

# Ejemplos de uso
print(valComplex(3+4j)) #True
print(valComplex(4.0)) #False
print(valComplex(3+4j,(5,10))) #False
print(valComplex(3+4j,[5,10])) #True
print(valComplex(3+4j,[4,10])) #True
print(valComplex(3+4j, [4, 5], 3)) # False
#print(valComplex(3+4j,[10,4])) #ValueError
#print(valComplex(3+4j,5)) #TypeError

# Ejemplos de uso:
print(valList([1, 2, 3]))  # True
print(valList([1, 2, 3], [1, 2, 3], 'values'))  # True
print(valList([1, 2, 3], [1, 2, 4], 'values'))  # False
#print(valList([1, 2, 3], 3, 'values'))  # TypeError
print(valList([1, 2, 3], 3, 'len'))  # True
print(valList([1, 2, 3], 2, 'len'))  # False
print(valList([1, 2, 3], [4, 5, 6])) # False
print(valList(4, [4, 5, 6], 3, 4, 5)) # False
#print(valList([1, 2, 3], 2.5, 'len'))  #typeError
#print(valList([1, 2, 3], [1, 2, 3], 'length'))  # ValueError

