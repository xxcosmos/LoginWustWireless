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
    column_names = ["username", "name", "password"]
    datas = []
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
        if (row_num - 1) % 9000 == 0 or row_num == row_count - 1:
            datas.append(records)
            records = []
    return datas


if __name__ == '__main__':
    tables = excel2json("namelist.xlsx")
    print(tables[0])
    num = -1
    for table in tables:
        num += 1
        json_data = json.dumps(table, ensure_ascii=False)
        filename = "namelist{number}.txt".format(number=num)
        with open(filename,"w") as f:
            f.write(json_data)
