'''Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
 Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan
 alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True. '''

num_list = []

while True:
    user_input = input("Anna luku: ")
    if user_input == "":
        break
    try:
        num = float(user_input)
        num_list.append(num)
    except ValueError:
        print("Virheellinen syöte. Syötä kelvollinen luku.")

num_list.sort(reverse = True)

result = num_list[:5]
print(f'Tässä viisi suurinta numeroa suuruus järjestyksessä:{result}')