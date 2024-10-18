my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while len(my_list) > 0:
    a = my_list[0]
    if a > 0:
        print(my_list[0])
    my_list = my_list[1:]