class Eläintarha:
    # eläintarha ja eläin luokkien välill on pysyvä assosiosaatiosuhde
    # yksisuutainen assosiaatio
    # eläintarha tietää mitä eläimiä siellä on mutta eläimet eivät tiedä olevansa tarhassa

    # luokan konstruktori eli alustaja
    def __init__(self, nimi):
        self.nimi = nimi
        self.eläimet = []

    # luokan metodi
    def lisää_eläin(self, eläin):
        self.eläimet.append(eläin)

    def listaa_eläimet(self):
        for i in self.eläimet:
            Eläin.tee_ääni(i)


class Eläin():
    def __init__(self, rotu, ääni):
        self.rotu = rotu
        self.ääni = ääni

    def tee_ääni(self):
        print(f'{self.rotu} {self.ääni}')


Eläintarha1 = Eläintarha('zoo')
eläin1 = Eläin('Leijona', 'Karjuu')
Eläintarha1.lisää_eläin(eläin1)
eläin1.tee_ääni()
eläin2 = Eläin('Kissa', 'Vinkuu')
Eläintarha1.lisää_eläin(eläin2)
eläin2.tee_ääni()

Eläintarha1.listaa_eläimet()
