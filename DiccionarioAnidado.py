
user = {
    "name": "John Doe",
    "direccion":{
        "Provincia":"Guanacaste",
        "Canton":"Liberia"
    }
}

for key, value in user.items():
    if isinstance(value, dict): # Verificar si el valor es un diccionario
        print(f"La clave '{key}' Contiene un diccionario de datos." )
        for subKey, subValue in value.items():
            print(f"'{subKey}': '{subValue}'")
    else:
        print(f"'{key}': '{value}'")

              
                

