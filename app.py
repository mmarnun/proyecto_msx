import json
from flask import Flask, render_template, request, redirect, url_for, abort
app = Flask(__name__)	

with open('msx.json') as r:
    infojuegos = json.load(r)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/juegos', methods=['GET', 'POST'])
def juegos():
    if request.method == 'POST':
        nombre = request.form.get('buscador', '')
        juegos = [juego for juego in infojuegos if str(juego['nombre']).lower().startswith(nombre.lower())]
        return render_template('listajuegos.html', juegos=juegos)
    else: 
        return render_template('juegos.html')

# @app.route('/listajuegos', methods=['POST'])
# def listajuegos():
#     nombre = request.form.get('buscador', '')
#     juegos = [juego for juego in infojuegos if str(juego['nombre']).lower().startswith(nombre.lower())]
#     return render_template('listajuegos.html', juegos=juegos)

@app.route('/juego/<int:id>',methods=["GET"])
def juego(id):
    for i in infojuegos:
        if i["id"] == id:
            return render_template('juego.html',juego=i)
    abort(404)
            
app.run("0.0.0.0",5000,debug=True)