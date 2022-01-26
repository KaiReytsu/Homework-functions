# Напишите функцию, которая считает количество цифр в числе. 
# Число передаётся в качестве параметра. 
# Из функции нужно вернуть полученное количество цифр.
# Например, если передали 3456, количество цифр будет 4.

def digit_number(number):
    """Return the length of a given number"""
    num_to_str = str(number)
    len_of_string = len(num_to_str)
    return len_of_string

random_number = int(input('Enter number: '))
print('Length of number', random_number, 'is', digit_number(random_number))

