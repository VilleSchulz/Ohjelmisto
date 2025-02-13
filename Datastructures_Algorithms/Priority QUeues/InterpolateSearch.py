def interpolation_search(array, value):
    start = 0
    end = len(array) - 1

    while start <= end and array[start] <= value <= array[end]:
        # Estetään jakaminen nollalla
        if array[start] == array[end]:
            if array[start] == value:
                return start
            return None

        # Lasketaan interpolaatioindeksi
        midpoint = start + ((end - start) * (value - array[start])) // (array[end] - array[start])

        # Tarkistetaan, löytyikö arvo
        if array[midpoint] == value:
            return midpoint
        elif array[midpoint] < value:
            start = midpoint + 1  # Siirrytään oikealle
        else:
            end = midpoint - 1  # Siirrytään vasemmalle

    return None  # Jos arvoa ei löydy

# Testidata
array = [0, 5, 8, 11, 14, 17, 29, 31, 31, 35, 39, 40, 47, 61, 68, 78, 85, 88, 95, 98]

print(interpolation_search(array, 0))   # 0
print(interpolation_search(array, 98))  # 19
print(interpolation_search(array, 29))  # 6
print(interpolation_search(array, 100)) # None
print(interpolation_search(array, -1))  # None
print(interpolation_search(array, 4))   # None
