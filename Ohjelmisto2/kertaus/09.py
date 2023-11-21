

class Eläin():
    def __init__(self, rotu, ääni):
        self.rotu = rotu
        self.ääni = ääni


    def tee_ääni(self):
        print(f'{self.rotu} {self.ääni}')


eläin1 = Eläin('Leijona', 'Karjuu')
eläin1.tee_ääni()
eläin2 = Eläin('Kissa', 'Vinkuu')
eläin2.tee_ääni()

