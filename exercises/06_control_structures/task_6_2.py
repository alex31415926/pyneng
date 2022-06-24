# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

user_ip = input("Введите ip:")
ip = user_ip.split(".")
oct1, oct2, oct3, oct4 = int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])


if oct1 > 0 and oct1 < 224:
    print('unicast')
elif oct1 > 223 and oct1 < 240:
    print('multicast')
elif oct1 == 255 and oct2 == 255 and oct3 == 255 and oct4 == 255:
    print('local broadcast')
elif oct1 == 0 and oct2 == 0 and oct3 == 0 and oct4 == 0:
    print('unassigned')
else:
    print('unused')
