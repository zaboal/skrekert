# Importing local libaries.
import sys
sys.path.append('src/App')
from catalogue import bespeak_product


import logging
# Primary statcs for the logging system.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.DEBUG)


from telegram.ext import Updater, CommandHandler, CallbackContext, Defaults
import telegram
# Primary statics for the API system.
updater = Updater(token='5011357019:AAGVYQ3AdcfAgiscRWT7plSAHkHWRs3P36M', use_context=True)
dispatcher = updater.dispatcher


# General commands' functions.
def bespeak_catalogue(update: Updater, context: CallbackContext): # Beskeaps a catalogue for the current week.
    context.bot.send_message(chat_id=update.effective_chat.id, text=(bespeak_product("🧃️", "Сок", "Моя семья", 18, "из груш, черноплодных рябин, чёрных смородин, малины и клубники")), parse_mode=telegram.ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id, text=(bespeak_product("🍪️", "Печенька", "Юбилейное", 5, "с глазурью из тёмного шоколада на стороне")), parse_mode=telegram.ParseMode.HTML)


# 'Handling' commands, what makes them executable.
dispatcher.add_handler(CommandHandler('catalogue', bespeak_catalogue))

updater.start_polling()
