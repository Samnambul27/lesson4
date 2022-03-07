def gen1():
    a = int(input('Введите стартовое число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(a), 10): #генерирует 10 чисел начиная с указанного
        print(i)
gen1()