'''Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman
alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan
100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun
aikana tehdään tunnin välein seuraavat toimenpiteet:Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos
arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan
kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.'''
import random


class Auto():
    def __init__(self,register,top_speed,speed = 0, km_amount = 0):
        self.register = register
        self.top_speed = top_speed
        self.speed = speed
        self.km_amount = km_amount



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










