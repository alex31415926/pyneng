# -*- coding: utf-8 -*-
import pprint
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    access_list = {}
    trunk_list = {}
    with open(config_filename, 'r') as file:
        for line in file:
            #print(line.rstrip())
            if line.startswith("interface"):
                intf = line.split()[1]
                #print(intf)
            if line.startswith(" switchport access vlan"):
                access_list[intf] = int(line.split()[3])
            if line.startswith(" switchport trunk allowed vlan"):
                trunk_list[intf] = list(map(int, line.split()[4].split(",")))

    pprint.pprint(access_list, trunk_list)
    return access_list, trunk_list




get_int_vlan_map("config_sw1.txt")