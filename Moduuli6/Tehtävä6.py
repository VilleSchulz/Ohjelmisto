'''Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan
halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.'''

import math
def pizzalaskuri(pizza_size2, pizza_price2):
    pizza_value_list = []
    for i in range(2):
        area = pizza_size2[i]
        pizza_value = pizza_price2[i]/pizza_size2[i/100]
        pizza_value_list.append(pizza_value)

    return pizza_value_list

pizza_size = []
pizza_price = []
for i in range(2):
    size_input = float(input(f"Anna pizzan {i+1}. halkaisija senttimetreinä: "))
    pizza_size.append(size_input)
    price_input= float(input(f"Anna pizzan {i + 1}. hinta: "))
    pizza_price.append(price_input)

print(f'{pizzalaskuri(pizza_size, pizza_price):.2f}€/m')



