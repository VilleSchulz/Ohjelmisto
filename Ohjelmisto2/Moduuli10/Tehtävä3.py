'''Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki
hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

'''


class Talo:


    def __init__(self,alinkerros,ylinkerros,hissienlkm):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissienlkm = hissienlkm
        self.hissit = []
        for i in range(hissienlkm):
            self.hissit.append(Hissi(alinkerros, ylinkerros))

    def aja_hissiä(self,hissin_nro,kohdekerros):

        self.kohdekerros = kohdekerros
        self.hissit[hissin_nro - 1].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for i in range(self.hissienlkm):
            self.hissit[i].siirry_kerrokseen(1)


class Hissi:

    def __init__(self,alinkerros,ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros




    def siirry_kerrokseen(self,kohdekerros):
        while self.alinkerros != kohdekerros:
            if kohdekerros > self.alinkerros:
                self.kerros_ylös()
            elif kohdekerros < self.alinkerros:
                self.kerros_alas()



    def kerros_ylös(self):
        self.alinkerros += 1
        print(f"You are in floor: {self.alinkerros}")
    def kerros_alas(self):
        self.alinkerros += -1
        print(f"You are in floor: {self.alinkerros}")
talo1 = Talo(1,0,0)


talo1.ylinkerros = int(input("Give the highest floor the elevator goes to\n"))
talo1.hissienlkm = int(input("Give the amount of elevators\n"))
hissin_nro,kohdekerros = map(int,input("Give the elevator number and floor number where you want to go (Example: 1,1)\n").split(","))

talo1.aja_hissiä(hissin_nro,kohdekerros)
'''talo1 = Talo(1,10, 2)
talo1.aja_hissiä(1,5)
talo1.palohälytys()'''
