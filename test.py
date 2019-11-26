import shutil
# decodigo.com
fuente = "resources/template.xlsx"
destino = "output/template.xlsx"
shutil.copyfile(fuente, destino)

import os

# Abrir un archivo
path = "output"
dirs = os.listdir(path)

# Esto va a imprimir todos los archivos del directorio
for file in dirs:
   print (file)

import openpyxl

wb = openpyxl.load_workbook(destino)
ws = wb.worksheets[0]
ws['B9'] = 'today'

wb.save(destino)