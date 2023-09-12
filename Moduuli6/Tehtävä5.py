''''Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että
 karsitun listan.'''



def laskuri(summarum):
    num = 0
    while (num < len(summarum)):
        # Cecking condition
        if summarum[num] % 2 == 0:
           result = summarum[num]
        # increment num
        num += 1
    return result

numero_list = []
lista = input("Anna lukuja:") # kysyy listaan lisättäviä numeroita

while lista != "":
    numero_list.append(int(lista)) # lisää listaan numeron
    lista = input("Anna lukuja:")
else:
    print(f'Alkuperäinen lista:{numero_list}')
    print(f'Parilliset numerot: {laskuri(numero_list)}')
