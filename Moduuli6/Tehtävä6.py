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



'''python
Copy code
import math

def laske_yksikkohinta(halkaisija, hinta):
    pinta_ala = math.pi * (halkaisija / 2) ** 2  # Lasketaan pizzan pinta-ala neliömetreinä
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

def main():
    print("Syötä ensimmäisen pizzan tiedot:")
    halkaisija1 = float(input("Halkaisija (senttimetreinä): "))
    hinta1 = float(input("Hinta (euroina): "))

    print("\nSyötä toisen pizzan tiedot:")
    halkaisija2 = float(input("Halkaisija (senttimetreinä): "))
    hinta2 = float(input("Hinta (euroina): "))

    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    print("\nEnsimmäisen pizzan yksikköhinta: {:.2f} euroa/neliömetri".format(yksikkohinta1))
    print("Toisen pizzan yksikköhinta: {:.2f} euroa/neliömetri".format(yksikkohinta2))

    if yksikkohinta1 < yksikkohinta2:
        print("\nEnsimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta2 < yksikkohinta1:
        print("\nToinen pizza antaa paremman vastineen rahalle.")
    else:
        print("\nMolemmat pizzat ovat samanhintaisia per neliömetri.")

if __name__ == "__main__":
    main().'''