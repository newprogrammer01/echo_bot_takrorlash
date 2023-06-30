# from telegram import Bot
# import os

# # get token from env
# TOKEN = os.environ['TOKEN']
# # Create a bot object
# bot = Bot(token=TOKEN)

# chat_id =5575549228
# # Send message
# bot.sendMessage(chat_id=chat_id,text='Salom')

# # Get updates from bot

# updates = bot.getUpdates()
# photos = updates[5].message.photo
# file_id=photos[0].file_id
# print(file_id)
# bot.sendPhoto(chat_id=chat_id,photo=file_id)




from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram import Update,ReplyKeyboardMarkup
import os

# get token from env
TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    bot = context.bot
    bot.sendMessage(chat_id,'Assalom alaykum xush kelibsiz botimizga 👍')

def echo(update: Update, context: CallbackContext):
    # Get text from update
    text = update.message.text
    chat_id = update.message.chat.id
    print(text)
    # Send message to Bot
    bot = context.bot
    bot.sendMessage(chat_id,text)

def hi(update: Update, context: CallbackContext):
    print('hi')
    chat_id = update.message.chat.id

    bot = context.bot
    bot.sendMessage(chat_id,'Salom')

def help(update: Update, context: CallbackContext):
    print('hi')
    chat_id = update.message.chat.id

    bot = context.bot
    markup = ReplyKeyboardMarkup(
        [['Help 🇺🇸','Yordam 🇺🇿']]
        )
    bot.sendMessage(
        chat_id=chat_id,
        text='Qanday yordam kerak!!!',
        reply_markup=markup)
updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CommandHandler('help',help))
updater.dispatcher.add_handler(MessageHandler(Filters.text('hi'),hi))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()