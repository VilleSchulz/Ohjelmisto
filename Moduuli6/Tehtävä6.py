'''Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan
halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota'''

import math
def pizzalaskuri(pizza_size2, pizza_price2):
    pizza_value_list = []
    for i in range(2):
        area = math.pi * (pizza_size2[i]/2)**2/10000# laskee pinta-alan senttimetreistä ja tekee samalla muunnokset neliömetreiksi
        pizza_value = pizza_price2[i]/area  # laskee pitsan neliöhinnan
        pizza_value_list.append(pizza_value) # lisää neliöhinnan listaan

    return pizza_value_list



pizza_size = []
pizza_price = []
for i in range(2):
    size_input = float(input(f"Anna pizzan {i+1}. halkaisija senttimetreinä: "))
    pizza_size.append(size_input)
    price_input = float(input(f"Anna pizzan {i + 1}. hinta: "))
    pizza_price.append(price_input)

pizza_menu = pizzalaskuri(pizza_size, pizza_price)

for i, hinta in enumerate(pizza_menu, start=1):
    print(f'{i}. pizzan hinta on: {hinta:.2f} €/m2')
#print(f'Ensimmäisen pizzan hinta on: {pizza_menu[0]:.2f}')
#print(f'Toisen pizzan hinta on: {pizza_menu[1]:.2f}')


