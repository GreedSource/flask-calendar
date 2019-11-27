from datetime import datetime, timedelta
import xlrd, json
from __class.weekday import process_data
import openpyxl

class xlsx_reader(object):

    def json_output(self, data):
        date = datetime.now()
        name = 'calendario'+ date.strftime('%Y%m%d-%H%M%S')
        with open(f'json/{name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
        
    def read(self, file):
        all_data = []
        excel = xlrd.open_workbook(file)
        sheet_0 = excel.sheet_by_index(0) # Open the first tab
        prev_row = [None for i in range(sheet_0.ncols)]
        first = True
        for row_index in range(sheet_0.nrows):
            if first == False:
                row = []
                for col_index in range(sheet_0.ncols):
                    value = sheet_0.cell(rowx=row_index,colx=col_index).value
                    if len(value) == 0:
                        value = prev_row[col_index]
                    row.append(value)
                prev_row = row
                all_data.append(row)
            else:
                first = False
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
        data = self.parse_to_json(data)
        return data

    def parse_to_json(self, data):
        array = {}
        array['lunes'] = []
        array['martes'] = []
        array['miercoles'] = []
        array['jueves'] = []
        array['viernes'] = []
        for hour in data:
            if type(hour[1]) != str:
                tmp = hour[1]
                tmp.append(1)
                if any(list == tmp for list in array['lunes']):
                    x = array['lunes'].index(tmp)
                    y = len(hour[1]) - 1
                    array['lunes'][x][y] += 1
                else:
                    array['lunes'].append(tmp)
            if type(hour[2]) != str:
                tmp = hour[2]
                tmp.append(1)
                if any(list == tmp for list in array['martes']):
                    x = array['martes'].index(tmp)
                    y = len(hour[2]) - 1
                    array['martes'][x][y] += 1
                else:
                    array['martes'].append(tmp)
            if type(hour[3]) != str:
                tmp = hour[3]
                tmp.append(1)
                if any(list == tmp for list in array['miercoles']):
                    x = array['miercoles'].index(tmp)
                    y = len(hour[3]) - 1
                    array['miercoles'][x][y] += 1
                else:
                    array['miercoles'].append(tmp)
            if type(hour[4]) != str:
                tmp = hour[4]
                tmp.append(1)
                if any(list == tmp for list in array['jueves']):
                    x = array['jueves'].index(tmp)
                    y = len(hour[4]) - 1
                    array['jueves'][x][y] += 1
                else:
                    array['jueves'].append(tmp)
            if type(hour[5]) != str:
                tmp = hour[5]
                tmp.append(1)
                if any(list == tmp for list in array['viernes']):
                    x = array['viernes'].index(tmp)
                    y = len(hour[5]) - 1
                    array['viernes'][x][y] += 1
                else:
                    array['viernes'].append(tmp)
        array = self.obtain_majors(array)
        self.json_output(array)
        return array

    def obtain_majors(self, data):
        array = []
        for record in data:
            for row in data[record]:
                    if not (row[1] in array):
                        if row[1] != 'Tutorías':
                                #tmp = [row[1], record]
                                array.append(row[1])
                                #array.append(tmp)

        output = {}
        for record in data:
            for major in array:
                    if not major in output:
                        for row in data[record]:      
                                if row[1] == major:
                                    hours = row[len(row)-1]
                                    if hours > 1:
                                        #tmp = [record, hours]
                                        output[major] = [record]
                    else:
                        for row in data[record]:      
                                if row[1] == major:
                                    hours = row[len(row)-1]
                                    if hours > 1:
                                        #tmp = [record, hours]
                                        output[major].append(record)
        return output

class xlsx_writer(object):
    def __init__(self, carrera, grado, grupo):
        self.carrera = carrera
        self.grado = grado
        self.grupo = grupo
        import shutil
        fuente = "resources/template.xlsx"
        date = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        name = f'calendario-{carrera}-{grado}{grupo}-{date}'
        name = f'output/{name}.xlsx'
        self.name = name
        shutil.copyfile(fuente, name)

    def date_assignament(self, majors, corte, habiles):
        array = {}
        for major in majors:
            index = len(majors[major]) - 1
            last = majors[major][index]
            wd = process_data()
            day = wd.date_assignament(last)
            for row in corte:
                if row.weekday() == day:
                    if not major in array:
                        array[major] = [row]
                    else:
                        array[major].append(row)
                else:
                    date = self.__recursive_date_validation(row, day, habiles)
                    if not major in array:
                        array[major] = [date]
                    else:
                        array[major].append(date)
        return array

    def __recursive_date_validation(self, date, wd, habiles):
        date = date - timedelta(days=1)
        if date.weekday() == wd:
            if date in habiles:
                return date
            else:
                return self.__recursive_date_validation(date, wd, habiles)
        else:
            return self.__recursive_date_validation(date, wd, habiles)

    def write(self, corte, majors, habiles):
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        wb = openpyxl.load_workbook(self.name)
        ws = wb.worksheets[0]
        ws['B2'] = f'{self.grado}-{self.grupo}'
        index = 1
        for item in corte:
            item = item.strftime('%d-%m-%Y')
            cell = f'{columns[index]}8'
            ws[cell] = item
            index += 1
        index = 9
        for major in majors:
            cell = f'A{index}'
            ws[cell] = major
            index += 1
        fechas = self.date_assignament(majors, corte, habiles)
        row = 9
        for major in fechas:
            column = 1
            for fecha in fechas[major]:
                cell = f'{columns[column]}{row}'
                ws[cell] = fecha.strftime('%d-%m-%Y')
                column += 1
            row += 1
        wb.save(self.name)