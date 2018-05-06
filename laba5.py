from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

xspam_dict={}
def parsing_of_file():
    masFrom=[]
    with open('email.txt','r') as file:
        for line in file:
            l=str.find(line,"From:")
            if l==0:
                buf=line.split(' ')
                buf=buf[1].split('\n')
                masFrom.append(buf[0])
            k=str.find(line,"X-DSPAM-Confidence:")
            if k==0 and xspam_dict.get(buf[0])==None:
                buf_of_xspam=line.split(' ')
                xspam_dict[buf[0]]=(float(buf_of_xspam[1]))
            elif k==0 and xspam_dict.get(buf[0])!=None:
                buf_of_xspam=line.split(' ')
                buffer = xspam_dict.get(buf[0])
                xspam_dict[buf[0]]= (float(buf_of_xspam[1]))+buffer
    return masFrom,xspam_dict
def create_new_massives(masFrom):
    buf = Counter(masFrom)
    dict_buf = dict(buf)
    list_buf = list(buf)
    return dict_buf,list_buf
def parsing_of_massives(dict_buf,list_buf):
    masKey, masValue, masXspam=[],[],[]
    for element in list_buf:
        masKey.append(element)
        masValue.append(dict_buf[element])
        masXspam.append(xspam_dict[element]/dict_buf[element])
    return masKey,masValue,masXspam
def drawing_of_graphics(masKey,masValue,masXspam):
    print(masKey[1],masXspam[1])
    plt.title('Количество писем')
    # plt.bar(masKey,masValue, align='center')
    plt.bar(masKey,masValue,1, align='center')
    plt.xticks(fontsize='6', rotation=90)
    plt.savefig("1.png",figsize=(10, 6))
    plt.show()

    plt.title('Средний показатель спама по каждому отправителю')
    plt.bar(masKey,masXspam, align='center')
    plt.xticks(fontsize='6', rotation=90)
    plt.savefig("2.png",figsize=(10, 6))

    plt.show()
def main():
    masFrom, xspam_dict = parsing_of_file()
    dict_buf, list_buf=create_new_massives(masFrom)
    masKey, masValue, masXspam=parsing_of_massives(dict_buf,list_buf)
    drawing_of_graphics(masKey, masValue, masXspam)
if __name__ == "__main__":
    main()