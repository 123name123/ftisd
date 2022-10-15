def init():
    return list()


def size(data):
    return len(data)


def empty(data):
    return size(data) == 0


def push(data, val):
    return data + [val]


def top(data):
    return None if empty(data) else data[-1]


def pop(data):
    return data if empty(data) else data[:size(data) - 1]


def print_top(data):
    print(data[-1])
    return data


if __name__ == "__main__":
    print_top(pop(pop(print_top(push(push(push(push(init(), 5), 10), 15), 20)))))
