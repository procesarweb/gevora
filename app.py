
from flask import Flask
from flask import render_template, request, redirect, session
from flaskext.mysql import MySQL
from requests import post

app=Flask(__name__)
#app.secret_key="gv"
#Establecemos la conexión a la base de datos
mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='gevora'
mysql.init_app(app)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')


@app.route('/libros')
def libros():
    return render_template('sitio/libros.html')


#Restricción para ingreso no autorizado, enrutado hacia la raiz
@app.route('/admin/inicio')
def admin_inicio():
    if not 'login' in session:
        return redirect("/")

#@app.route('admin/login')
#def admin_login():
 #   return render_template('admin/login.html',login=login)
 #   return redirect('admin/login.html')

#inicio CRUD libros ---  David López Ramirez
@app.route('/admin/')
def admin_libros():
    conexion=mysql.connect()
    #Traer la información de la base de datos
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    libros=cursor.fetchall()
    conexion.commit()
    return render_template('admin/libros.html', libros=libros)

@app.route('/admin/libros/guardar', methods=['POST'])
def admin_libros_guardar():
    __nombre = request.form['nombre_libro']
    __imagen = request.files['imagen_libro']
    __url = request.form['url_libro']
    #print(__nombre)
    #print(__imagen)
    #print(__url)
    #Ejecutar la sentencia de inserción de datos a la tabla
    sql="INSERT INTO libros (nombre, imagen, url) VALUES(%s, %s,%s)"
    dato=(__nombre, __imagen.filename, __url)
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql, dato)
    conexion.commit()
    return redirect('/admin/')

#editar libros
@app.route('/admin/libros/editar', methods=['POST'])
def editar():
    __id__=request.form['id']
    conexion = mysql.connect()
    cursor =conexion.cursor()
    consulta = "SELECT * FROM libros WHERE id=%s"
    cursor.execute(consulta, __id__)
    dato=cursor.fetchall()
    conexion.commit()
    return render_template('admin/editar.html', d=dato[0])


@app.route('/admin/libros/modificar', methods=['POST'])
def modificar():
    __id__ = request.form['filtro']
    __nombre__ = request.form['nombre_libro']
    __url__ = request.form['url_libro']
    conexion = mysql.connect()
    cursor =conexion.cursor()
    cursor.execute("UPDATE libros SET nombre=%s, url=%s WHERE id=%s",(__nombre__, __url__, __id__))
    conexion.commit()
    return redirect('/admin/')


@app.route('/admin/libros/eliminar', methods=['POST'])
def eliminar():
    __id__ = request.form['id']
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id=%s",(__id__))
    conexion.commit() 
    return redirect('/admin/')
# fin CRUD libros


#rutas de las habitaciones


@app.route('/habitaciones')
def habitaciones():
    return render_template('habitaciones/habitaciones.html')

@app.route('/habitaciones/')
def hab_habitaciones():
    conexion=mysql.connect()
    #Traer la información de la base de datos de Consulta - Read
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM habitaciones")
    habitaciones=cursor.fetchall()
    conexion.commit()  
    return render_template('habitaciones/habitaciones.html', habitaciones=habitaciones)

#Crear Habitaciones  - Inserción
@app.route('/habitaciones/habitaciones/guardar', methods=['POST'])
def habitaciones_guardar():
    __descriphab = request.form['descripcionhabitacion']
    __preciohab = request.form['preciohabitacion']
    __estadohab = request.form['estadohabitacion']
       #Ejecutar la sentencia de inserción de datos a la tabla
    sql="INSERT INTO habitaciones (descriphab, preciohab, estadohab) VALUES (%s, %s, %s)" #preciohab, estadohab
    datos=(__descriphab, __preciohab, __estadohab)
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect('/habitaciones/')

#Editar habitaciones a partir del cod/id
@app.route('/habitaciones/habitaciones/editarh', methods=['POST'])
def editarh():
    __codhab__=request.form['id']
    conexion = mysql.connect()
    cursor =conexion.cursor()
    consulta = "SELECT * FROM habitaciones WHERE codhab=%s"
    cursor.execute(consulta, __codhab__)
    datos=cursor.fetchall()
    conexion.commit()
    return render_template('/habitaciones/editarh.html', datos=datos[0])

@app.route('/habitaciones/habitaciones/modificarh', methods=['POST'])
def modificarh():
    __codhab__ = request.form['filtro']
    __descriphab__ = request.form['descripcionhabitacion']
    __preciohab__ = request.form['preciohabitacion']
    __estadohab__ = request.form['estadohabitacion']
    conexion = mysql.connect()
    cursor =conexion.cursor()
    cursor.execute("UPDATE habitaciones SET descriphab=%s, preciohab=%s, estadohab=%s WHERE codhab=%s", (__descriphab__, __preciohab__, __estadohab__, __codhab__))
    conexion.commit()
    return redirect('/habitaciones/')

@app.route('/habitaciones/habitaciones/eliminarh', methods=['POST'])
def eliminarh():
    __codhab__=request.form['id']
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM habitaciones WHERE codhab=%s",(__codhab__))
    conexion.commit() 
    return redirect('/habitaciones/')
# fin CRUD libros


#fin ruta de las habitaciones

#ruta de reservas de usario inal
@app.route('/reservas')
def reservas():
    return render_template('reservas/reservas.html')

@app.route('/reservas/')
def reserv_habitaciones():
    conexion=mysql.connect()
    #Traer la información de la base de datos
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM habitaciones")
    reservas=cursor.fetchall()
    conexion.commit()  
    return render_template('reservas/reservas.html', reservas=reservas)

#fin ruta de reservas 




#ruta de de la pagina "Nosotros"
@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/nosotros/')
def snosotros():
    return render_template('sitio/nosotros.html')

#fin ruta de la pagina "Nosotros"

#ruta ver Habitaciones
@app.route('/habitaciones/')
def ver_habitaciones(): 
    return render_template('habitaciones/habitaciones.html', habitaciones=habitaciones)
#fin ruta ver habitaciones


#ruta inicio de sesion



#fin ruta inicio de sesion

if __name__=='__main__':
    app.run(debug=True)