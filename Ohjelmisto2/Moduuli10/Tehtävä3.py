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
        print(f"Olet kerroksessa{self.alinkerros}")
    def kerros_alas(self):
        self.alinkerros += -1
        print(f"Olet kerroksessa{self.alinkerros}")

talo1 = Talo(1,10, 2)
talo1.aja_hissiä(1,5)
talo1.palohälytys()
