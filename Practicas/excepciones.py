try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Elige una operación (+, -, *, /): ")

    if operacion == "+":
        print(f"Resultado {num1+num2}")
    elif operacion == "-":
        print(f"Resultado {num1-num2}")
    elif operacion == "*":
        print(f"Resultado {num1*num2}")
    elif operacion == "/":
        print(f"Resultado {num1/num2}")
    else:
        print("Operación no válida")
except ZeroDivisionError:
    print("Error: No se puede dividir entre 0")
except ValueError:
    print("Error: Ingresa un número válido")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    print("Fin de la operación")    