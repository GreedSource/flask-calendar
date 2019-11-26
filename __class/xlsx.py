from datetime import datetime
import xlrd, json


class xlsx_reader(object):

    def json_output(self, data):
        date = datetime.now()
        name = 'calendario'+ date.strftime('%Y%m%d-%H%M%S')
        with open(f'json/{name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
        
    def reader(self, file):
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
        self.json_output(array)
        return array

