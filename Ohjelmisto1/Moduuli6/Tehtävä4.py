'''Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
 Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.'''

def laskuri(summarum):
    result =sum(summarum)
    return result


numero_list = []
lista = input("Anna lukuja:")

while lista != "":
    numero_list.append(int(lista))
    lista = input("Anna lukuja:")
else:
    lista == ""
    print(f'Summa on: {laskuri(numero_list)}')