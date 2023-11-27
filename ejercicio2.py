alumno = input("Introduce el nombre del alumno/a y si está aprobado o suspendido: ")
apr_sus = input("- ")
clase = {alumno : apr_sus}
print(clase)
añadir = input("¿Quieres añadir un alumno/a, si o no? ")
while añadir == "si":
    alumno = input("Introduce el nombre del alumno/a y si está aprobado o suspendido: ")
    apr_sus = input("- ")
    clase = {alumno : apr_sus}
    print(clase)
    añadir1 = input("¿Quieres añadir un alumno/a, si o no? ")
else:  
    añadir = input("¿Cuál es el número de aprobados? ")
    print("El número de aprobados es", añadir)
print(clase)