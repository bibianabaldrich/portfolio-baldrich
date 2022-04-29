from flask import Flask, redirect,request,make_response,render_template,url_for

app = Flask(__name__)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html', e=e), 404

@app.route('/')
def index():
    titulo = "Estas en casa"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)