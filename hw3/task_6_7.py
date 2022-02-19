# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text
# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
# пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
# исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
# написанную ранее функцию int_func().

# 6
def int_func(word):
    small_letter = word[0]
    if small_letter.islower():
        big_letter = chr(ord(small_letter) - ord('a') + ord('A'))
        return big_letter + word[1:]
    else:
        return word


# 7

in_list = list(input('Enter the words separated by a space: ').strip().split())
out_str = ''

for el in in_list:
    out_str += int_func(el) + ' '

print(out_str)
