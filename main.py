from flask import Flask, url_for, render_template

app = Flask(__name__)


#rotas
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/sobre')
def sobre():
    return "sobre nós"

@app.route('/pagina3')
def pagina3():
    return "nova página 1"

@app.route('/pagina4')
def pagina4():
    return "nova página 4"


if __name__=='__main__':
    app.run(debug=True)



