# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

string = input("Введите строку для сжатия: ")

def coding(strint):
    char = string[0]
    count = 1
    code = ""
    for i in range(1, len(string)):
        if char == string[i]:
            count += 1
        else:
            code += str(count) + char
            char = string[i] 
            count = 1
    return code + str(count) + char

def decoding(code_strint):
    decode_string = ""
    num = ''
    for i in code_strint:
        if i.isdigit():
            num += i
        else:
            decode_string += i * int(num)
            num = ''
    return decode_string

code_strint = coding(string)

print(f"Строка после сжатия: {code_strint}")
print(f"Восстановленная строка: {decoding(code_strint)}")


