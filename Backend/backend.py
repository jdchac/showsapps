import mysql.connector
import datetime
import random
mensajes = []

def enviar_mensaje(nombre, apellido, telefono, email, consulta):
    mensaje = {}
    mensaje["id"] = random.randint(1000,9999)
    mensaje["nombre"] = nombre
    mensaje["apellido"] = apellido
    mensaje["telefono"] = telefono
    mensaje["email"] = email
    mensaje["mensaje"] = consulta
    mensaje["fecha_envio"] = "2023-12-06 11:02PM"
    mensajes.append(mensaje)

enviar_mensaje("Juan","Perez","123456789","juan@juan.com","Mensaje de Prueba")


def leer_mensajes():
    #Consultar a la base de datos todos los mensajes
    for mensaje in mensajes:
        print(mensajes)
        print("-"*10)

leer_mensajes()

def responder_mensaje(id, gestion):
    for mensaje in mensajes:
        if mensaje["id"] == int(id):
            mensaje["leido"] = 1
            mensaje["gestion"] = gestion
            mensaje["fecha_gestion"] = "2023-12-06"
            break

#id = input("Ingrese el ID:")
#gestion = input("Gestion: ")

#responder_mensaje(id, gestion)

def eliminar_mensaje(id):
    for x in range(0,len(mensajes)):
        if mensajes[x]["id"] == int(id):
            mensajes.pop(x)
            break

id_borrar = input("Que mensaje desea eliminar?: ")
eliminar_mensaje(id_borrar)
leer_mensajes()