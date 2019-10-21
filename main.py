import requests
import json


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


def get_json_object(path):
    with open(path) as f:
        return json.load(f)


if __name__ == '__main__':
    account_list = get_json_object("account_list.json")
    for account in account_list:
        username = account["username"]
        password = str(account["pwd"])[6:14]
        print("学号：%s\t密码：%s" % (username, password))

        response = login_by_username(username, password)
        message = str(response["message"])
        result = response["result"]

        if message.find("当前无可用套餐") != -1:
            continue
        if message.find("密码错误") != -1:
            account_list
        if result == "success" or result == "online":
            print("连接成功")
            break
        if message.find("内部") >= 0:
            print(message)
            break
