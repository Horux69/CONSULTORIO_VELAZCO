from datetime import datetime
import os


class Medicos:
    def __init__(self, miDB):
        self.mysql = miDB
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    def consultar(self):
        sql = "SELECT * FROM medicos WHERE activo = 1"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def buscarMedico(self, id):
        consultaMedicos = f"SELECT * FROM medicos WHERE idmedico = '{id}'"
        self.cursor.execute(consultaMedicos)
        resultado = self.cursor.fetchone()
        self.conexion.commit()
        return resultado
    
    def agregar(self, medico):

        ahora = datetime.now()
        tiempo = ahora.strftime("%Y%m%d%H%M%S")
        nom, extension = os.path.splitext(medico[3].filename)
        nombreFoto = "F" + tiempo + extension
        medico[3].save("uploads/"+nombreFoto)

        sql = f"INSERT INTO medicos (idmedico, nombre, especialidad, foto, activo) VALUES ('{medico[0]}','{medico[1]}','{medico[2]}','{nombreFoto}',1)"
        self.cursor.execute(sql)
        self.conexion.commit()

    def borrar(self, id):
        consulta = f"UPDATE medicos SET activo = 0 WHERE idmedico = '{id}'"
        self.cursor.execute(consulta)
        self.conexion.commit()

