tuumat= 0
while tuumat >= 0:
    tuumat = float(input("Anna pituus tuumina, niin muutan sen senteiksi: "))
    sentit = tuumat * 2.54
    if tuumat>=0:
        print(f"{sentit}cm")