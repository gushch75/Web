from telegram import Update
from telegram.ext import Updater, CommandHandler, Filters,MessageHandler
from bot_commands import *

updater = Updater('5410393603:AAGrC8faoNm6E3F4H_FfIcllPuVRW3w_aDU')
updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(MessageHandler(Filters.text, UserStep))
print('server start')
updater.start_polling()
updater.idle()