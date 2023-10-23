'''Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua
matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion
tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun
matkan lukemaan 2090 km.'''


class Auto():
    def __init__(self,register,top_speed,speed = 0, km_amount = 0):
        self.register = register
        self.top_speed = top_speed
        self.speed = speed
        self.km_amount = km_amount



    def auto_info(self):
        print(f'Auton infot:\nRekisteritunnus:{self.register}\n'
              f'Huippunopeus: {self.top_speed}\n'
              f'Tämän hetkinen nopeus: {self.speed} km/h\n'
              f'Ajettu kilometrimäärä: {self.km_amount} km')
    def kiihdytä(self, difference):
        if self.speed + difference > self.top_speed:
            self.speed = self.top_speed
        elif self.speed + difference < 0:
            self.speed = 0
        else:
            self.speed += difference

    def auto_kulje(self,time):
        self.km_amount = self.km_amount + (time * self.speed)

car1 = Auto("ABC-123", 142,60,2000)


print(car1.auto_info())
car1.auto_kulje(1.5)
print(car1.auto_info())
#print(f'{car1.speed} km/h')

