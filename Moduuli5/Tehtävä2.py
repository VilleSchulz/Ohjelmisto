'''Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
 Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan
 alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True. '''

num = int(input("Anna luku: "))
num_list= []
for i in num_list:
    num_list.append(num)
    if str(num) == "":
        break
num_list.sort(reversed(max,4))
print(f'Tässä viisi suurinta numeroa suuruus järjestyksessä: ')