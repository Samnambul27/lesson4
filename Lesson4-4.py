my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 10, 12, 13, 13]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Исходный список {my_list}, 'f'Не повторяющиеся числа {my_new_list}')
