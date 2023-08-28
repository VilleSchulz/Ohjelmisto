
import math
leiviskät = int(input ("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luoti = int(input("Anna luodit: "))

leiviskä_m = leiviskät * 8512
naula_m = naulat * 425.6
luoti_m = luoti * 13.3

kokonaismassa = leiviskä_m + naula_m + luoti_m
kokonaismassa_KG = kokonaismassa/1000
result = math.modf(kokonaismassa_KG)
result_kg =result[1]
result_g = result[0]

'''Toinen tapa laskea kiloiksi ja grammoiksi
kilot = int(kokonaismassa // 1000)
gramma = kokonaismassa % 1000'''


print(f"Massa nykymittojen mukaan: \n {result_kg:1.0f}  kilogrammaa ja {result_g:1.0f} grammaa.")