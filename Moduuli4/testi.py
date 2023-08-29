''''

kerrat= int(input('Kuinka monta kertaa haluat, että koira haukkuu?: '))
tehdyt_haukut = 0
while tehdyt_haukut<kerrat:
    print('HAU')
    tehdyt_haukut += 1'''

print('koira haukkuu koko ajan')
käsky = input('Anna käsky ''stop'' jos haluat että koira lopettaa haukkumisen')
while käsky !='stop':
    haukku = 0
    while haukku<10:
        print('HAU')
        haukku += 1
    käsky = input('Anna käsky ''stop'' jos haluat että koira lopettaa haukkumisen')



