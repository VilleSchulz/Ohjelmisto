'''def tervehdi(tervehdys, kerrat):# kerrat = parametrimuuttujat
    for i in range(kerrat):
        print (tervehdys + " " + str(i+1) + ". kerran")
    return

print("päivä alkaa tervehdyksillä")
tervehdi("Moi", 3)
tervehdi("Hyvää päivää", 2)'''
'''

def printtaa_summa(x, y):
    print(x + y)
    return

#funktiolle voi välittää useampia argumentteja
printtaa_summa(5, 8)
#tämä funktio ei palauta mitään
def summa(x, y):
    yht= x+ y
    return
tulos = summa(5, 8)
print(tulos)
'''

def tietoja( nimi, ikä, harrastus):
    tervehdys= f'Terve {nimi}. Ikäsi on: {ikä} ja suosikki harrastuksesi on {harrastus}'
    return tervehdys

henkilö = tietoja('Ville', '32', 'nukkuminen')
print(henkilö)

#Parametrien välittäminen svainsanojen avulla.
#Ohjelmoija voi antaa parametrien arvo( nimi = arvo)- pareina
#Parametreille voi antaa funktion määrityksessä myös oletusarvot
henkilö2 = tietoja(nimi="pekka", ikä=22, harrastus="Kävely")
print(henkilö2)
''''''

#Mitä jos en tiedä jotain argumenttia, miten voi kutsua funktiota???

def tietoja2(nimi, ikä, harrastus):
    tervehdys2= f'Terve{nimi} ja suosikkiharrastukseni on {harrastus}'
    return tervehdys2
henkilö3= (tietoja2("pekka", 33))
print(henkilö3)