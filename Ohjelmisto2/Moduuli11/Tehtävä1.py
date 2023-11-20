'''Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat
alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa
julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien
julkaisujen kaikki tiedot toteuttamiesi metodien avulla.'''


class Julkaisu:
    def __init__(self,name):
        self.name = name


class Kirja(Julkaisu):
    def __init__(self,name, writer,pages):
        super().__init__(name)
        self.writer = writer
        self.pages = pages
    def tulosta_tiedot(self):
        print(f"Kirjan nimi:{self.name}, \n"
              f"kirjan kirjoittoja: {self.writer} ja sivumäärä on {self.pages}")
class Lehti(Julkaisu):
    def __init__(self,name,päätoimittaja):
        super().__init__(name)
        self.päätoimittaja = päätoimittaja
    def tulosta_tiedot(self):
        print(f"Lehden nimi on: {self.name} ja päätoimittaja on {self.päätoimittaja}")

lehti1 = Lehti("Aku-Ankka","Aki Hyyppä")
kirja1 = Kirja("Hytti n:o 6","Rosa Liksom",200)

kirja1.tulosta_tiedot()
lehti1.tulosta_tiedot()


