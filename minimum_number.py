# Напишите функцию, которая возвращает минимальное из пяти чисел. 
# Числа передаются в качестве параметров.
from random import randint

def minimum_number(num_one, num_two, num_three, num_four, num_five):
    """Return the minimum of the given numbers"""
    list_of_num = [num_one, num_two, num_three, num_four, num_five]
    minimun = min(list_of_num)
    return minimun

def random_numbers():
    """Return a list of random numbers"""
    step = 0
    limit_num = 5
    list_of_num = []
    while step < limit_num:
        rand_num = randint(0, 1000)
        list_of_num.append(rand_num)
        step += 1
    return list_of_num

numbers = random_numbers()

min_of_numbers = minimum_number(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])
print('Minimum number in list:', *numbers, 'is', min_of_numbers)