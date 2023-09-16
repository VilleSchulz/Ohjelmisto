''''Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että
 karsitun listan.'''



def laskuri(calc):
    even_num = [x for x in calc if x % 2 == 0]
    return even_num

numero_list = []
lista = input("Anna lukuja:") # kysyy listaan lisättäviä numeroita

while lista != "":
    numero_list.append(int(lista)) # lisää listaan numeron
    lista = input("Anna lukuja:")
else:
    print(f'Alkuperäinen lista:{numero_list}')
    print(f'Parilliset numerot: {laskuri(numero_list)}')
