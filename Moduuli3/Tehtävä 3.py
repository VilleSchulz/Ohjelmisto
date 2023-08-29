sukupuoli= str(input("Anna sukupuolesi(m/n): ")).upper()
hemoglobiini= int(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli=="M" and hemoglobiini<134:
    print("Hemoglobiiniarvosi on alhainen, miehen normaali arvo on välillä 134-195g/l")

elif (sukupuoli=="M" and  134<=hemoglobiini<=195):
    print("Hemoglobiinisi on normaalilla tasolla, miehen normaali arvo on välillä 134-195g/l")
elif (sukupuoli=="M" and  hemoglobiini>195):
    print("Hemoglobiinisi on korkealla, miehen normaali arvo on välillä 134-195g/l")

if sukupuoli=="N" and hemoglobiini<117:
    print("Hemoglobiinisi on alhainen, naisen normaali hemoglobiiniarvo on välillä 117-175 g/l")
elif sukupuoli=="N" and  117<=hemoglobiini<=175:
    print("Hemoglobiinisi on normaalilla tasolla, naisen normaali arvo on välillä 117-175g/l")
elif sukupuoli=="N" and  hemoglobiini>175:
    print("Hemoglobiinisi on korkealla, naisen normaali arvo on välillä 117-175g/l")



