'''Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on ominaisuutena
akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille
alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita
pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h,
32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen
matkamittarilukemat.'''


import random


class Auto():
    def __init__(self,register,top_speed,speed = 0, km_amount = 0,capacity):
        self.register = register
        self.top_speed = top_speed
        self.speed = speed
        self.km_amount = km_amount
        super().__init__(capacity)


class Sähköauto(Auto):
    def __init__(self,capacity,register,top_speed):
        self.capacity = capacity
        super().__init__(register)
        super().__init__(top_speed)



class Polttomoottori(Auto):
    def __init__(self,capacity,register,top_speed):
        self.capacity = capacity
        super().__init__(register)
        super().__init__(top_speed)
    def auto_info(self):
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

while True:
    for car in auto_lista:
        car.kiihdytä(random.randint(-10,15))
        car.auto_kulje(1)
    if any(car.km_amount >= 10000 for car in auto_lista):
            break

print(f'{"Rekisteritunnus ":<16}{"Huippunopeus ":<16}{"Nopeus (km/h)":<16}{"Ajettu km":<16}')
for car in auto_lista:
    info = car.auto_info()
    print(f'{info[0]:<16}{info[1]:<16}{info[2]:<16}{info[3]:<16}')



