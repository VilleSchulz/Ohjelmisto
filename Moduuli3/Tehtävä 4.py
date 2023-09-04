year = int(input("Anna vuosi: "))
if ( year % 4 == 0 and year % 100!= 0) or ( year % 100 == 0 and year % 400 == 0):
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")
