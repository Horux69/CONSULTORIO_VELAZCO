import hashlib
from flask import Flask
from flaskext.mysql import MySQL

programa = Flask(__name__)
mysql = MySQL()
programa.config['MYSQL_DATABASE_HOST']='localhost'
programa.config['MYSQL_DATABASE_PORT']=3306
programa.config['MYSQL_DATABASE_USER']='root'
programa.config['MYSQL_DATABASE_PASSWORD']=''
programa.config['MYSQL_DATABASE_DB']='consultorio'
mysql.init_app(programa)

idusuario = input("Digite id: ")
nombre = input("Digite nombre: ")
contrasena = input("Digite contraseña: ")
cifrada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()

sql = f"INSERT INTO usuarios (idusuario,nombre,contrasena,activo) VALUES ('{idusuario}','{nombre}','{cifrada}',1)"
con = mysql.connect()
cur = con.cursor()
cur.execute(sql)
con.commit()

################### METODO MAS FACIL EH INTUITIVO PARA ALMACENAR DATOS EN UN BD POR HTML Y BACK PYTHON #######################

# import hashlib
# from flask import Flask, render_template, request
# from flaskext.mysql import MySQL

# programa = Flask(__name__)
# mysql = MySQL()
# programa.config['MYSQL_DATABASE_HOST'] = 'localhost'
# programa.config['MYSQL_DATABASE_PORT'] = 3306
# programa.config['MYSQL_DATABASE_USER'] = 'root'
# programa.config['MYSQL_DATABASE_PASSWORD'] = ''
# programa.config['MYSQL_DATABASE_DB'] = 'consulta'
# mysql.init_app(programa)

# conexion = mysql.connect()
# cursor = conexion.cursor()

# @programa.route('/')
# def index():
#     return render_template("formulario.html")

# @programa.route('/guardar', methods=['POST'])
# def guardar():
#     idusuario = request.form['idusuario']
#     nombre = request.form['nombre']
#     contrasena = request.form['contrasena']
#     activo = '1' if 'activo' in request.form else '0'

#     encriptada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()

#     consulta = "INSERT INTO usuarios (idusuario, nombre, contrasena, activo) VALUES (%s, %s, %s, %s)"
#     valores = (idusuario, nombre, encriptada, activo)

#     cursor.execute(consulta, valores)
#     conexion.commit()

#     return "Los datos se han guardado correctamente."

# if __name__ == '__main__':
#     programa.run(host='0.0.0.0', debug=True, port='8080')

###########################################################################################################


# import hashlib
# from flask import Flask
# from flaskext.mysql import MySQL

# programa = Flask(__name__)
# mysql = MySQL()
# programa.config['MYSQL_DATABASE_HOST'] = 'localhost'
# programa.config['MYSQL_DATABASE_PORT'] = 3306
# programa.config['MYSQL_DATABASE_USER'] = 'root'
# programa.config['MYSQL_DATABASE_PASSWORD'] = ''
# programa.config['MYSQL_DATABASE_DB'] = 'consulta'
# mysql.init_app(programa)

# conexion = mysql.connect()
# cursor = conexion.cursor()

# cursor.execute("DESCRIBE usuarios")
# campos = [campo[0] for campo in cursor.fetchall()]

# valores = {}
# for campo in campos:
#     if campo == 'activo':
#         valores[campo] = 1
#     else:
#         valor = input(f"Ingrese el valor del campo '{campo}': ")
#         valores[campo] = valor

# if 'contrasena' in valores:
#     contrasena = valores['contrasena']
#     encriptada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()
#     valores['contrasena'] = encriptada

#     consulta = f"INSERT INTO usuarios ({', '.join(campos)}) VALUES ({', '.join(['%s'] * len(campos))})"
#     valoresOrdenados = [valores[campo] for campo in campos]
#     cursor.execute(consulta, valoresOrdenados)

#     conexion.commit()

#     print("Los datos se han insertado correctamente.")

# else:
#     print("No se han insertado los datos")

# cursor.close()
# conexion.close()