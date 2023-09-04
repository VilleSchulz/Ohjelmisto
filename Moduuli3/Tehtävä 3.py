sukupuoli= str(input("Anna sukupuolesi(m/n): ")).upper()
hemoglobiini= int(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli=="M":
        if hemoglobiini<134:
            print("Hemoglobiiniarvosi on alhainen, miehen normaali arvo on välillä 134-195g/l")
        elif 134<=hemoglobiini<=195:
            print("Hemoglobiinisi on normaalilla tasolla, miehen normaali arvo on välillä 134-195g/l")
        elif hemoglobiini>195:
            print("Hemoglobiinisi on korkealla, miehen normaali arvo on välillä 134-195g/l")
else:
    if sukupuoli=="N":
        if hemoglobiini<117:
            print("Hemoglobiinisi on alhainen, naisen normaali hemoglobiiniarvo on välillä 117-175 g/l")
        elif 117<=hemoglobiini<=175:
            print("Hemoglobiinisi on normaalilla tasolla, naisen normaali arvo on välillä 117-175g/l")
        elif hemoglobiini>175:
            print("Hemoglobiinisi on korkealla, naisen normaali arvo on välillä 117-175g/l")



