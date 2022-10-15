import threading
from time import sleep


def main_notify(cond, n):
    for _ in range(n * 3):
        with cond:
            cond.notify_all()
        sleep(0.001)


def print_numbers(cond, n):
    name = int(threading.current_thread().name)
    for _ in range(n):
        with cond:
            for _ in range(name):
                cond.wait()
        print(name, end="")
        with cond:
            for _ in range(3 - name):
                cond.wait()


def numbers():
    condition = threading.Condition(lock=None)
    n = int(input())

    for i in range(1, 4):
        threading.Thread(name=str(i), target=print_numbers, args=(condition, n,)).start()
    threading.Thread(name="main", target=main_notify, args=(condition, n,)).start()


if __name__ == "__main__":
    numbers()
