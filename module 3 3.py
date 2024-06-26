def print_params(a = 1, b = 'Бугагашенька', c = True):
    print(a, b, c)
# Вызов функции с передачей всех трех аргументов
print_params(10, 'новая строка', False)

# Вызов функции с передачей двух аргументов
print_params(5, 'еще одна строка')

# Вызов функции с передачей одного аргумента
print_params(100)

# Вызов функции без аргументов (используются значения по умолчанию)
print_params()

value_list = [1, 'русы', False]
value_dict = {'a': 4, 'b': 'айти', 'c': 9}
print_params(*value_list)
print_params(**value_dict)

value_list2 = [69, 'модули']
print_params(*value_list2, 56)
