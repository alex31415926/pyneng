# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ipMask = input("Введите IP:")

ipMask = ipMask.split("/")
ip = ipMask[0]
mask = ipMask[1]

ip = ip.split('.')
maskB = "1" * int(mask) + "0" * (32-int(mask))
mask1 = maskB[:8]
mask2 = maskB[8:16]
mask3 = maskB[16:24]
mask4 = maskB[24:32]

mask11 = int(mask1, 2)
mask12 = int(mask2, 2)
mask13 = int(mask3, 2)
mask14 = int(mask4, 2)

ipStr = "{:<10}{:<10}{:<10}{:<10}".format(ip[0], ip[1], ip[2], ip[3])
ipStr2 = "{:>08b}  {:>08b}  {:>08b}  {:>08b}  ".format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))

print("Network:")
print(ipStr)
print(ipStr2)

print("\nMask:")
print("/"+mask)
maskStr1 = "{:<10}{:<10}{:<10}{:<10}".format(mask11, mask12, mask13, mask14)
maskStr2 = "{:>08b}  {:>08b}  {:>08b}  {:>08b}".format(mask11, mask12, mask13, mask14)
#print(str(mask11)+" "+str(mask12)+" "+str(mask13)+" "+str(mask14))
print(maskStr1)
print(maskStr2)

#print(maskB)

