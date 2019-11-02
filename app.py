import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from classes.svg_reader import reader

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './uploads'
ALLOWED_EXTENSIONS = set(['svg'])

@app.route("/")
def home():
    return render_template("master.html")

@app.route("/index")
def index():
    return render_template("master.html")

@app.route('/subir')
def upload():
    return render_template('form.html')

@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        file = os.path.join(app.config['UPLOAD_FOLDER'], filename);
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(file)
        my_list = reader.read(file)
        os.remove(file)
    # Retornamos una respuesta satisfactoria
    return jsonify(my_list)
    #return render_template("output.html", data=my_list)

@app.route('/uploads', methods=['post'])
def pandas():
    import pandas as pd
    df = pd.read_excel('resources/excel-sample.xlsx')
    json = df.values.tolist()
    return jsonify(json)

if __name__ == "__main__":
    app.run(debug=True)