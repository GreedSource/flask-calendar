from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from __class.weekday import weekday
from __class.xlsx import xlsx_reader
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './uploads'
ALLOWED_EXTENSIONS = set(['xlsx'])

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/subir')
def upload():
    return render_template('form.html')

@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # Guardamos el archivo en el directorio "Archivos PDF"

        f.save(file)
        obj = xlsx_reader()
        my_list = obj.reader(file)
        os.remove(file)
    # Retornamos una respuesta satisfactoria
    return jsonify(my_list)
    #return render_template("output.html", data=my_list)

@app.route('/uploads', methods=['post'])
def pandas():
    #########
    if request.method == 'POST':
        #data = request.form.getlist('inhabiles')
        data = request.get_json()
        inhabiles = weekday('2019-11-01', '2019-12-31')
    return jsonify(inhabiles.obtener_habiles(data))

if __name__ == "__main__":
    app.run(debug=True)