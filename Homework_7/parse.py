def listExample(stringExample):
    example = stringExample.replace(' ', '')
    example = example.replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')
    example = example.split()
    return example