from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup
import os

# get token from env
TOKEN = os.environ['TOKEN']

def start(update:Update, context:CallbackContext):
    chat_id = update.message.chat.id

    bot=context.bot
    bot.sendMessage(chat_id=chat_id, text='Assalomu alaykum botimizga xush kelibsiz! 👍')


def echo(update:Update, context: CallbackContext):
    # get text from update
    text = update.message.text
    chat_id=update.message.chat.id
    print(text)
    # send Message to bot
    bot=context.bot
    bot.sendMessage(chat_id, text)

def hi(update:Update, context:CallbackContext):
    print('hi')
    chat_id = update.message.chat.id
    bot=context.bot
    bot.sendMessage(chat_id, 'Salom')


def help(update:Update, context:CallbackContext):
    print('hi')
    chat_id = update.message.chat.id

    bot = context.bot
    markup = ReplyKeyboardMarkup(
        [['Help 🇺🇸','Yordam 🇺🇿']]
    )
    bot.sendMessage(
        chat_id=chat_id,
        text='Qanday yordam kerak?',
        reply_markup=markup
        )





updater = Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))
updater.dispatcher.add_handler(MessageHandler(Filters.text('hi'),hi))




updater.start_polling()

updater.idle()