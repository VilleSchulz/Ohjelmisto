def insertion_sort(array):
    for i in range(1, len(array)):  # Käydään läpi kaikki alkiot alkaen toisesta (indeksi 1)
        key = array[i]  # Talletetaan tarkasteltava alkio (se, jonka paikkaa etsitään)
        j = i - 1  # Laitetaan j aluksi juuri ennen tarkasteltavaa alkioita (eli vasemmalle)

        # Siirretään kaikki suuremmat alkiot yhdellä askelma oikealle, jotta löydämme paikan keylle
        while j >= 0 and array[j] > key:  # Kun edellinen alkio on suurempi kuin key
            array[j + 1] = array[j]  # Siirretään alkio oikealle
            j -= 1  # Liikutetaan j vasemmalle

        array[j + 1] = key  # Asetetaan key oikeaan kohtaan (kun löytyy oikea paikka)


array = [6, 8, 5, 1, 2]
insertion_sort(array)
print(array)