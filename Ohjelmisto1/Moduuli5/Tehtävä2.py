'''Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
 Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan
 alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True. '''


num_list = []
run = True
while run:
    user_input = input("Anna luku: ")
    if user_input != "":
        num_list.append(int(user_input))  # muutetaan string floatiksi ja lisätään listaanv
    else:
        run = False


num_list.sort(reverse = True) # Järjestetään nousevaan järjestykseen luvut

result = num_list[:5]
print(f'Tässä viisi suurinta numeroa suuruus järjestyksessä:{result}')

#vaihtoehto printtaukselle
for i in range(5):
    print(num_list[i])
'''
num_list = []

while True:
    user_input = input("Anna luku: ")
    if user_input == "":
        break
    elif user_input != "":
        num = float(user_input) # muutetaan string floatiksi
        num_list.append(num)

num_list.sort(reverse = True) # Järjestetään nousevaan järjestykseen luvut

result = num_list[:5]
print(f'Tässä viisi suurinta numeroa suuruus järjestyksessä:{result}')
'''
'''
# Toinen tapa
num_list = []

while True:
    user_input = input("Anna luku: ")
    if user_input == "":
        break
    try:
        num = float(user_input) # muutetaan string floatiksi
        num_list.append(num)
    except ValueError:
        print("Virheellinen syöte. Syötä kelvollinen luku.")

num_list.sort(reverse = True) # Järjestetään nousevaan järjestykseen luvut

result = num_list[:5]
print(f'Tässä viisi suurinta numeroa suuruus järjestyksessä:{result}')
'''