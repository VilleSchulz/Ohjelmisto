class Tili:
    tilien_määrä = 0
    def __init__(self,nimi,saldo=0):
        self.nimi = nimi
        self.saldo = saldo
        self.tilien_määrä += 1
        print(f'tilejä luotu {self.tilien_määrä}')

    def maksa(self,maksu):
        if self.saldo < maksu:
            self.saldo = self.saldo - maksu
            print('Maksu onnistui')
        else:
            print('EI tarpeeksi rahaa')

    def tulostus(self):
        print(f'Omistaja {self.nimi}, tilillä rahaa{self.saldo}')


print('---tilien luonti---')
t1 = Tili('Jorma')
t2 = Tili('Anne',100)
print('---maksut---')