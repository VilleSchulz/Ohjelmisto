'''Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
 (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina
 monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on
 ensimmäinen talvikuukausi.'''

months = ("tammmikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
seasons = ("talvi", "kevät", "kesä", "syksy" )
month_num = int(input("Anna kuukauden numero: "))

if 1 <= month_num <= 12:
    if month_num == 12 or month_num == 1 or month_num == 2: # Jos kuukauden numero on 12 1 tai 2 niin kuukauden i on 0 jolloin se on automaattisesti talvi
        season = 0
    else:
        season = month_num // 3 # tässä jaetaan kuukaden järjestynumero 3 jolloin saadaan season listan indeksi arvo

    print(f'Kuukausi {months[month_num-1]} kuuluu vuodenaikaan {seasons[season]}')

else:
    print("Väärä kuukauden arvo")




