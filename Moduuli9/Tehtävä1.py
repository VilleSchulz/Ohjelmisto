'''Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu
matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot uuden
auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen
luodun auton kaikki ominaisuudet.'''


class Car():
    def __init__(self,register,top_speed):
        self.register = register
        self.top_speed = top_speed
        self.speed = 0
        self.km_amount = 0

    def car_info(self):
        print(f'Auton infot:\nRekisteritunnus:{self.register}\n'
              f'Huippunopeus: {self.top_speed}\n'
              f'Tämän hetkinen nopeus: {self.speed}\n'
              f'Ajettu kilometrimäärä: {self.km_amount}')



car1 = Car("123-ABC","142 km/h")
car1.car_info()