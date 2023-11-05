'''Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. Käytä seuravalla sivulla
esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.'''

import requests

request = f"https://api.chucknorris.io/jokes/random"
end = False
while not end:
    input("Press enter to get random Chuck Norris- joke")
    response_content = requests.get(request).json()
    print(response_content["value"])
    user_input = input("You wanna more jokes?? (Y/N)").lower()
    if user_input == "n":
        end = True
