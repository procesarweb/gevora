
from flask import Flask,render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL
from requests import post
import MySQLdb.cursors
import re

app=Flask(__name__)
app.secret_key="gv"
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




#Restricción para ingreso no autorizado, enrutado hacia la raiz
@app.route('/admin/inicio')
def admin_inicio():
    if not 'login' in session:
        return redirect("/")

#@app.route('admin/login')
#def admin_login():
 #   return render_template('admin/login.html',login=login)
 #   return redirect('admin/login.html')

#rutas de las habitaciones - administrador y Super admin


@app.route('/habitaciones')
def habitaciones():
    return render_template('habitaciones/habitaciones.html')

@app.route('/habitaciones/')
def hab_habitaciones():
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM habitaciones")
    habitaciones=cursor.fetchall()
    conexion.commit()  
    return render_template('habitaciones/habitaciones.html', habitaciones=habitaciones)

@app.route('/habitaciones/habitaciones/guardar', methods=['POST'])
def habitaciones_guardar():
    __codhab = request.form['codigo_hab']
    __descriphab = request.form['descripcionhabitacion']
    __preciohab = request.form['preciohabitacion']
    __estadohab = request.form['estadohabitacion']
       #Ejecutar la sentencia de inserción de datos a la tabla
    sql="INSERT INTO habitaciones (codhab,descriphab, preciohab, estadohab) VALUES (%s,%s, %s, %s)" #preciohab, estadohab
    datos=(__codhab,__descriphab, __preciohab, __estadohab)
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect('/habitaciones/')

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
# fin CRUD habitaciones


#fin ruta de las habitaciones

#ruta de reservas de usario final
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
    return render_template('admin/nosotros.html')

#fin ruta de la pagina "Nosotros"

@app.route('/registrar/guardar', methods=['POST'])
def registrar_guardar():
    __tipodoc = request.form['tipodoc']
    __idusu = request.form['numerodocumento']
    __nombrecompleto = request.form['nombrecompleto']
    __direccion = request.form['direcciondeusuario']
    __telefono = request.form['telefonousuario']
    __nombreusuario = request.form['user_usu']
    __password = request.form['password_usuario']
    conexion = mysql.connect()
    cursor =conexion.cursor()
    sql = "INSERT INTO usuarios (tipo_doc_usu, id_usu, nom_ape_usu,dir_usu,movil_usu,user_usu,pasw_usu) values (%s,%s,%s,%s,%s,%s,%s)"
    datos=(__tipodoc,__idusu, __nombrecompleto, __direccion, __telefono, __nombreusuario, __password)
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect('/registrar')

#ruta registro
@app.route('/registrar')
def registrar():
    return render_template('login/registrar.html')

#ruta login
@app.route('/login', methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'user_usu' in request.form and 'password_usuario' in request.form:
        # Create variables for easy access
        username = request.form['user_usu']
        password = request.form['password_usuario']
        # Check if account exists using MySQL
        conexion = mysql.connect()
        cursor =conexion.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE user_usu = %s AND pasw_usu = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[1]
            session['username'] = account[5]
            # Redirect to home page
            print('Logged in successfully')
            return 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('/login/login.html', msg=msg)

#logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    #redirect to login
    return redirect(url_for('login'))
#ruta ver Habitaciones
#@app.route('/habitaciones/')
#def ver_habitaciones(): 
#    return render_template('habitaciones/habitaciones.html', habitaciones=habitaciones)
#fin ruta ver habitaciones


#ruta inicio de sesion


#fin ruta inicio de sesion

if __name__=='__main__':
    app.run(debug=True)