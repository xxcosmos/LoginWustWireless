import requests


def login_by_username(username, password):
    url = r"http://10.200.2.2:9090/zportal/login/do"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    data = {
        "username": str(username),
        "pwd": str(password),
        "wlanuserip": "f09df0ee06255f08c28797b2f2383ef8",
        "nasip": "5340d13e4208e1b891476c890b7f5f5c"
    }

    response = requests.post(url, data, headers=headers)
    return response.json()


def handle_response(student_info):
    username = student_info.student_id
    password = student_info.id_number[6, 14]
    response = login_by_username(username, password)
    message = str(response["message"])
    result = str(response["result"])

    if "online" in result:
        return -10
    if "密码错误" in message:
        return -1
    if "内部" in message:
        return -2
    return 0
