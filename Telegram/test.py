import requests
import datetime
from config import TOKEN, open_wather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start']) # obrabotkaya anum (hendler@  dekoratora vor@ vercnuma sms @ u abrabotkaya anum)
async def start_command(message: types.Message): # asinxronni funkcia(async) , start_comand(mer anunov asixronni funkciana )
                                                # Sart_comandi mejin@ mer sms na vor2 USER@     UXARKUMA BOTIN
    await message.answer("\U0001F596Привет! Напиши мне название города и я пришлю сводку погоды!")#AWAITI MEJ GRVUMA en kod@ vor@ klini mer funkciayio(meji grac useri harci) patasxan@


@dp.message_handler()
async def get_weather(message: types.Message):
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
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_wather_token}&units=metric')
        data = r.json()
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
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        langht = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])
        await message.answer(f"\U0001F4C9_________{datetime.datetime.now().strftime('%Y-%m-%d')}___________\n"
                             f"Погода в городу -- {city}\nТемпература   :   {cur_wather}С°{wd}\n"
                             f"Влажность воздуха -- {humidity} % \U0001F4A7 \nДавление   :  {pressure} мм.рт.ст\nСкорость ветра    :   {wind} м\с \U0001F300\n\n"
                             f"Восход сольнца -- {sunrise_timestamp.strftime('%H:%M:%S')} \U0001F31D\n"
                             f"Закат сольнца -- {sunset_timestamp.strftime('%H:%M:%S')}\U0001F312\n"
                             f"Дневное время  -- {langht} \U0000231B \n\n"
                             f"              \U0000200D  Хорошего дня!\U0001F44C             ")

    except:
        await message.reply('\U00002620Проверьте название города есть ошибка\U00002620 :')


if __name__ == '__main__':
    executor.start_polling(dp)
