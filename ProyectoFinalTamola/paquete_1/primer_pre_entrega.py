import os

#---------------------------
#--------------------------

ruta="E:\Curso Python\Coder Python\PrimerPreEntrega\paquete_1"

#Funicion Registrar Usuario
def registrar_usuario(user,passw):
    base_dato={}
    base_dato.update({user:passw})
    with open("paquete_1/mydatabase.txt","a") as mydatabase:
        for user , passw in base_dato.items():
            mydatabase.write(f"{user}"+":"+f"{passw}\n")

#---------------------------
#---------------------------

#Funcion Leer Base de Datos
def leer_base():
    with open("paquete_1/mydatabase.txt","r") as mydatabase:
        base_dato=mydatabase.read().strip("\n")
        print(base_dato)
        return base_dato

#---------------------------   
#---------------------------    

#Funcion Loguear Usuario    
def loguear_usuario():
    lista_usuarios=[]
    lista_password=[]
    with open('paquete_1/mydatabase.txt', 'r') as mydatabase:  
        
        data=mydatabase.readlines()
        for linea in data:
            lista_usuarios.append(linea.strip("\n").split(":")[0])
            lista_password.append(linea.strip("\n").split(":")[1])
            
        #print("-----")
        #print(lista_usuarios)
        #print(lista_password)


        correcto=False
        while correcto==False:
            nombre=input("Ingrese nombre de usuario: ")
            if nombre in lista_usuarios:
                print("Usuario existe")
                correcto=True
            else:
                print ("Usuario no existe")
                #break
            while correcto==True:
                contrasenia=input("Ingrese su Password: ")
                if contrasenia in lista_password:
                    print("Usuario y contraseñas correctas")
                    print(f"Bienvenido {nombre}")
                    break
                else:
                    print("Contraseña incorrecta")
                    
#---------------------------
#---------------------------

#Funcion Menu Inicio
def menu():
    #os.system("cls")
    print ("Selecciona una opción")
    print ("\t1 - Registrar Usuario")
    print ("\t2 - Loguear Usuario")
    print ("\t3 - Leer Base de Datos")
    print ("\t0 - salir")

#---------------------------
#---------------------------

while True:
    menu()

    opcionMenu = input("Inserte el número de la opción deseada ==> ")

    if opcionMenu=="1":
        usuario=input("Ingrese el Usuario: ")
        contrasenia=input("Ingrese la contraseña: ")
        registrar_usuario(usuario,contrasenia)
        
    elif opcionMenu=="2":
        loguear_usuario()
    elif opcionMenu=="3":
        leer_base()
        
    elif opcionMenu=="0":
        break
    else:
        print("----------------")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")