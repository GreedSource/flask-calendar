import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
from svg_reader import reader

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './uploads'
ALLOWED_EXTENSIONS = set(['svg'])

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/subir')
def upload():
    return render_template('form.html')

@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        file = os.path.join(app.config['UPLOAD_FOLDER'],filename);
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(file)
        my_list = reader.read(file)
        os.remove(file)
    # Retornamos una respuesta satisfactoria
    #return "<h1>Archivo subido exitosamente</h1>"
    return render_template("output.html", data=my_list)

if __name__ == "__main__":
    app.run(debug=True)