#Kysyy lukua niin pitkään ennen kuin käyttäjä syöttää tyhjän merkkijonon

'''
while True:
    luku=input('Anna luku:')
    if luku!="":
        continue
    else:
        break
'''
print('Ohjelma tulostaa saaduista luvuista pienimmän ja suurimman')
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

print(f'''
{min(merkkijen_jono)} - on pienin sinun luvuista
{max(merkkijen_jono)} - on isoin sinun luvuista ''')


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



