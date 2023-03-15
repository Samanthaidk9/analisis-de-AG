import random

lista_aleatoria = []

for i in range(19):
    lista_aleatoria.append(random.randint(0, 101))

print(lista_aleatoria)

#Elimina los repetidos
lista_f = list(set(lista_aleatoria))

#ordenar la lista
lista_aleatoria.sort(reverse=True)#descendente
print(lista_aleatoria )
#tiempo inicial


