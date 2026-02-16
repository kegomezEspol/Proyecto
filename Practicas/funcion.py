def calcular(numero1, numero2, operacion="sumar"):
    if operacion == "sumar":
        return numero1 + numero2
    elif operacion == "restar":
        return numero1 - numero2
    elif operacion == "multiplicar":
        return numero1*numero2
    elif operacion == "dividir":
        return numero1//numero2
    else:
        return "Ingresa operación valida"
    

print (calcular(10,2,"multiplicar"))
print (calcular(9,3,"dividir"))
print (calcular(10,2,"muldfsdfcf"))
print (calcular(15,8))

