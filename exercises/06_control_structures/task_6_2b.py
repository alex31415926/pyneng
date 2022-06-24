# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

user_ip = input("Введите ip:")
ip = user_ip.split(".")

correct_ip = False

while correct_ip != True
if len(ip) != 4:
    print("Неправильный IP-адрес")

else:

    try:
        oct1, oct2, oct3, oct4 = int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])
    except ValueError:
        print("Неправильный IP-адрес")
    else:
        if oct1 > 255 or oct2 > 255 or oct3 > 255 or oct4 > 255:
            print("Неправильный IP-адрес")


        else:
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