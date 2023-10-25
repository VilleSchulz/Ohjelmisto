'''Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.
'''

names = set()


run = True

while run:
    input_name = input("Anna nimi (jos syötät tyhjn merkkijonon kysely loppuu):")
    if input_name != "": # tarkistaa onko syötetty nimi tyhjä, jos on niin lopettaa kyselyn ja ohjelma menee eteenpäin
        if input_name not in names: #testaa onko syötetty nimi jo names listassa
            names.add(input_name)
        else:
            print("Nimi on jo listassa!!")
    else:
        run = False # jos while loopin ehto ei true niin lopettaa
for names in names:
    print(names)

