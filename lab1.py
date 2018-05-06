def input_data():
    value = input()
    return value


def operations():
    print('Введите число или текст:')
    a=input_data()
    y = 'y'
    while y == 'y':
        b=input_operand()
        print('Введите число или текст:')
        c = input_data()
        a,c,check_text = validator(a,c)

        if check_text == 2:
            if b == '+':
                a = a+c

        if check_text == 1:
            if b == '+':
                a = a+c
            elif b == '-':
                a = a-c
            elif b == '*':
                a = a*c
            elif b == '/':
                a = a/c

        if check_text == 0:
            if b == '*':
                a = a*c


        print(a)
        print('Продолжить операцию? Введите "y" если да')
        y=input()

def validator(a,c):
    ok='ne ok'
    check_text=-1
    while ok!='ok':
        a, c, check_text = convertor(a, c)
        if type(a) == str and type(c) == float:
            c = warning(4)
        elif  type(c) == str and type(a) == float:
            a = warning(3)
        elif  type(c) == str and type(a) == int:
            ok = 'ok'
        elif  type(a) == str and type(c) == int:
            ok = 'ok'
        elif  type(c) == str and type(a) == str:
            check_text = 2
            ok = 'ok'
        else: ok='ok'

    return a,c, check_text
def convertor(a,c):
    n=0
    try:
        a = float(a)
        if a % 1 == 0:
            a = int(a)
    except ValueError:
        n+=1
    try:
        c = float(c)
        if c % 1 == 0:
            c = int(c)
    except ValueError:
        n+=1
    if n!=0:
        check_text = warning(n)
    else: check_text = 1
    return a,c,check_text


def warning(test):
    if test==1:
        print('Для символов И числа недоступны операции + , - и /')
        text = 0
        return text
    if test==2:
        print('Для символов  недоступны операции * , - и /')
        text = 0
        return text
    if test == 3:
        print('Первое число должно быть целым')
        a = input_data()
        return a
    if test==4:
        print('Второе число должно быть целым')
        c = input_data()
        return c


def error_message(name_of_function):
    if name_of_function=='input_operand':
        print('Вы ввели не операнд')
        b = input_operand()
        return b


def input_operand():
    print('Введите операнд:')
    b=input()
    if b == '+' or b =='-' or b =='*' or b =='/':
        return b
    else:
        return error_message('input_operand')

if __name__ == "__main__":
    operations()
