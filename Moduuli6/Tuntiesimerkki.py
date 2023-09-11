def tervehdi(tervehdys, kerrat):# kerrat = parametrimuuttujat
    for i in range(kerrat):
        print (tervehdys + " " + str(i+1) + ". kerran")
    return

print("päivä alkaa tervehdyksillä")
tervehdi("Moi", 3)
tervehdi("Hyvää päivää", 2)