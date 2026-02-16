print("Ver saldo = 1")
print ("retiro = 2")
comanda = int(input("Ingrese lo que desee hacer: "))

if comanda == 1:
    print("Su saldo es $----")
elif comanda == 2:
    retiro = int(input("¿Cuanto desea retirar?: "))
    if retiro >= 0:
        print(f"Ha retirado $ {retiro}")
    else:
     print ("ERROR")
else:
    print ("ERROR")