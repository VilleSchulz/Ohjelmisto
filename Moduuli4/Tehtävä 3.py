#Kysyy lukua niin pitkään ennen kuin käyttäjä syöttää tyhjän merkkijonon

'''
while True:
    luku=input('Anna luku:')
    if luku!="":
        continue
    else:
        break
'''
luku = 0
while luku!='':
    luku = input('Anna luku: ')


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



