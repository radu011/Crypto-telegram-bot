from email import message
from multiprocessing import context
from os import times
from turtle import update
from telegram import Update
import telegram.ext
import schedule
import time
import threading

from binanceTop10 import getTop
from yhFinance import getCryptoInfos
from scraper import getNews, getAbrev

### Api token
with open('botToken.txt', 'r') as f:
    TOKEN = f.read()

### Menu functions
def start(update, context):
    update.message.reply_text("Hello, I am a bot and I am here to help you!")

def help(update, context):
    update.message.reply_text("""
    The following commands are available:
    /start - Welcome message
    /help - This help message
    /abrev - Get the abreviation of the crypto
    /info <crypto abrev> - Get the prices and other info about the crypto
    /top10 - See top 10 cryptocurrencies
    /news - Get the news
    /contact - Get the contact info
    """)

def abrev(update, context):
    update.message.reply_text(getAbrev())

def info(update, context):
    try:
        update.message.reply_text(getCryptoInfos(context.args[0]))
    except (IndexError, ValueError):
        update.message.reply_text('<crypto abrev> is missing')
    

def top10(update, context):
    update.message.reply_text(getTop())

def news(update, context):
    update.message.reply_text(getNews())

def contact(update, context):
    update.message.reply_text("""
    Github: radu011
    Instagram: radu0tm
    """)

def handle_message(update, context):
    update.message.reply_text("You said: " + update.message.text) 


### Menu code
def botMenu():
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    disp = updater.dispatcher
    
    disp.add_handler(telegram.ext.CommandHandler('start', start))
    disp.add_handler(telegram.ext.CommandHandler('help', help))
    disp.add_handler(telegram.ext.CommandHandler('abrev', abrev))
    disp.add_handler(telegram.ext.CommandHandler('info', info, pass_args=True))
    disp.add_handler(telegram.ext.CommandHandler('top10', top10))
    disp.add_handler(telegram.ext.CommandHandler('news', news))
    disp.add_handler(telegram.ext.CommandHandler('contact', contact))
    disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

    updater.start_polling()
    updater.idle()



### Scheduler functions
def showPrices():
    # send message to telegram bot
    
### Scheduler code
def botScheduler():
    for timeS in range (0, 24):
        schedule.every().day.at("12:36").do(showPrices)

    while True:
        schedule.run_pending()
        time.sleep(1)


### Main code
t1 = threading.Thread(target=botScheduler) # Scheduler for info messages
t1.start()
botMenu()
