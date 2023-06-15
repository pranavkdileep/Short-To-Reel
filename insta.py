import telebot
import app
from flask import Flask, jsonify, request

BOT_TOKEN = "1836057993:AAF4cP9qNx3gFh-epkgjBRYkALyzVs6W0gw"

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    
    mess = message.text
    urlly = mess.replace("?feature=share3","")
    bot.reply_to(message, urlly)
    app.downloadvid(urlly)
    app.instaup()

bot.infinity_polling()
app = Flask(__name__)
@app.route('/')
    def index():
        return 'Web App with Python Flask!'
    
   app.run(host='0.0.0.0', port=81)
