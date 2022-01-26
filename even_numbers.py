# Напишите функцию, 
# 1. которая принимает два числа в качестве параметра 
# 2. отображает все четные числа между ними.


def even_numbers(first_num, second_num):
    """Return all even numbers in a given interval"""
    even_num = []
    parity = 2
    if first_num < second_num:
        while first_num <= second_num:
            if first_num % parity == 0:
                even_num.append(first_num)
            first_num += 1
    else:
        while second_num <= first_num:
            if second_num % parity == 0:
                even_num.append(second_num)
            second_num += 1
    return even_num


input_number_one = int(input('Input your first number: '))
input_number_two = int(input('Input your second number: '))
print('All even numbers in a given interval:', *even_numbers(input_number_one, input_number_two))

