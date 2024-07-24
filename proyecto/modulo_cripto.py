def cifrar_cesar(mensaje, clave_cifrado):
    if not isinstance(mensaje, str) or not isinstance(clave_cifrado, int):
        raise ValueError("El mensaje debe ser una cadena y la clave de cifrado un entero.")

    abc = "abcdefghijklmnopqrstuvwxyz"
    clave_cifrado = clave_cifrado % len(abc)
    parte_inicial = abc[:clave_cifrado]
    parte_final = abc[clave_cifrado:]
    resultado = parte_final + parte_inicial

    cifrado = {}
    for w in range(len(abc)):
        cifrado[abc[w]] = resultado[w]

    texto_cifrado = ""
    for letra in mensaje.lower():
        if letra in cifrado:
            texto_cifrado += cifrado[letra]
        else:
            texto_cifrado += letra

    return texto_cifrado

def descifrar_cesar(mensaje, clave_cifrado):
    if not isinstance(mensaje, str) or not isinstance(clave_cifrado, int):
        raise ValueError("El mensaje debe ser una cadena y la clave de cifrado un entero.")

    abc = "abcdefghijklmnopqrstuvwxyz"
    clave_cifrado = clave_cifrado % len(abc)
    parte_inicial = abc[:clave_cifrado]
    parte_final = abc[clave_cifrado:]
    resultado = parte_final + parte_inicial

    descifrado = {}
    for w in range(len(abc)):
        descifrado[resultado[w]] = abc[w]

    texto_descifrado = ""
    for letra in mensaje.lower():
        if letra in descifrado:
            texto_descifrado += descifrado[letra]
        else:
            texto_descifrado += letra

    return texto_descifrado
