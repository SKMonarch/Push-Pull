def suma_con_args(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

numeros = 1, 2, 3, 4, 5
resultado = suma_con_args(*numeros)
print(f"La suma es: {resultado}")
