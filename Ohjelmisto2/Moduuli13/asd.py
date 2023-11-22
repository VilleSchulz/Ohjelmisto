'''Aloitetaan pohtimalla sitä, mitä koirahoitolan toteuttamiseksi vaaditaan.
Ensinnäkin koirahoitola kannattaa toteuttaa omana luokkanaan. Hoitolan toiminnallisuus ei liity mitenkään yksittäiseen
koiraan, eikä sitä tule kirjoittaa Koira-luokan sisään. Kirjoitamme siis ohjelmaan toisen luokan nimeltä Hoitola.
Sitten pohdimme, mitä ominaisuuksia koirahoitolalla on. Huomaamme, että hoitolan täytyy olla tietoinen siitä, mitä
koiria siellä kulloinkin on hoidossa. Sen voimme toteuttaa listan avulla: liitetään hoitolan ominaisuudeksi lista,
onka alkiot ovat koiria.Entä onko hoitolalla toimintoja, jotka on syytä kirjoittaa metodeiksi? Äsken tehdystä hoitolan
määrittelystä tunnistetaan, että koirahoitolalle kannattaa laatia kolme metodia:koiran kirjaaminen sisään hoitolaan
koiran kirjaaminen ulos hoitolastakierroksen tekeminen hoitolassa.'''


class Koira:
    def __init__(self,nimi,syntymävuosi,haukahdus="vuh vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def tervehdi(self):
        print(f'{self.haukahdus}')

class Hoitola:
    def __init__(self):
        self.koirat = []

    def kirjaa_sisään(self,koira):
        print(f'Tervetuloa hoitoon {koira.nimi}')
        koira.tervehdi()
        self.koirat.append(koira)
    def kirjaa_ulos(self,koira):
        self.koirat.remove(koira)
        print(f'Tervemenoa {koira.nimi}')
        koira.tervehdi()

    def tee_hoitolakierros(self):
        print(f'koiria on {len(self.koirat)}')
        for i in self.koirat:
            print(f'{i.nimi}:llä on kaikki hyvin')
            i.tervehdi()


hoitola1 = Hoitola()
koira1= Koira('kurre',1992,"krr krr")
koira2 = Koira('palle',1992,"wuhuuuwhuu")
koira3 = Koira('Myy',2000,"tik tik")
hoitola1.kirjaa_sisään(koira1)
hoitola1.kirjaa_sisään(koira2)
hoitola1.kirjaa_sisään(koira3)
hoitola1.tee_hoitolakierros()





