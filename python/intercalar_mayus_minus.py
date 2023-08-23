def intercalar_mayus_minus(cadena):
    resultado = ""
    mayus = True  # Empezamos con mayúscula
    
    for letra in cadena:
        if letra.isalpha():  # Solo procesamos letras
            if mayus:
                resultado += letra.upper()
            else:
                resultado += letra.lower()
            mayus = not mayus
        else:
            resultado += letra  # Mantenemos caracteres no alfabéticos
    
    return resultado

if __name__ == "__main__":
    entrada = input("Introduce una cadena: ")
    resultado = intercalar_mayus_minus(entrada)
    print("Cadena transformada:", resultado)
