# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

ignore = ["duplex", "alias", "configuration"]

#filename = ''
#input(filename)
n = 0;
f = open("config_sw1.txt")
f2 = open("config_sw2.txt", 'w')

string = f.readline()
for line in f:
    if line[0] != "!":
        for ignore_word in ignore:
            if ignore_word in line:
                n = n+1
        if n == 0:
                #print(line.strip("\n"))
                f2.write(line)
        n = 0
f2.close()