'''Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
 Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. 
 Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, 
 että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. 
 Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse 
 vielä päivittää.'''


class Car():
    def __init__(self,register,top_speed,speed = 0, km_amount = 0):
        self.register = register
        self.top_speed = top_speed
        self.speed = speed
        self.km_amount = km_amount



    def car_info(self):
        print(f'Auton infot:\nRekisteritunnus:{self.register}\n'
              f'Huippunopeus: {self.top_speed}\n'
              f'Tämän hetkinen nopeus: {self.speed} km/h\n'
              f'Ajettu kilometrimäärä: {self.km_amount} km')
    def acceleration(self,difference):
        if self.speed + difference > self.top_speed:
            self.speed = self.top_speed
        elif self.speed + difference < 0:
            self.speed = 0
        else:
            self.speed += difference







car1 = Car("123-ABC",142)
car1.car_info()
car1.acceleration(30)
car1.car_info()
car1.acceleration(70)
car1.car_info()
car1.acceleration(50)
car1.car_info()
car1.acceleration(-200)
car1.car_info()
print(f'{car1.speed} km/h')

