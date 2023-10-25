hytti_luokka= str(input("Anna hyttiluokkasi (LUX,A,B,C) : ")).upper()

if hytti_luokka== "LUX":
    print("Hyttisi on parvekkeellinen hytti yläkannella.")

elif hytti_luokka=="A":
        print("Hyttisi on ikkunallinen hytti autokannen yläpuolella.")
elif hytti_luokka=="B":
    print("Hyttisi on ikkunaton hytti autokannen yläpuolella")
elif hytti_luokka=="C":
    print("Hyttisi on ikkunaton hytti autokannen alapuolella")

else:
    print("Virheellinen hyttiluokka")