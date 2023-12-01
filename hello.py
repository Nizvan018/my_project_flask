from flask import Flask, render_template, url_for, request
from markupsafe import escape
from datetime import datetime

app = Flask(__name__) #indica que es la aplicación de Flask

# FILTROS PERSONALIZADOS:
@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')
# app.add_template_filter(today, 'today')

# FUNCIONES PERSONALIZADAS:
@app.add_template_global
def repeat(s, n):
    return s * n
# app.add_template_global(repeat, 'repeat')

# RUTAS:
@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('hello', name='Nizvan', age='22'))
    print(url_for('code', code = 'print("Hola")'))
    name = 'nizvan'
    friends = ['Oliver', 'Ubish', 'Naim', 'Vivi', 'Jafed', 'Juan']
    date = datetime.now()

    return render_template(
        'index.html', 
        name = name, 
        friends = friends, 
        date = date,
    )

@app.route('/hello')
@app.route('/hello/<string:name>')
@app.route('/hello/<string:name>/<int:age>') 
@app.route('/hello/<string:name>/<int:age>/<string:email>') #por defecto recibe string (int, float, paht, uuid)
def hello(name = None, age = None, email = None):
    data = {
        'name': name,
        'age': age,
        'email': email
    }

    return render_template('hello.html', data = data)
    

@app.route('/code/<path:code>')
def code(code):
    return f'<h1>{escape(code)}</h1>'

@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        return f'Nombre de usuario: {username}, contraseña: {password}'

    return render_template('auth/register.html')