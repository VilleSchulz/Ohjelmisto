'''Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit
 siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille
h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta
kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai
alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin
ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.'''


class Hissi:
    def __init__(self,alinkerros,ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros

    def siirry_kerrokseen(self,kerros):
        self.kerros = kerros
        while self.kerros != kerros:
            if kerros < self.kerros:
                self.kerros_ylös(kerros)

    def kerros_ylös(self,kerros):
        self.kerros =+ kerros
        print(f"Olet kerroksessa{kerros}")
    def kerros_alas(self,kerros):
        self.kerros = kerros =- 1
        print(f"Olet kerroksessa{kerros}")


hissi1 = Hissi(1,50)
hissi1.siirry_kerrokseen(3)
