#Funciones
def mensaje():
    print("Unisangil")
#Llamar funcion
mensaje()
#Parametros
def suma (a,b):
    c = (a+b)
    print(c)
#llamar
suma(3,4)

#Parametros valores de retorno
def suma_resta (a,b):
    """
    suma y resta dos valores in

    """
    d = a+b
    e = a-b
    return d,e
#Llamar
suma_resta(4,5)
resultado_suma,resultado_res = suma_resta (4,5)
print(f"el resultado de la suma es:{resultado_suma}")
print(f"el resultado de la suma es:{resultado_res}")
#Funcion
def mensaje2():
    f="Algoritmos"
    return f
#Llamar
print(mensaje2())
