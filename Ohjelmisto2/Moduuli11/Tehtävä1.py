'''Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat
alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa
julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien
julkaisujen kaikki tiedot toteuttamiesi metodien avulla.'''

class Julkaisu:
    def __init__(self,name):


class Kirja(Julkaisu):
    def __init__(self,writer,pages):
        self.writer = writer
        self.pages = pages
    def tulosta_tiedot(self):
        print(f"Kirjan nimi:{super().__init__(name)}, \n"
              f"kirjan kirjoittoja: {self.writer} ja sivumäärä on {self.pages}")
class Lehti(Julkaisu):
    def __init__(self,päätoimittaja):
        self.päätoimittaja = päätoimittaja
    def tulosta_tiedot(self):
        print(f"Lehden nimi on: {super()__init__(name)} ja päätoimittaja on {self.päätoimittaja}")

