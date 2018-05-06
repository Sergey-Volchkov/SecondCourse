import numpy as np
from matplotlib import pyplot as plt
def moving_average(data, smaPeriod=3):
    j = next(i for i, x in enumerate(data) if x is not None)
    our_range = range(len(data))[j + smaPeriod - 1:]
    empty_list = [None] * (j + smaPeriod - 1)
    sub_result = [np.mean(data[i - smaPeriod + 1: i + 1]) for i in our_range]

    return np.array(empty_list + sub_result)
def input_len():
    print('Сколько данных вы собираетесь ввести? Не менее 25')
    try:
        l=int(input())
        if l<25:
            print('Длина должна быть не меньше 25!')
            return input_len()
        else:
            return l
    except:
        print('Вы ввели неверную длину')
        return input_len()
def input_size():
    print('Сколько последних значений вы хотите видеть на графике?')
    try:
        l=int(input())
        if l<25:
            print('Длина должна быть не меньше 25!')
            return input_size()
        else:
            return l
    except:
        print('Вы ввели неверную длину')
        return input_len()

def feel_mas():
    l=input_len()
    x=[]
    print(l,x)
    while len(x)<l:
        try:
            print('Введите число')
            x.append(float(input()))
        except:
            print('Ошибка.Введите число')
    return x
def draw_graphic(y):
    size = input_size()
    smay=moving_average(y)
    smay = smay[(len(y)-size):]
    y = y[(len(y)-size):]
    x = np.arange(1, len(y) + 1)
    smax = np.arange(1, len(smay) + 1)

    plt.title('Cкользящая средняя')
    plt.plot(x, y, label ='Простые значения')
    plt.legend()
    plt.show()
    plt.plot(smax,smay,x, y, label='SMA',)
    plt.legend()
    plt.show()
def main():
    data=[1,6,10,4,20,20,40,9,15,63,23,12,12,43,532,60,21,43,12,23,43,15,15,1,6,0]
    draw_graphic(data)
if __name__ == "__main__":
    main()
