from flask import Flask, render_template

app = Flask(__name__)

# ! para renderizar templates o archivos html con flask
@app.route('/inicio')
def inicio():
    return render_template('inicio.html', nombre='Lena')

if __name__ == '__main__':
    app.run(debug=True)