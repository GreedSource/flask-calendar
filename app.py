import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from classes.svg_reader import reader
import json

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
    """import pandas as pd
    df = pd.read_excel('resources/excel-sample.xlsx')
    json = df.values.tolist()"""
    import xlrd
    all_data = []
    excel = xlrd.open_workbook('resources/excel-sample.xlsx')
    sheet_0 = excel.sheet_by_index(0) # Open the first tab
    prev_row = [None for i in range(sheet_0.ncols)]
    for row_index in range(sheet_0.nrows):
        row = []
        for col_index in range(sheet_0.ncols):
            value = sheet_0.cell(rowx=row_index,colx=col_index).value
            if len(value) == 0:
                value = prev_row[col_index]
            row.append(value)
        prev_row = row
        all_data.append(row)
    ######
    data = []
    for row in all_data:
        #data.append(row)
        tmp = []
        for child in row:
            if child and '\n' in child:
                child = child.split('\n')
            tmp.append(child)
        data.append(tmp)
    with open('output/result.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)