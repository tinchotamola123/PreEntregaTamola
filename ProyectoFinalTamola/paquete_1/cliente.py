#Clase cliente
#------------

class Cliente:
    
    #Atributos de la clase
    #---------------------
    
    def __init__(self,nombre,apellido,edad,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
    
    #Metodos de la clase
    #-------------------
    
    def __str__(self):
        texto="-Nombre:{0} \n-Apellido:{1} \n-Tel:{2}"
        return texto.format(self.nombre, self.apellido, self.telefono)

    def imprimir(self):
        print(f"Cliente:\n Nombre {self.nombre} {self.apellido} \n Edad: {self.edad} \n Telefono: {self.telefono}")
    
    def iniciar_sesion(self):
        texto=f"Hola Bienvenido {self.nombre} {self.apellido}."
        return print(texto)

    def cerrar_session(self):
        texto=f"Buena suerte {self.nombre} {self.apellido}, lo esperamos pronto."
        return print(texto)
    
    def comprar(self):
        print(f"{self.nombre} estas comprando!!!!")