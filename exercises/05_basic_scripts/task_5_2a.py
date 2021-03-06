# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ipMask = input("Введите IP:")

ipMask = ipMask.split("/")
ip = ipMask[0]
mask = ipMask[1]

ip = ip.split('.')

ipbin = "{:>08b}{:>08b}{:>08b}{:>08b}".format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))
ipNetbin = ipbin[:int(mask)]+ "0" * (32 - int(mask))
oct1 = ipNetbin[:8]
oct2 = ipNetbin[8:16]
oct3 = ipNetbin[16:24]
oct4 = ipNetbin[24:32]

ipNet = [int(oct1, 2), int(oct2, 2), int(oct3, 2), int(oct4, 2)]


#print(ipbin)
#print(ipNetbin)
#print(ipNet)
maskB = "1" * int(mask) + "0" * (32-int(mask))
mask1 = maskB[:8]
mask2 = maskB[8:16]
mask3 = maskB[16:24]
mask4 = maskB[24:32]

mask11 = int(mask1, 2)
mask12 = int(mask2, 2)
mask13 = int(mask3, 2)
mask14 = int(mask4, 2)

ipStr = "{:<10}{:<10}{:<10}{:<10}".format(ipNet[0], ipNet[1], ipNet[2], ipNet[3])
ipStr2 = "{:>08b}  {:>08b}  {:>08b}  {:>08b}  ".format(int(ipNet[0]), int(ipNet[1]), int(ipNet[2]), int(ipNet[3]))

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