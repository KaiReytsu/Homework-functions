# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. 
# Границы диапазона передаются в качестве параметров. 
# Если границы диапазона перепутаны 
#   (например, 5 — верхняя граница, 25 — нижняя граница), 
# их нужно поменять местами.

def produst_of_num(begin_num, end_num):
    """Product of numbers in a given range"""
    num_product = 0
    if begin_num < end_num:
        num_product = begin_num
        while begin_num < end_num:
            num_product = num_product * (begin_num + 1)
            begin_num += 1
    else:
        num_product = end_num
        while end_num < begin_num:
            num_product = num_product * (end_num + 1)
            end_num += 1
    return num_product

input_one = int(input('Input the first number of the range: '))
input_two = int(input('Input the second number of the range: '))
print('Product of numbers in the range from', input_one, 'to', input_two, 'is',  produst_of_num(input_one, input_two))