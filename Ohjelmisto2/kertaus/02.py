class Eläintarha:
    eläimet = []
    def __init__(self, nimi):
        self.nimi = nimi
    def lisää_eläin(self,eläin):
        self.eläimet.append(eläin)



class Eläin():
    def __init__(self,rotu,ääni):
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
