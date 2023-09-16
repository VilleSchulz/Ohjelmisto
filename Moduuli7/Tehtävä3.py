'''Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
 haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee
 uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun,
 ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus
 päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
 (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät
 koodeja helposti selaimen avulla.)'''
airport_list = {"Afutara Airport":"AGAF", "Balalae Airport":"AGGE","Kirakira Airport":"AGGK","Santa Ana Airport":"AGGT"}
run = True
print("Haluatko syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa")
while run:
    input_select = input("kirjoita: syöttö , haku, lopeta: ").lower()
    if input_select == "syöttö":
        key1 = input("Anna lentoaseman nimi: ")
        value1 = input("Anna lentoaseman ICAO- koodi: ")
        airport_list[key1] = value1
    elif input_select == "haku":
        value2 = input("Anna lentoaseman ICAO- koodi: ").upper()
        if value2 in airport_list.values():
            airport_name = [key for key, value in airport_list.items() if value == value2][0]
            print(f"ICAO-koodin {value2} lentoasema: {airport_name}")
    elif input_select == "lopeta":
        run = False



print(airport_list)

