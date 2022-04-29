from flask import Flask, redirect,request,make_response,render_template,url_for
from info import *
app = Flask(__name__)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html', e=e), 404

@app.route('/')
def index():
    barranavegacion = ["Inicio", "Sobre Mi", "Proyectos", "Contacto",'EN']
    titulopagina = "Portafolio Bibiana Baldrich"
    soy="Soy"
    cargo=['Diseñadora web', 'Desarrolladora Web', 'Diseñadora web']
    dw=["Descargar HV","Contactar"]
    return render_template("index.html",barranavegacion=barranavegacion,titulopagina=titulopagina, soy=soy,cargo=cargo,dw=dw,sobremi=sobremi1,tec=tecnoES,servi=serviES,listtec=listtec)

# @app.route('/es')
# def espanol():
#     titulopagina = "Portafolio Bibiana Baldrich"
#     return render_template("index.html")

@app.route('/en')
def ingles():
    barranavegacion = ["Home", "About", "Portfolio", "Contact","ES"]
    titulopagina = "Bibiana Baldrich Portafolio"
    soy="I'm"
    cargo=['Wed Design', 'Web Developer', 'Web Design']
    dw=["Download CV","Contact"]
    
    return render_template("index.html",barranavegacion=barranavegacion,titulopagina=titulopagina, soy=soy,cargo=cargo,dw=dw ,sobremi=sobremi2,tec=tecnoEN,servi=serviEN,listtec=listtec)

if __name__ == "__main__":
    app.run(debug=True)