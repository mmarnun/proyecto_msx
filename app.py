import json
from flask import Flask, render_template, request
app = Flask(__name__)	

with open('msx.json') as f:
    juegos = json.load(f)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/juegos',methods=["GET","POST"])
def juegos():
    if request.method=="POST":
        buscador=request.form.get("buscador")
        try:
            info="Prueba info".format(buscador)
        except:
            info="No hay"
        return render_template("listajuegos.html",info=info)
    else:
        return render_template("juegos.html")

app.run("0.0.0.0",5000,debug=True)