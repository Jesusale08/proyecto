import proyecto.modulo_cripto as cripto

codificar = cripto.cifrar_cesar
decodificar = cripto.descifrar_cesar

while True:
    clave_cifrado = int(input("Ingrese un número para la clave de cifrado: "))
    opcion = input("¿Desea cifrar o descifrar el mensaje? (cifrar/descifrar): ").strip().lower()
    mensaje = input("Ingrese el mensaje: ")

    if opcion == "cifrar":
        resultado = codificar(mensaje, clave_cifrado)
        print("Mensaje cifrado: ", resultado)
    elif opcion == "descifrar":
        resultado = decodificar(mensaje, clave_cifrado)
        print("Mensaje descifrado: ", resultado)
    else:
        print("Opción no válida.")

    continuar = input("¿Desea continuar? (sí/no): ").strip().lower()
    if continuar != "sí":
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
