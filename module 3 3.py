def print_params(a = 1, b = 'Бугагашенька', c = True):
    print(a, b, c)
# Вызов функции с передачей всех трех аргументов
print_params(39, 'строка', False)

# Вызов функции с передачей двух аргументов
print_params(25, 'фильмы')

# Вызов функции с передачей одного аргумента
print_params(77)

# Вызов функции без аргументов (используются значения по умолчанию)
print_params()

# Вызов функции с передаче позиционных и непозиционных параметров
value_list = [1, 'русы', False]
value_dict = {'a': 4, 'b': 'айти', 'c': 9}
print_params(*value_list)
print_params(**value_dict)

value_list2 = [69, 'модули']
print_params(*value_list2, 56)

