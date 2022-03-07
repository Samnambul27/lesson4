def gen2():
    list = [4, 15, None, "new_list"]

    from itertools import islice
    from itertools import cycle

    for el in islice(cycle(list), 10): #повторение элементов списка будет прекращено после 10ого повторения
        print(el)
gen2()