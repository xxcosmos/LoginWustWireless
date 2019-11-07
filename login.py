import requests

from excel2json import get_json_data


def login_by_username(username, password):
    url = r"http://10.200.2.2:9090/zportal/login/do"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    data = {
        "username": str(username),
        "pwd": str(password),
        "wlanuserip": "f09df0ee06255f08c28797b2f2383ef8",
        "nasip": "5340d13e4208e1b891476c890b7f5f5c"
    }

    response = requests.post(url, data, headers=headers).json()
    return response_handler(response)


def response_handler(response):
    print(response["message"])
    response = str(response)
    if "online" in response or "success" in response:
        return True
    if "密码错误" in response or "内部" in response:
        return False


def login():
    filepath = "available_account.json"
    account_list = get_json_data(filepath)
    for account in account_list:
        if login_by_username(account["username"], account["password"]):
            print("login successfully")
            break


if __name__ == '__main__':
    login()
