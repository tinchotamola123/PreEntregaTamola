#Importamos el paquete_1 con la clase cliente.
#---------------------------------------------
from paquete_1.cliente import *
from paquete_1.primer_pre_entrega import *

#Instancia de la clase cliente.
cliente1=Cliente("Martin","Tamola",27,15721310)

#Print de la clase Cliente.
print(cliente1)

#Llamamos los metodos de la clase.
cliente1.imprimir()
cliente1.iniciar_sesion()
cliente1.cerrar_session()
cliente1.comprar()

menu()