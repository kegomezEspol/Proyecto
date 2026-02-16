with open ("poema.txt","r") as file:
    for linea in file:
        print(linea)

with open ("poema.txt","r") as file:
    contenido = file.read()
    print(contenido)


