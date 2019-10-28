import json

import xlrd

from db_config import StudentInfo, add_student_info, query_password_unmodified_student_info_list


def open_excel(file_path):
    try:
        data = xlrd.open_workbook(file_path)
        return data
    except Exception as e:
        print(str(e))


def excel2student_info(file_path="namelist.xlsx"):
    data = open_excel(file_path)
    table = data.sheet_by_index(0)
    row_count = table.nrows
    student_info_list = []

    for index in range(2, row_count):
        row = table.row_values(index)
        if row:
            student_info_list.append(StudentInfo(student_id=row[0], student_name=row[1], id_number=row[2],
                                                 is_wireless_password_unmodified=True))
    return student_info_list


# def excel2json(file_path):
#     data = open_excel(file_path)
#     table = data.sheet_by_index(0)
#     row_count = table.nrows
#     column_names = ["username", "name", "password"]
#     records = []
#     for row_num in range(2, row_count):
#         row = table.row_values(row_num)
#         if row:
#             record = {}
#             for i in range(len(column_names)):
#                 if i == 1:
#                     continue
#                 record[column_names[i]] = row[i]
#                 if i == 2:
#                     record[column_names[i]] = str(row[i])[6:14]
#             records.append(record)
#     return records


if __name__ == '__main__':
    student_info_list = query_password_unmodified_student_info_list()
    for student_info in student_info_list:
        print(student_info)