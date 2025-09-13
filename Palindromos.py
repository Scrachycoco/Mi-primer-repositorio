nombre = input("Ingresa un nombre: ")

def es_palindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False
        
        
if es_palindromo(nombre):
    print(f"{nombre} es palindromo")
else:
    print(f"{nombre} no es un palindromo")
    