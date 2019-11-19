from datetime import datetime
import xlrd, json


class xlsx_reader(object):
    def json_output(self, data):
        date = datetime.now()
        name = 'calendario'+ date.strftime('%Y%m%d-%H%M%S')
        with open(f'output/{name}.json', 'w', encoding='utf-8') as f:
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
        self.json_output(data)
        return data

