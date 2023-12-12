import mysql.connector
import datetime

class Mensaje: 
    
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        self.conn.commit()
        self.cursor = self.conn.cursor(dictionary=True)
               #-------------------------------
                       
    def enviar_mensaje(self, nombre, apellido, telefono, email, consulta):
        sql = "INSERT INTO mensajes(nombre, apellido, telefono, email, mensaje, fecha_envio) VALUES (%s, %s, %s, %s , %s, %s)" 
        fecha_envio = datetime.datetime.now()
        valores = (nombre, apellido, telefono, email, consulta, fecha_envio)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return True
    def listar_mensajes(self):
        self.cursor.execute("SELECT * FROM mensajes")
        mensajes = self.cursor.fetchall()
        return mensajes

    #----------------------------------------------------------------
    def responder_mensaje(self, id, gestion):
        fecha_gestion = datetime.datetime.now()
        sql = "UPDATE mensajes SET leido = 1, gestion = %s, fecha_gestion = %s WHERE id = %s"
        valores = (gestion, fecha_gestion, id)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def eliminar_mensaje(self, id):
        # Eliminamos un mensaje de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM mensajes WHERE id = {id}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def mostrar_mensaje(self, id):
         sql = f"SELECT id, nombre, apellido, telefono, email, mensaje, fecha_envio, leido, gestion, fecha_gestion FROM mensajes WHERE id = {id}"
         self.cursor.execute(sql)
         return self.cursor.fetchone()
             
        

mensaje = Mensaje("localhost", "root", "", "clientes")    

#mensaje.enviar_mensaje("Jose","Chacon","0005151515","jose@jose.com", "Mensaje nuevo de prueba")