#pip install of BotAPI
!pip install pyTelegramBotAPI requests

#Process 
import telebot
import requests
import json

#Using API Keys
TELEGRAM_API_KEY = '6042809880:AAFTc9nyR3l6h_gO0lHewivb8fW19Vk57Ng'
OPENWEATHER_API_KEY = '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'

#Running the Bot Function
bot = telebot.TeleBot(TELEGRAM_API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Send me a city name and I'll provide the current temperature.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    city_name = message.text
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}')
    data = json.loads(response.text)
    if data['cod'] == 200:
        temp = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        bot.reply_to(message, f'The current temperature in {city_name} is {temp:.2f}°C.')
    else:
        bot.reply_to(message, 'Sorry, I could not find that city.')

bot.polling()
