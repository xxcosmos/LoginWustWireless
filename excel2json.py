import json

import xlrd


def open_excel(file_path):
    try:
        data = xlrd.open_workbook(file_path)
        return data
    except Exception as e:
        print(str(e))


def excel2json(file_path):
    data = open_excel(file_path)
    table = data.sheet_by_index(0)
    row_count = table.nrows
    column_names = ["username","name","password"]
    records = []
    for row_num in range(2, row_count):
        row = table.row_values(row_num)
        if row:
            record = {}
            for i in range(len(column_names)):
                if i == 1:
                    continue
                record[column_names[i]] = row[i]
                if i == 2:
                    record[column_names[i]] = str(row[i])[6:14]
            records.append(record)
    return records


if __name__ == '__main__':
    records = excel2json("namelist.xlsx")
    json_data = json.dumps(records, ensure_ascii=False, indent=2)
    with open("namelist.json", 'w') as f:
        f.write(json_data)
