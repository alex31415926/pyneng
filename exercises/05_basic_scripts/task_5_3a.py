# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

modes = {
    "access": [
        "switchport mode access\n",
        "switchport access vlan {}\n",
        "switchport nonegotiate\n",
        "spanning-tree portfast\n",
        "spanning-tree bpduguard enable\n",
    ],

    "trunk": [
        "switchport trunk encapsulation dot1q\n",
        "switchport mode trunk\n",
        "switchport trunk allowed vlan {}\n",
    ]
}

questions = {
    "access" : "Введите номер VLAN:",
    "trunk" :"Введите разрешенные VLANы:"
}
mode  = input("Введите режим работы интерфейса (access/trunk):")
iface = input("Введите тип и номер интерфейса:") # Fa0/6
vlans = input(questions[mode]) # 3

print("interface " + iface)
string = "".join(modes[mode]).format(vlans)
print(string)