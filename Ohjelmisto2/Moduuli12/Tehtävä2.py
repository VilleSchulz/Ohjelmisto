'''Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan
tekstin sekä lämpötilan Celsius-asteina.Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on
tarpeen, jotta saat rajapintapyynnöissätarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet
muunnettua Celsius-asteiksi.'''


import requests
end = False
api_key = "1de88b337a970d6f071afa1641cba452"

while not end:
    query = input("Anna paikkakunnan nimi jolta halua säätiedotteen!")
    request =f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}&units=metric"
    response_content = requests.get(request).json()
    print(str(response_content["main"]["temp"])+ "°C")
    user_input = input("Haluatko hakea toisen kaupungin tiedot?(y/n)").lower()
    if user_input == "n":
        end = True
