'''Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen,
kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo
kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle annetaan
kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla
toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen,
kun kilpailu on päättynyt.'''




import random

class Kilpailu:
    def __init__(self,nimi,kilometrimäärä,autolista):
        self.nimi = nimi
        self.kilometrimäärä = kilometrimäärä
        self.autolista = autolista

    def tunti_kuluu(self):
            while not self.kilpailu_ohi():
                laskuri = 0
                for car in self.autolista:
                    car.kiihdytä(random.randint(-10,15))
                    car.auto_kulje(1)
                    laskuri += 1
                    if laskuri == 10:
                        self.tulosta_tilanne()
                    if self.kilpailu_ohi():
                        print("kilpailu ohi!")
                        self.tulosta_tilanne()
                    elif self.kilpailu_ohi() :
                        print("kilpailu jatkuu")





    def kilpailu_ohi(self):
        return any(car.km_amount >= self.kilometrimäärä for car in self.autolista)


    def tulosta_tilanne(self):
        print(f'{"Rekisteritunnus ":<16}{"Huippunopeus ":<16}{"Nopeus (km/h)":<16}{"Ajettu km":<16}')
        for car in self.autolista:
            print(f'{car.register:<16}{car.top_speed:<16}{car.speed:<16}{car.km_amount:<16}')


class Auto():
    def __init__(self,register,top_speed,speed = 0, km_amount = 0):
        self.register = register
        self.top_speed = top_speed
        self.speed = speed
        self.km_amount = km_amount



    def auto_info(self):
        print(f'{"Rekisteritunnus ":<16}{"Huippunopeus ":<16}{"Nopeus (km/h)":<16}{"Ajettu km":<16}')
        for car in auto_lista:
            print(f'{car.register:<16}{car.top_speed:<16}{car.speed:<16}{car.km_amount:<16}')
        return self.register,self.top_speed, self.speed,self.km_amount
    def kiihdytä(self, difference):
        if self.speed + difference > self.top_speed:
            self.speed = self.top_speed
        elif self.speed + difference < 0:
            self.speed = 0
        else:
            self.speed += difference

    def auto_kulje(self,time):
        self.km_amount = self.km_amount + (time * self.speed)

auto_lista = []
for i in range(10):
    new_car = Auto(f"ABC-{i+1}", random.randint(100,200))
    auto_lista.append(new_car)

'''while True:
    for car in auto_lista:
        car.kiihdytä(random.randint(-10,15))

    if any(car.km_amount >= 10000 for car in auto_lista):
            break'''



kilpailu1 = Kilpailu("Suuri romuralli",8000,auto_lista)

kilpailu1.tunti_kuluu()







