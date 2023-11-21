class Eläintarha:
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

     #metodien ylikirjoittaminen, eli nyt lisätään myös väri



class Lintu(Eläin):
    def __init__(self, rotu, ääni, väri):
        super().__init__(rotu, ääni)
        #Eläin.__init__(self,rotu,ääni)
        self.väri = väri

    def tee_ääni(self):
        print(f'{self.rotu} {self.ääni}')
        print(f'sulkieni väri on {self.väri}')


eläin1 = Eläin('Leijona', 'Karjuu')
eläin2 = Eläin('Kissa', 'Vinkuu')
eläin3 = Lintu('Käki', 'Kukkuu', 'Ruskea')
Eläintarha1 = Eläintarha('zoo')

Eläintarha1.lisää_eläin(eläin1)
eläin1.tee_ääni()

Eläintarha1.lisää_eläin(eläin2)
eläin2.tee_ääni()

Eläintarha1.listaa_eläimet()
