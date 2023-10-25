'''Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan
 vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on
 tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.'''
def laskuri(litra):
   litra =  litra * 3.785
   return litra
bensin = 0
while bensin >= 0:
    bensin = float(input("Anna bensiinin määrä gallonoina: "))
    print(f'Bensiinin määrä litroina: {laskuri(bensin):.2f}')
else:
    print("Annoit negatiivisen luvun")