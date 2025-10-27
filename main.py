def first(a, b):
    if a > b:
        print(f'Наибольшее - {a}\nНаименьшее - {b}')
    else:
        print(f'Наибольшее - {b}\nНаименьшее - {a}')

first(1, 5)

def second(a, b, c, d):
    array = [b, c, d]
    max_val = a
    for i in array:
        if max_val < i:
            max_val = i
    return max_val

print(second(1, 7, 3, 4))

def third(Anton, Boris, Drobovictor):
    dict = {'Антон': Anton, 'Борис': Boris, 'Дробовиктор': Drobovictor}
    max_val = Anton
    for i in dict.values():
        if max_val < i:
            max_val = i
    old = []
    for key, value in dict.items():
        if value == max_val:
            old.append(key)
    return f"Самые старшие: {', '.join(old)}"
print(third(17, 17, 16))

def fourth(a, b):
    if 0 > a or a > b:
        return 'incorrect input'
    for i in range(a, b+1):
        print(f'{i} * {i} = {i*i}')
fourth(10, 12)

def fifth(a, b):
    res = 0
    if (a < 0) == (b < 0):
        if a < 0:
            for i in range(-a):
                res -= b
        else:
            for i in range(a):
                res += b
    else:
        if a > 0:
            for i in range(a):
                res -= b
        else:
            for i in range(b):
                res -= a
    return res
print(fifth(-5, -10))

def sixth(n):
    a, b = 0, 1
    res = 0
    while b < n:
        res += b
        a, b = b, a + b
    return res

print(f'Сумма равна {sixth(1)}')
print(f'Сумма равна {sixth(10000)}')
