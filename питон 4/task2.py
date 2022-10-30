def get_count_char(str_):
    dict_ = {}
    str_raboch = "".join(c for c in str_.lower() if c.isalpha())
    for letter in str_raboch:
        if letter in dict_:
             dict_[letter] += 1
        else:
            dict_[letter] = 1
    return dict_
            # TODO посчитать количество каждой буквы в строке в аргументе str_
dict_new = get_count_char
def new_dict(dict_new):
    list_new_values = dict_new.values()
    list_new_keys = dict_new.keys()
    sum_ = sum(list_new_values)
    list_prozent = []
    for i in list_new_values:
        list_prozent += [round(i/sum_*100,1)]
    dict_prozent = dict(zip(list_new_keys,list_prozent))
    return dict_prozent



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(new_dict(get_count_char(main_str)))
print(sum(new_dict(get_count_char(main_str)).values()))