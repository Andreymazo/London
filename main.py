#!/usr/bin/env python3

a = input('Введите имя устройства:')
#b = input('Введите имя параметра:')
b = input('Введите имя параметра (ios, model, vendor, location, ip)')

def london(a):
    london_co = {
            "r1": {"location": "21 New Globe Walk",
                     "vendor": "Cisco",
                      "model": "4451",
                        "ios": "15.4",
                         "ip": "10.255.0.1"
                                                },
            "r2": {
                   "location": "21 New Globe Walk",
                     "vendor": "Cisco",
                      "model": "4451",
                        "ios": "15.4",
                         "ip": "10.255.0.2"
                                                },
            "sw1": {
                   "location": "21 New Globe Walk",
                     "vendor": "Cisco",
                      "model": "3850",
                        "ios": "3.6.XE",
                         "ip": "10.255.0.101",
                      "vlans": "10,20,30",
                    "routing": True
                                                }
                                                      }

    if a == 'r1':
        #print(london_co['r1'])
        if b == "location":
            print(london_co['r1']['location'])
        if b == "vendor":
            print(london_co['r1']['vendor'])
        if b == "model":
            print(london_co['r1']['model'])
        if b == "ios":
            print(london_co['r1']['ios'])
        if b == "ip":
            print(london_co['r1']['ip'])
        else:
            print('Такого параметра нет')
    if a == 'r2':
        #print(london_co['r2'])
        if b == "location":
            print(london_co['r2']['location'])
        if b == "vendor":
            print(london_co['r2']['vendor'])
        if b == "model":
            print(london_co['r2']['model'])
        if b == "ios":
            print(london_co['r2']['ios'])
        if b == "ip":
            print(london_co['r2']['ip'])
        else:
            print('Такого параметра нет')
    if a == 'sw1':
        #print(london_co['sw1'])
        if b == "location":
            print(london_co['sw1']['location'])
        if b == "vendor":
            print(london_co['sw1']['vendor'])
        if b == "model":
            print(london_co['sw1']['model'])
        if b == "ios":
            print(london_co['sw1']['ios'])
        if b == "ip":
            print(london_co['sw1']['ip'])
        if b == "ios":
            print(london_co['sw1']['ios'])
        if b == "ip":
            print(london_co['sw1']['ip'])
    else:
            print('Такого параметра нет')

london(a)

