def suma_con_kwargs(**kwargs):
    resultado = 0
    for key, value in kwargs.items():
        resultado += value
    return resultado

valores = {"num1": 10, "num2": 20, "num3": 30}
resultado = suma_con_kwargs(**valores)
print(f"La suma es: {resultado}")
