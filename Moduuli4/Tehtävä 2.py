sentit= 0
while sentit >= 0:
    sentit = float(input("Anna pituus senttimetreinä, niin muutan sen tuumiksi: "))
    tuumat = sentit / 2.54
    if sentit>=0:
        print(f"{tuumat} tuumaa")