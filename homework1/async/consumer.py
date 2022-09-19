import threading
from random import randint
from time import sleep
from queue import Queue


def producer(que, cond):
    name = int(threading.current_thread().name)
    while True:
        sleep(randint(1, name))
        count_goods = randint(1, 4)
        print(f"Producer{name} put {count_goods} goods to the warehouse")
        for _ in range(count_goods):
            que.put(name)
            with cond:
                cond.notify_all()
            sleep(0.01)
        sleep(randint(1, 3))


def consumer(que, cond, cons):
    name = int(threading.current_thread().name)
    while True:
        for _ in range(name):
            with cond:
                cond.wait()
        name_good = que.get()
        print(f"Consumer{name} has taken Producer{name_good}'s good")
        for _ in range(cons - name):
            with cond:
                cond.wait()


if __name__ == "__main__":
    consumers = int(input("Enter number of consumers\n"))
    producers = int(input("Enter number of producers\n"))
    condition = threading.Condition(lock=None)
    queue = Queue()
    for i in range(1, consumers + 1):
        threading.Thread(name=str(i), target=consumer, args=(queue, condition, consumers,)).start()
    for i in range(1, producers + 1):
        threading.Thread(name=str(i), target=producer, args=(queue, condition,)).start()
