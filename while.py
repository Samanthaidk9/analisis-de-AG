"""""
#variable
contador = 0

# Estructura
while contador <=4:
    if contador  == 3:
        print("unisangil")
        break
    print(f"contador = {contador}")
    contador += 1
    print("salio de while")
"""""
"""""
    #ejemplo 
    contador = 0
while contador < 20:
     contador +=1
     if contador < 15:
        continue
     print(contador)
     """

texto = "Estoy en clase de algoritmos unisangil"
#buscar
print("clases" in texto)
print(texto.title())
print(texto.upper())#mayusculas
print(texto.lower())#minusculas
print(texto.count("a"))#veces que se repite una letra