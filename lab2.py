def input_data():
    print('Введите число, корень которого хотите найти')
    a = float(input())
    return a
def operations():
    a= input_data() #число корень которого хотим найти
    b=0.0000001 #просто начальный корень с которого начинаем считать
    c=None
    while b!=c:
        try:
            c = b
            b=1/2*(b+a/b)
        except ZeroDivisionError:
            print('нельзя найти корень из 0')
    return c
if __name__ == "__main__":
    print(operations())
