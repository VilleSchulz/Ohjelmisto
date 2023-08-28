sukupuoli= str(input("Anna sukupuolesi(mies/nainen): ")).upper()
hemoglobiini= int(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli=="MIES" and hemoglobiini<134:
    print("Hemoglobiiniarvosi on alhainen, miehen normaali arvo on välillä 134-195g/l")

elif (sukupuoli=="MIES" and  134<=hemoglobiini<=195):
    print("Hemoglobiinisi on normaalilla tasolla, miehen normaali arvo on välillä 134-195g/l")
elif (sukupuoli=="MIES" and  hemoglobiini>195):
    print("Hemoglobiinisi on korkealla, miehen normaali arvo on välillä 134-195g/l")

if sukupuoli=="NAINEN" and hemoglobiini<117:
    print("Hemoglobiinisi on alhainen, naisen normaali hemoglobiiniarvo on välillä 117-175 g/l")
elif sukupuoli=="NAINEN" and  117<=hemoglobiini<=175:
    print("Hemoglobiinisi on normaalilla tasolla, naisen normaali arvo on välillä 117-175g/l")
elif sukupuoli=="NAINEN" and  hemoglobiini>175:
    print("Hemoglobiinisi on korkealla, naisen normaali arvo on välillä 117-175g/l")



