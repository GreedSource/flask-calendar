import shutil
# decodigo.com
"""fuente = "resources/template.xlsx"
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
ws['B9'] = 'today'"""

from datetime import date, datetime, timedelta

fin = '24/11/2019'

date_object = datetime.strptime(fin, '%d/%m/%Y')
#fin = date_object.strftime('%Y-%m-%d')


def __weekday(day):
         date_number = day.weekday()
         if date_number < 5:
               print('weekday')
         else:
               new_date = day - timedelta(days=1)
               __weekday(new_date)
               print('weekend')

__weekday(date_object)