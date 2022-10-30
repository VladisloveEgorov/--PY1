word_dict = {}


def get_count_char(str_):
    str_ = str_.lower()
    str1 = ''
    for i in str_:
        if i.isalpha():
            str1 = ''.join([str1, i])
    for sym in str1:
        if sym in word_dict:
            word_dict[sym] += 1
        else:
            word_dict[sym] = 1
    return word_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


def procent(dict_):
    dict_1 = {}
    total_count = sum(dict_.values())
    for i, value in dict_.items():
        dict_1[i] = value * 100 / total_count
    return dict_1
