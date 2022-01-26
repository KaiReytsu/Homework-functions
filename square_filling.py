# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. 
# Функция принимает в качестве параметров: 
# 1.длину стороны квадрата
# 2.символ
# 3.переменную логического типа:
#     * если она равна True, квадрат заполненный;
#     * если False, квадрат пустой.


def square_filling(lenght_sq, simbol, bool_var):
    """Draws a square according to the specified parameters"""
    step = 0
    if bool_var:
        while step < lenght_sq:
            print((simbol + ' ') * lenght_sq)
            step += 1
    else:
        print(simbol * lenght_sq)
        for item in range(lenght_sq - 2):
            print(simbol + ' ' * (lenght_sq - 2) + simbol)
        print(simbol * lenght_sq)
        return None


square_filling(10, '*', False)