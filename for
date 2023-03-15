#estructura
for control in range (0,10,2):
    print(control)
#listas
lista = [1,2,3, True,"unisangil",3.44]
tupla = (1,2,3,4,5)
print(lista[3])
print(lista[:])
print(lista[3:])
print(lista[:3])
print(lista[3:5])
print (len(lista))
#metodos para las listas
"""""
for control in lista:
    print(control)
    for control in tupla:
      print(control)
      lista.insert(5,"u")
    print(lista)
    """
#append
lista.append(123)
print(lista)
#pop
lista.pop()
print(lista)
#remove
lista.remove("unisangil")
print(lista)