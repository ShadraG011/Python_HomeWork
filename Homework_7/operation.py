opSelect = {
    "*": lambda x, y: int(x) * int(y),
    "/": lambda x, y: int(x) / int(y),
    "+": lambda x, y: int(x) + int(y),
    "-": lambda x, y: int(x) - int(y)
    }

def deleteElement(example, i):
    example.pop(i + 1)
    example.pop(i)

def operation(example, i, oper):
    if example[i] == oper:
        example[i - 1] = opSelect.get(oper)(int(example[i - 1]), int(example[i + 1]))
        deleteElement(example, i)
        return True