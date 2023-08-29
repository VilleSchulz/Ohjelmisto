user = 0
pword = 0
while user!='python' and pword!='rules':
    user = input("Anna käyttäjätunnus: ")
    pword = input('Anna salanasi: ')
    if user!='python' and pword!='rules':
        print('Pääsy evätty')
else:
    print('Tervetuloa')

