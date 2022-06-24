# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

f = open("ospf.txt")
filedata = f.readlines()
#print(f.readlines())

text = ["Prefix", "AD/Metric", "Next-Hop", "Last update", "Outbound Interface"]
for string in filedata:
    string = string.strip()
    interface_data = string.split()
    str1 = "{:<22} {}".format(text[0], interface_data[1])
    str2 = "{:<22} {}".format(text[1], interface_data[2].strip("[]"))
    str3 = "{:<22} {}".format(text[2], interface_data[4].strip(","))
    str4 = "{:<22} {}".format(text[3], interface_data[5].strip(","))
    str5 = "{:<22} {}".format(text[4], interface_data[6])
    print(str1)
    print(str2)
    print(str3)
    print(str4)
    print(str5)
    #print("\n")
