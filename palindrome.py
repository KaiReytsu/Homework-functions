# Напишите функцию, которая проверяет является ли число палиндромом. 
# Число передаётся в качестве параметра. 
# Если число палиндром нужно вернуть из функции
#   true, иначе false.

def is_palindrome(number):
    """Returns whether the number is a palindrome"""
    if number < 0:
        number *= -1
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

number = int(input('Input number: '))
print('Number', number, 'is polindrome?', is_palindrome(number))