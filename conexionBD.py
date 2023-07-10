import mysql.connector
import datetime


class Data_register():
    def __init__(self):
        self.conx = mysql.connector.connect(
                host = 'db4free.net',
                port = 3306,
                username = 'msjoan02',
                password = 'KFRD_MEhAN#fj5T',
                db = 'tfg_jmartinez'
        )
        
    
    # FUNCION PARA CREAR UNA NOTA NUEVA EN LA BASE DE DATOS

    def createNote(self, title, content, user):      
        cursor = self.conx.cursor()
        
        query = "INSERT INTO notas (titulo, contenido, fecha_creacion, id_usuario) VALUES (%s, %s, NOW(), %s)"
        cursor.execute(query, (title, content, user))
        self.conx.commit()
        cursor.close()
        
    # FUNCION PARA LEER LAS NOTAS QUE HAY EN LA BASE DE DATOS FILTRANDO POR EL ID_USUARIO
    # DEVUELVE UN ARRAY DE LOS DATOS ENCONTRADOS

    def readNotes(self, userId):
        cursor = self.conx.cursor()
        query = "SELECT * FROM notas WHERE id_usuario = %s ORDER BY fecha_creacion DESC"
        cursor.execute(query, (userId,))
        registro = cursor.fetchall()
        cursor.close()
        
        return registro
    
    # FUNCION PARA CREAR UN USUARIO EN LA BASE DE DATOS CON LOS DATOS OBTENIDOS
    # DEVUELVE TRUE EN CASO DE ÉXITO EN LA OPERACIÓN Y FALSE EN CASO DE FRACASO

    def createUser(self, username, password):
        cursor = self.conx.cursor()
        query = "SELECT * FROM usuarios WHERE n_Usuario = %s"
        cursor.execute(query, (username,))
        rs = cursor.fetchone()
        if rs is None:
            query = "INSERT INTO usuarios (n_Usuario, pass) VALUES (%s, %s)"
            cursor.execute(query, (username, password))
            self.conx.commit()
            cursor.close()
            
            return True
        
        else:
            cursor.close()
            
            return False
    
    # FUNCION PARA FILTRAR LAS NOTAS DE LA BASE DE DATOS TENIENDO COMO CRITERIO EL TÍTULO OBTENIDO Y QUE SEA EL ID_USUARIO OBTENIDO DE LA APP
    # DEVUELVE UN ARRAY CON LOS RESULTADOS OBTENIDOS

    def filterNote(self, title, userId):
        cursor = self.conx.cursor()
        query = "SELECT id, titulo, fecha_creacion, ultima_modificacion FROM notas WHERE titulo LIKE %s AND id_usuario = %s"
        title = f"%{title}%"
        params = (title, userId)
        cursor.execute(query, params)
        resultados = []

        for row in cursor.fetchall():
            id_nota = str(row[0])
            titulo = row[1]
            fecha_creacion = str(row[2])
            ultima_modificacion = row[3]
            datos = [id_nota, titulo, fecha_creacion, ultima_modificacion]
            resultados.append(datos)
        cursor.close()
        return resultados
    
    # FUNCION PARA FILTRAR NOTAS DE LA BASE DE DATOS TENIENDO COMO CRITERIO EL ID DE LA NOTA QUE SE OBTIENE Y EL ID_USUARIO OBTENIDO DE LA APP
    # DEVUELVE FALSE EN CASO DE NO ENCONTRAR NADA Y EN CASO DE TENER RESULTADOS LOS DEVUELVE EN FORMA DE ARRAY

    def searchNote (self, idNota, userId):
        
        cursor = self.conx.cursor()
        query = "SELECT titulo, contenido FROM notas WHERE id = %s AND id_usuario = %s"
        params = (idNota, userId)
        cursor.execute(query, params)
        rs = cursor.fetchone()
        if rs is None:
            return False
        else:
            return rs

    # FUNCION PARA ACTUALIZAR LOS DATOS DE LA NOTA QUE SE DESEA E INTRODUCIR LA FECHA DE ÚLTIMA MODIFICACIÓN

    def updateNote (self, idNota, newTitle, newContent, userId):

        cursor = self.conx.cursor()
        query = "UPDATE notas SET titulo = %s, contenido = %s, ultima_modificacion = NOW() WHERE id = %s AND id_usuario = %s"
        params = (newTitle, newContent, idNota, userId)
        cursor.execute(query, params)
        self.conx.commit()
        

        cursor.close()
        
    # FUNCION PARA BORRAR LA NOTA QUE DESEA EL USUARIO TENIENDO EN CUENTA QUE SEA DE LA PROPIEDAD DEL USUARIO QUE HA INICIADO SESIÓN

    def deleteNote(self, tituloNota, userId):
        cursor = self.conx.cursor()

        query = "DELETE FROM notas WHERE titulo = %s AND id_usuario = %s"
        params = (tituloNota, userId)

        cursor.execute(query, params)
        self.conx.commit()

        cursor.close()
    
    # FUNCION QUE COMPRUEBA LOS DATOS DE INICIO DE SESIÓN QUE HA INTRODUCIDO EL USUARIO
    # DEVUELVE FALSE EN CASO DE NO ENCONTRAR EL USUARIO ESPECIFICADO Y DEVUELVE EL CAMPO ID DEL USUARIO QUE HA ENCONTRADO

    def logInUser(self, username, password):
        cursor = self.conx.cursor()
        query = "SELECT * FROM usuarios WHERE n_Usuario = %s AND pass = %s"
        cursor.execute(query, (username, password))
        rs = cursor.fetchone()

        if rs is None:
            cursor.close()
            
            return False
            
        else:
            cursor.close()
            
            return rs[0]

    # FUNCION PARA LEER LOS DATOS DE LA NOTA ESPECIFICADA CON EL TÍTULO Y ID DE USUARIO
    # DEVUELVE UN ARRAY CON LOS DATOS OBTENIDOS

    def selectNote(self, title, userId):

        if title is None:
            return False

        cursor = self.conx.cursor()
        query ="SELECT titulo, contenido, fecha_creacion, ultima_modificacion, usuarios.n_Usuario FROM notas JOIN usuarios ON notas.id_usuario = usuarios.id WHERE notas.titulo = %s AND notas.id_usuario = %s"
        params = (title, userId)

        cursor.execute(query, params)
        
        rs = cursor.fetchone()
        cursor.close()
        return rs
    
    # FUNCION PARA CERRAR LA CONEXIÓN CON LA BASE DE DATOS

    def closeConnection(self):
        self.conx.close()
    
    