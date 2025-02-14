def sift_down(array, start, end):
    # Aloitetaan annetuista indeksistä
    current = start

    # Jatketaan niin kauan kuin vasen lapsi on taulukon sisällä
    while (left_child := 2 * current + 1) <= end:
        swap_index = current  # Oletetaan ensin, että nykyinen solmu on oikeassa paikassa

        # Tarkistetaan, onko vasen lapsi suurempi kuin nykyinen solmu
        if array[swap_index] < array[left_child]:
            swap_index = left_child

        # Lasketaan oikean lapsen indeksi
        right_child = 2 * current + 2
        # Tarkistetaan, onko oikea lapsi olemassa ja suurempi kuin tähän mennessä suurin
        if right_child <= end and array[swap_index] < array[right_child]:
            swap_index = right_child

        # Jos nykyinen solmu on jo suurin, lopetetaan
        if swap_index == current:
            return

        # Vaihdetaan nykyinen solmu ja suurin lapsi keskenään
        array[current], array[swap_index] = array[swap_index], array[current]

        # Jatketaan upottamista uudessa sijainnissa
        current = swap_index

array = [6, 2, 5, 8, 1]
sift_down(array, 1, 4)
print(array)
