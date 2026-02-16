import datetime

with open("log.txt", "a") as file:
    ahora = datetime.datetime.now()
    file.write(f"{ahora.strftime('%Y - %m - %d %H:%M:%S')} - Programa ejecutado correctamente \n")

