import view
import parse
import operation

def start():
    example = parse.listExample(view.getExample())
    end = view.giveExample(example)
    while len(example)>1:
        if '*' in example or '/' in example:
            for i in range(len(example)):
                if operation.operation(example, i, '*'): break
                if operation.operation(example, i, '/'): break

        elif '+' in example or '-' in example:
            for i in range(len(example)):
                if operation.operation(example, i, '+'): break
                if operation.operation(example, i, '-'): break
    print(f"Результат: {end} = {example[0]}")
