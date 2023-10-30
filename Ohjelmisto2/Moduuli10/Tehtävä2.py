'''Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja
ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien
lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja
kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.'''




class Talo:
    def __init__(self,alinkerros,ylinkerros,hissienlkm):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissienlmk = hissienlkm
        self.hissit = []
        for i in range(self.hissienlmk):
            self.hissit.append(Hissi(alinkerros, ylinkerros))

    def aja_hissiä(self,hissin_nro,kohdekerros):
        self.hissit[hissin_nro-1] = hissin_nro
        self.kohdekerros = kohdekerros
        self.hissit[hissin_nro].siirry_kerrokseen(kohdekerros)



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
        while self.alinkerros != 1:
             if self.alinkerros > 1:
                 self.kerros_alas()

    def kerros_ylös(self):
        self.alinkerros += 1
        print(f"Olet kerroksessa{self.alinkerros}")
    def kerros_alas(self):
        self.alinkerros += -1
        print(f"Olet kerroksessa{self.alinkerros}")

talo1 = Talo(1,10, 2)
talo1.aja_hissiä(1,5)

