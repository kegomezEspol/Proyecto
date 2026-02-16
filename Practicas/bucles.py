tareas = []
max_tareas = 5
prioridades_validas = ["alta","media","baja"]

while True:
    if len(tareas) >= max_tareas:
        print("Has alcanzado el número máximo de tareas a ingresar")
    accion = input("¿Deseas agregar o ver las tareas? (agregar/ver/salir): ").lower()
    if accion == "salir":
        print("Saliendo del gestir de tareas")
        break #termina el programa porque el usuario decide salir
    elif accion=="agregar" and len(tareas)<max_tareas:
        tarea = input("Ingresa el nombre de la tarea ")
        prioridad = input("Ingresa la prioridad (alta/media/baja): ").lower()
        if prioridad not in prioridades_validas:
            print("Ingresa una prioridad valida ")
            continue
        tareas.append((tarea, prioridad))
        print(f"tarea agregada: {tarea} - prioridad : {prioridad}")
    elif accion=="ver":
        if not tareas:
            print("No hay tareas en lista")
        else: 
            print("\n ---- Tareas actuales")
            for i, (tarea,prioridad) in enumerate(tareas,1):
                print(f"{i}, {tarea} - prioridad: {prioridad}")
                print("-------\n")
    else:
        pass