
preson = {
    "nombre": "Juan", 
    "edad": 30, 
    "correo": "juan@ejemplo.com"
}

print(preson.get("nombre", "No se encontró el nombre")) 

if "telefono" in preson:
    print("La telefono  existe en el diccionario")
else:
    print("La telefono no existe en el diccionario")

