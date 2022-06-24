# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

f = open("CAM_table.txt")
data = []

for line in f:
    if "DYNAMIC" in line:
        ld = line.split()
        ld[0] = int(ld[0])
        data.append(ld)
        #str = "{:<10}{:<20}{:<10}".format(ld[0], ld[1], ld[3])
data = sorted(data)
"""for ld in data:
    str = "{:<10}{:<20}{:<10}".format(ld[0], ld[1], ld[3])
    #print(str)"""

n = input("Введите Vlan:")
n = int(n)
for line in data:
    if line[0] == n:
        str = "{:<10}{:<20}{:<10}".format(line[0], line[1], line[3])
        print(str)