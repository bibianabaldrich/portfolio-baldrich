from flask import Flask, redirect,request,make_response,render_template,url_for

app = Flask(__name__)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html', e=e), 404

@app.route('/')
def index():
    titulopagina = "Portafolio Bibiana Baldrich"
    soy="Soy"
    dw="Descargar HV"
    return render_template("index.html",titulopagina=titulopagina, soy=soy,dw=dw)

@app.route('/es')
def espanol():
    titulopagina = "Portafolio Bibiana Baldrich"
    return render_template("index.html")

@app.route('/en')
def ingles():
    titulopagina = "Bibiana Baldrich Portafolio"
    soy="I'm"
    dw="Download CV"
    return render_template("index.html",titulopagina=titulopagina, soy=soy,dw=dw)

if __name__ == "__main__":
    app.run(debug=True)