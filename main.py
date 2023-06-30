from telegram import Bot
import os

# get token from env
TOKEN=os.environ['TOKEN']
# create a bot object
bot=Bot(token=TOKEN)

chat_id=1901668739
# send message
bot.sendMessage(chat_id=chat_id, text='Salom')

# Get updates from bot

updates = bot.getUpdates()
photos=updates.message[-1].photo
file_id=photos[0].file_id
print(file_id)
bot.sendPhoto(chat_id=chat_id, photo=file_id)