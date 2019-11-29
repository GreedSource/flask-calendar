from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from __class.weekday import weekday, process_data
from __class.xlsx import xlsx_reader, xlsx_writer
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './uploads'
ALLOWED_EXTENSIONS = set(['xlsx'])

@app.route("/")
def home():
    # Abrir un archivo
    path = "output"
    dirs = os.listdir(path)
    records = []
    index = 1
    for file in dirs:
        tmp = [index, file]
        records.append(tmp)
        index+=1
    return render_template("home.html", records=records)

@app.route('/return-files', methods=['GET'])
def return_file():
    if request.method == 'GET':
        file = request.args.get('file')
    #return send_file(f'/output/{file}', as_attachment=True, attachment_filename=file)
    return send_file(f'output/{file}', as_attachment=True)

@app.route('/subir')
def upload():
    return render_template('form.html')

@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        #################REQUEST########################
        f = request.files['archivo']
        parcial1 = request.form.get('parcial-1')
        parcial2 = request.form.get('parcial-2')
        parcial3 = request.form.get('parcial-3')
        ordinario = request.form.get('ordinario')
        extra1  = request.form.get('extra-1')
        extra2  = request.form.get('extra-2')
        calendario = request.form.get('calendario')
        grado = request.form.get('grado')
        grupo = request.form.get('grupo')
        carrera = request.form.get('carrera')
        #################FILES####################
        filename = secure_filename(f.filename)
        file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(file)
        reader = xlsx_reader()
        majors = reader.read(file)
        os.remove(file)
        ###########################
        if calendario:
            calendario = calendario.split(',')
        entregas = [parcial1, parcial2, parcial3, ordinario, extra1, extra2]

        inhabiles = weekday(parcial1, extra2)
        habiles = inhabiles.obtener_habiles(calendario)
        
        process = process_data()
        processed = process.get_dates(entregas)
        #print(processed.get_dates())
        writer = xlsx_writer(carrera, grado, grupo)

        writer.write(processed, majors, habiles, entregas)
    # Retornamos una respuesta satisfactoria
    return jsonify(majors)
    #return render_template("output.html", data=my_list)

@app.route('/uploads', methods=['post'])
def pandas():
    #########
    if request.method == 'POST':
        #data = request.form.getlist('inhabiles')
        #data = request.get_json()
        days = request.form.get('date')
        data = days.split(',')
        inhabiles = weekday('2019-11-01', '2019-12-31')
        print(days)
    return jsonify(inhabiles.obtener_habiles(data))

if __name__ == "__main__":
    app.run(debug=True)