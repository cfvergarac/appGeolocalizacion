from flask import Flask
from flask import Flask,render_template
from pymongo import MongoClient
from flask import Flask,render_template, request, redirect, url_for
from geopy.geocoders import Nominatim


app = Flask(__name__)

@app.route('/')
@app.route('/inicio')
def index():
    lg=listaGerentes()
    return render_template('inicio.html',gerentes = lg)



@app.route('/agregar')
def agregar():
    return  render_template("agregar.html")


@app.route('/mapa')
def mapa():
    lg=listaGerentes()
    return render_template('mapa.html',gerentes = lg)
    

@app.route('/registrar', methods=["GET", "POST"])
def registrar():
    nombres = request.form['nombres']
    sexo = request.form['sexo']
    empresa = request.form['empresa']
    fortuna = request.form['fortuna']
    direccion = request.form['direccion']
    insertaGerente(nombres,sexo,empresa,fortuna,direccion)
    return redirect(url_for('index'))



# Lista los datos de los gerentes de la colección mongo
def listaGerentes():
    mongo = MongoClient("localhost",27017)
    dbempresas = mongo["empresas"]
    coleccionGerentes =  dbempresas["gerentes"]
    listagerentes = coleccionGerentes.find()
    mongo.close()
    return ([lg for lg in listagerentes])  


#Registrar nuevo gerente
def insertaGerente(nombres, sexo, empresa, fortuna, direccion):
    mongo = MongoClient("localhost",27017)
    dbempresas = mongo["empresas"]
    coleccionGerentes =  dbempresas["gerentes"]
    
    app = Nominatim(user_agent="DEG52")
    direcc = app.geocode(direccion)
    if(direcc != None):
        vdireccion = direcc.address
        latitud = direcc.latitude
        longitud = direcc.longitude
    else:
        vdireccion = direccion
        latitud = ""
        longitud = ""
    
    coleccionGerentes.insert({"nombres":nombres,"sexo":sexo,"empresa":empresa,"fortuna":fortuna,"direccion":vdireccion,"latitud":latitud,"longitud":longitud})
    mongo.close()






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

