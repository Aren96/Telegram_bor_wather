from config import open_wather_token
import requests
from pprint import pprint
from datetime import datetime


def get_weather(city, open_wather_token):
    code_to_smile = {
        "Clear": "Ясно \U0001F31E",
        "Clouds": "Облачно \U0001F325",
        "Mist": " туман \U0001F32B",
        "Haze": "Мгла \U00002601",
        "Fog": " туман \U0001F32B",
        "Tornado": "Торнадо \U0001F32A",
        "Snow": "Снег \U00002744",
        "Rain": "Дождь \U0001F327",
        "Drizzle": "Морось \U0001F976",
        "Thunderstorm": "Гроза \U0001F329"
    }
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_wather_token}&units=metric')
        data = r.json()
        pprint(data)
        city = data['name']
        cur_wather = data['main']['temp']
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно , не пойму что там за погода '
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.fromtimestamp(data['sys']['sunset'])
        langht = datetime.fromtimestamp(data['sys']['sunset']) - datetime.fromtimestamp(data['sys']['sunrise'])
        print(f"####### {datetime.now().strftime('%Y-%m-%d')} #######\U0001F64C\n"
              f"Погода в городу : {city}\nТемпература : {cur_wather}С°{wd}\n"
              f"Влажность воздуха : {humidity} % \U0001F4A7\n Давление : {pressure} мм.рт.ст Скорость ветра : {wind} м\с \n \n"
              f"Восход сольнца : {sunrise_timestamp} \U0001F31D\n"
              f"Закат сольнца : {sunset_timestamp}\U0001F312\n"
              f"Дневное время Дня : {langht} можно много чего успеть сделвть \U0000231B \n"
              f"******* Хорошего дня! *******")

    except Exception as ex:
        print(ex)
        print('роверьте название города есть ошибка :')


def main():
    city = input('ввидите наиминование города :')
    get_weather(city, open_wather_token)

#
if __name__ == main():
    main()
# print(city)

