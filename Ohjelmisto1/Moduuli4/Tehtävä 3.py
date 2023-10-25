#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

print('Ohjelma tulostaa saaduista luvuista pienimmän ja suurimman')
print('Jos annat jotain paitsi lukua - ohjelma lopettaa toimintansa \n')
merkkien_jono = []
luku = 0

while True:
    # kysyy käyttäjältä lukua
    luku = input('Anna luku:')
    # jos luku on erisuuri kuin tyhjä niin se listään listaan
    if luku != "":
        luku2 = int(luku)
        merkkien_jono.append(luku2)
    #jos luku on yhtäsuuri kuin "" ohjelma lopetetaan
        if luku == "":
        break


print(f'{min(merkkien_jono)}: on pienin sinun luvuista \
{max(merkkien_jono)}: on isoin sinun luvuista ')






'''print('Ohjelma tulostaa saaduista luvuista pienimmän ja suurimman')
print('Jos annat jotain paitsi lukua - ohjelma lopettaa toimintansa \n')

var = input('Anna joku luku: ')

# merkkien jono lataan "[...]"
merkkijen_jono = []

while True:
    try:
        float(var)
        # append = lisays
        merkkijen_jono.append(var)
        var = input('Anna seurava luku: ')
    except Exception:
        break

print(f'{min[merkkijen_jono]} - on pienin sinun luvuista\
{max[merkkijen_jono]} -on isoin sinun luvuista ')

'''
'''Joelin tapa tehdä(itselle muistiin ):
num_list = []

while True:
    user_input = input("Anna luku: ")
    if user_input != "":
        num_list.append(int(user_input))
        continue
    else:
        break

print("Pienin luku: " + str(min(num_list)))
print("Suurin luku: " + str(max(num_list)))'''



