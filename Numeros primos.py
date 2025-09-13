def es_primo(n):
    if n < 2:  # 0 y 1 no son primos
        return False
    for i in range(2, int(n**0.5) + 1):  # solo probamos hasta la raíz cuadrada
        if n % i == 0:
            return False
    return True


# Ahora probamos del 1 al 100
for i in range(1, 101):
    if es_primo(i):
        print(f"{i} es un número primo")
    else:
        print(f"{i} no es un número primo")