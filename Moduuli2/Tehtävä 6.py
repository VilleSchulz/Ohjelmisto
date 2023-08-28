import random
print("Paina enter-näppäintä arpoaksesi avainkoodit")
input()
# Kolmen luvun koodi
code1 = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
# 4 luvun koodi
code2 = str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6))+ str(random.randint(1,6))

print("Tässä kaksi random avainkoodia:\n" +str(code1) + "\n" +str(code2))