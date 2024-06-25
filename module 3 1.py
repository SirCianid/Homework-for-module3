calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    s = (len(string), string.upper(), string.lower())
    return s

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [s.lower() for s in list_to_search]

s = string_info('Вероника')
print(s)
s = string_info('Руки Вверх')
print(s)
print(is_contains('Python', ['megaton', 'TON', 'Python']))
print(is_contains('bus', ['gAs', 'BigFloppa', 'abyss']))
print(calls)
