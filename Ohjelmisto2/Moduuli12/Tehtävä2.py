'''Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan
tekstin sekä lämpötilan Celsius-asteina.Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on
tarpeen, jotta saat rajapintapyynnöissätarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet
muunnettua Celsius-asteiksi.'''


import requests
end = False

try:
    while not end:
        api_key = input("Anna api-key")
        query = input("Anna paikkakunnan nimi jolta halua säätiedotteen!")
        request =f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}&units=metric&lang=fi"
        response_content = requests.get(request).json()
        if int(response_content["cod"]) == 200:
            temperature = response_content['main']['temp']
            weather = response_content['weather'][0]['description']
            print(f"Sää on {weather} ja lämpötila on {temperature} °C")
            user_input = input("Haluatko hakea toisen kaupungin tiedot?(y/n)").lower()
            if user_input == "n":
                end = True
        else:
            print(f"error {response_content['cod']}")
except requests.exceptions.RequestException as error:
    print(error)


#jos haluat kelvineinä niin voi laittaa imperial queryyn tai sitte laskee K = °C + 273,15