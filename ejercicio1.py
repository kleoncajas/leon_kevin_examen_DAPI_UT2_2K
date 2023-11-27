nombres = ["Kevin León", "Mathew Cajas", "Mateo Esparza"]

#def ListaNombres(nombres):
#    for a in range(len(nombres)):
        
def OrdenarNombre(nombre_1, nombre_2, nombre_3):
    """Función que recibe un "nombre y apellido" y devuelve el "apellido, nombre".
Parámetros:
- nombres: Nombre en el formato "Nombre Apellido"
Salida:
Nombre en el formato "Apellido, Nombre"
"""
    nombre_1 = nombres[0].split(" ")
    nombre_2 = nombres[1].split(" ")
    nombre_3 = nombres[2].split(" ")
    nombre_1.reverse()
    nombre_2.reverse()
    nombre_3.reverse()
    return OrdenarNombre(nombre_1, nombre_2, nombre_3)
print(nombre_1)
print(nombre_2)
print(nombre_3)