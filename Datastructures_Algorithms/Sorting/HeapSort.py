def heap_sort(array):
    # Muunnetaan taulukko max-heapiksi käyttämällä sift_down-funktiota
    for start in range(len(array) // 2 - 1, -1, -1):
        sift_down(array, start, len(array) - 1)

    # Järjestetään taulukko poistamalla max-heapista yksi alkio kerrallaan
    end = len(array) - 1  # Viimeinen alkion indeksi

    # Käydään heap läpi niin kauan kuin siinä on alkioita
    while end > 0:
        # Vaihdetaan juurisolmu (suurin arvo) ja viimeinen alkio
        array[0], array[end] = array[end], array[0]

        # Pienennetään keon kokoa yhdellä
        end -= 1

        # Korjataan heap, jotta suurin arvo on taas juurena
        sift_down(array, 0, end)
