
#1
import re
num = input()
if num[0].isalpha() and num [1].isdigit():
    car = re.findall(r"\b[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b", num)
    print(f'Номер {num} - легковой')
if num[0].isalpha() and num[1].isalpha():
    taxi = re.findall(r"\b[АВЕКМНОРСТУХ]{2}\d{2,3}\b", num)
    print(f'Номер {num} - легковой')

