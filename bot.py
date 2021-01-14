import telebot
import requests
from bs4 import BeautifulSoup
from telebot.types import Message
import datetime 

TOKEN = '1563919776:AAHDEQOOCwfxBkHfMmfFRyFYWRgADCCSXgA'
bot = telebot.TeleBot(TOKEN)

# API = 'https://banks.kg/api/v1/rates/daily/usd'
Dollar_url = 'https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS&valuta_id=15&beg_day=09&beg_month=01&beg_year=2021&end_day=14&end_month=01&end_year=2021'
Kaz_Url = 'https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS&valuta_id=40&beg_day=09&beg_month=01&beg_year=2021&end_day=14&end_month=01&end_year=2021'
Rub_Url = 'https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS&valuta_id=44&beg_day=09&beg_month=01&beg_year=2021&end_day=14&end_month=01&end_year=2021'


# Американский доллар
r = requests.get(Dollar_url)
soup = BeautifulSoup(r.text, 'html.parser')
tables = soup.find('table')

answer_to_USD = '\n\n'
for val in tables:
    try:
        date = val.find('td', class_="stat-center").text
    except:
        date = 'Актуальная дата'

    try:
        value = val.find('td', class_='stat-right').text
    except:
       value = 'Курс'

    answer_to_USD += date + '-->' + value + ' сом' + '\n'

# res = requests.get(API)
# j = res.json()
# buy = j['buy']
# for record in buy:
#     answer = datetime.datetime.fromtimestamp(record[0]/1000).strftime('%Y-%m-%d %H:%M:%S'), record[-1]
# ------------------------------------------------------------

# Казахский тенге
r_KZ = requests.get(Kaz_Url)
soup_KZ = BeautifulSoup(r_KZ.text, 'html.parser')
tables_KZ = soup_KZ.find('table')

answer_to_KZ = '\n\n'
for val_KZ in tables_KZ:
    try:
        date_KZ = val_KZ.find('td', class_="stat-center").text
    except:
        date_KZ = 'Актуальная дата'

    try:
        value_KZ = val_KZ.find('td', class_='stat-right').text
    except:
       value_KZ = 'Курс'

    answer_to_KZ += date_KZ + '-->' + value_KZ + ' сом' + '\n'    
# -----------------------------------------------------------------

# Российский рубль

r_RU = requests.get(Rub_Url)
soup_RU = BeautifulSoup(r_RU.text, 'html.parser')
tables_RU = soup_RU.find('table')

answer_to_RU = '\n\n'
for val_RU in tables_RU:
    try:
        date_RU = val_RU.find('td', class_="stat-center").text
    except:
        date_RU = 'Актуальная дата'

    try:
        value_RU = val_RU.find('td', class_='stat-right').text
    except:
       value_RU = 'Курс'

    answer_to_RU += date_RU + '-->' + value_RU + ' сом' + '\n' 
# --------------------------------------------------------------------

@bot.message_handler(commands=['start'])
def command_handler(message:Message):
    bot.reply_to(message, 'Привет! Выбери валюту\n("USD", "KZT", "RUB")')

@bot.message_handler(content_types=['text'])
def message_handler(message:Message):
    if message.text == 'USD' or message.text == 'Usd' or message.text == 'usd':
        bot.reply_to(message, answer_to_USD)
    elif message.text == 'KZT' or message.text == 'Kzt' or message.text == 'kzt':
        bot.reply_to(message, answer_to_KZ)
    elif message.text == 'RUB' or message.text == 'Rub' or message.text == 'rub':
        bot.reply_to(message, answer_to_RU)
    else: 
        bot.reply_to(message, 'Какая валюта?')


if __name__ == '__main__':

    bot.polling(none_stop=True)

