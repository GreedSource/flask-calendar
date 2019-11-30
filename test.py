import xlwt
import xlrd
import xlutils
import copy

wb1 = xlrd.open_workbook(r'output/prueba.xlsx')
copia = copy.copy(wb1)
hoja = copia.sheet_by_name(r'Grupo - ITI')
hoja.cell(12,3).value = 5 #solo para probar la edicion

copia.save('output/prueba.xlsx')