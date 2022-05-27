#Librerias---
import datetime
import os

def encabezado():
    print("***************************************")
    print("UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE")
    print("        Tomas Quirumbay Morales        ")
    print("              2do - ITIN               ")
    print("    Programación Orientada a objetos   ")
    print("***************************************")
encabezado()

#Variable arreglo---
listaClientes=[]

#Clases---
class Cliente():
    def __init__(self, nombre, edad, estado):
        self.nombre=nombre
        self.edad=edad
        self.estado=estado
class Tienda():
    def __init__(self, nombre, telefono, estado, gerente):
        self.nombreT=nombre
        self.telefonoT=telefono
        self.estadoT=estado
        self.gerenteT=gerente
class  Admin():
    def __init__(self, nombre, contrasena):
        self.nombreA=nombre
        self.contrasenaA=contrasena

#Instanciar clase---
adminCuenta=Admin("Tom","2022")

#Crear funciones-----------------------------------------------------------------------------
def fechaRegistro():
    fechaActual= datetime.datetime.now().strftime("%d-%m-%Y")
    return fechaActual
fechaActual= fechaRegistro()

#Funciones---
def guardarLista(nombre, telefono, fecha, hora):
    listaClientes.append(nombre)
    listaClientes.append(telefono)
    listaClientes.append(fecha)
    listaClientes.append(hora)


#Creación de menú---
def menuPrincipal():
    os.system("cls")
    while True:
        try:
            print("***************************************")
            print("            Menú Principal             ")
            print("      Escriba 1 para registrarse       ")
            print("     Escriba 2 para iniciar sesión     ")
            print("          Escriba 3 para salir         ")
            print("***************************************")
            opcionMenu= int(input("Escoja la opción que desee: "))
            if opcionMenu==1:
                os.system("cls")
                crearCuentaUsuario()
                break
            elif opcionMenu==2:
                inicioSesion()
                break
            elif opcionMenu==3:
                os.system("cls")
                print("***************************************")
                print(" Hasta luego, esperamos vuelva pronto. ")
                print("***************************************")
                break
            else:
                os.system("cls")
                print("*************************************************************")
                print("Error, por favor ingrese solo las opciones que ve en pantalla")
                print("*************************************************************")
        #Validación de opciones del menú principal
        except ValueError:
            os.system("cls")
            print("*************************************************************")
            print("     Solo números estimad@, por favor inténtelo de nuevo     ")
            print("*************************************************************")

#Procesos---
def crearCuentaUsuario():
    print("***************************************")
    print("  Bienvenvido al registro de Usuarios  ")
    print("***************************************")
    nombre=str(input("Escriba su nombre: "))
    edad=int(input("Escriba su edad: "))
    estado=str(input("Escriba su estado actual: "))
    #Instanciar objeto---
    nuevaCuenta= Cliente(nombre,edad,estado)
    guardarLista(nuevaCuenta.nombre, nuevaCuenta.edad, nuevaCuenta.estado, fechaActual)
    print("El/La paciente ",nuevaCuenta.nombre, " tiene ", nuevaCuenta.edad, " años de edad", "y se encuentra", nuevaCuenta.estado)

#Función de logueo--- 
def inicioSesion():
    print("***************************************")
    print("   Bienvenido usuario, inicie sesión   ")
    print("***************************************")
    usuario= str(input("Escriba su nombre de usuario: "))
    contraseña= str(input("Escriba la contraseña: "))
    if usuario==adminCuenta.nombreA and contraseña==adminCuenta.contrasenaA:
        print("***************************************")
        print("Usted inició sesión, bienvenido Usuario")
        print("***************************************")
    else:
        print("********************************************")
        print("Error, vuelva a iniciar sesión correctamente")
        print("********************************************")
        inicioSesion()
menuPrincipal()
print(listaClientes)
#lista
