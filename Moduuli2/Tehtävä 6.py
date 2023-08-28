import random
print("Paina enter-näppäintä arpoaksesi avainkoodit")
input()
# Kolmen luvun koodi
num1_1=random.randint(0,9)
num2_1=random.randint(0,9)
num3_1=random.randint(0,9)

# 4 luvun koodi
num1_2=random.randint(1,6)
num2_2=random.randint(1,6)
num3_2=random.randint(1,9)
num4_2=random.randint(1,6)


code1 = str(num1_1) + str(num2_1) + str(num3_1)
code2 = str(num1_2) + str(num2_2) + str(num3_2) + str(num4_2)

print("Tässä kaksi random avainkoodia:\n" +str(code1) + "\n" +str(code2))