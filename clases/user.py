class User :

    def __init__(self , name , email  ) : # Constructor de la clase User
        self.name = name
        self.email = email

    # metodo getter para obtener el nombre del usuario
    def get_name(self) :
        return self.name
    
    def get_email(self) :
        return self.email
    
    # metodo setter para establecer el nombre del usuario
    def set_name(self , name ) :
        self.name = name

    def set_email(self , email ) :
        self.email = email
    
    #metodo para mostrar la informacion del usuario
    def showInfo(self) :
        print(f"Nombre: {self.name} , Email: {self.email}")
        