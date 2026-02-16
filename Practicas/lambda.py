#map
lista = [1,2,3,4]
lista_doblada = list(map(lambda x:x*2, lista))
print (lista_doblada)

#filter
lista = [1,2,3,4,5,6]
lista_pares = list(filter(lambda x:x%2==0, lista))
print(lista_pares)

#reduce
from functools import reduce
lista = [1,2,3,4]
producto = reduce(lambda x,y:x*y, lista)
print(producto)


#CALCULADORA
def calculo(operacion):
    if operacion == "multiplicar":
        return lambda x,y: x*y
    elif operacion == "dividir":
        return lambda x,y: x/y
    elif operacion == "restar":
        return lambda x,y: x-y
    elif operacion == "sumar":
        return lambda x,y: x+y
    elif operacion == "potencia":
        return lambda x,y: x**y
    else:
        return "Ingresar una opreacaion valida"
    
multiplicar = calculo("potencia")
print(multiplicar(4,5))