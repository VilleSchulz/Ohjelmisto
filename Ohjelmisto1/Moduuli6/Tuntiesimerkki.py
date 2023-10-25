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
print(henkilö3)'''


'''
def print_city(city3):
    #lokaali muuttuja, arvo käytössä vain funktion sisällä (local scope)
    city = "Helsinki" #globaali muuttuja korvataan lokaalilla
    city2 = 'Vantaa'
    print(city)
    print(city2)
    print(city3)
    #myös funktion parametrina esitelty on lokaali
def print_city2():
    print(city)

#globaali muuttuja, arvo käytössä koko ohjelman laajuisesti (global scope)
#
city = "Espoo"
print_city("Vantaa")
print(city)
print_city2()
print_city("Vihti")
'''
#print sum funktio itsetehtynä
'''def list_sum(nums):
    print('lasketaan alla olevien alkioiden summa')
    print(nums)
    result = 0
    for num in nums:
        result = result + num
    return result
numbers = [1, 2, 3, 4, 6, 7]
print(list_sum(numbers))
numbers_sum = list_sum(numbers)
print(numbers_sum)
'''
'''def list_reset(nums):
    print('nollataan kaikki lista alkiot')
    print(nums)
    nums = nums.copy() # listasta voidaan luoda uusi kopio .copy() - metodilla
    for i in range(5):
       nums[i] = 0
    return nums
numbers = [1, 2, 3, 4, 6, 7]
numbers2 = 
print(list_reset(numbers))
print(numbers)#myös alkuperäinen lista muuttunut, koska funktiolle on syötetty parametrina viittaus
'''
#Vaihtuvan mittaiset argumenttijonot. ARgumentteja coidaan antaa kutsukerrasta toiseen
# vaihteleva määrä. Funktio voi käsitellä saadut arvot listana.

def numbers_to_tuple(*nums):
       return nums
print(numbers_to_tuple(5,6,7))

# monikko eli tuple, "kuin"  lista jota ei voi muokata
numbers
