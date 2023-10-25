#5.9 esimerkit
name1 = "Ville"
name2 = "viivi"
name3 = "Iines"
age1 = 5.5
age2 = 100
age3 = 1000
print(f'{name1}, ikä :{age1}')
print(f'{name2}, ikä :{age2}')
print(f'{name3}, ikä :{age3}')
names = ["ville", "viivi", "iines", 'jaripetteri', 'juri', 'kukko', 'kana']
ages = [5.5, 6, 38, 88, 20, 2, 2]
# print(f'{names[1]}, ikä :{ages[0]}')
# listan läpikäynti While-loopilla
iterator = 0
while iterator < len(names):
    print(f'{names[iterator]}, ikä :{ages[iterator]}')
    iterator+=1
'''# eri tapoja viitata alkioihin
print(names[2:5])# kolme alkiota alkaen indeksistä 2. Viides ei tulostu
print(names[-1])# -1 viittaa aina viimeseen alkioon
print(names[3:])# kaikki loput alkiot alkaen indeksistä 3
# listan pituus len() funktiolla'''
lenght = len(names)
print(lenght)
'''names.append("Uusi nimi") # lisää nimen
names.remove('iines') # Poistaa nimen
print(names)
names.insert(0, 'iines')# lisää nimen ensimmäiseksi listaan
names.extend(ages)# lisää namesiin ages listan
print(names)
ages2 = names[6:]# tällein saa eroteltua tietyn osan listasta omakseen tai näin ages2 = names[names.index(5.5):]
print(ages2)
print(names.index(5.5))# tällein saa tietoon 5.5 indeksiarvon'''
# newName = input('Anna uusinimi ')
# names.append(newName)
# searchTerm = input('Ketä etsit: ').lower()
# if searchTerm in names:
#    print(f'Löytyy {searchTerm}')
# else:
 #   print(f'Eipä löödy {searchTerm}')
# listan läpikäynti for- silmukalla
for name in names:
    print(f'Nimi: {name}')
# For loopin silmukka iteraattorilla
for i in range (2):
    print(f'Nimi: {names[i]}')

for i in range (len(names)):
    print(f'Nimi: {names[i]}')

# For looppi Range merkillä(joka kolmas numero
for i in range (0, 1000, 3):
    print(i)
for i in range (999, 0, -3):
    print(i)