from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode, Update
from telegram.ext import Client, Filters

Pm = """hello"""

@Client.on_callback_query()
async def callback(update, Update):
        update.reply_text(
          Pm,
            parse_mode=ParseMode.HTML,
        )
    else:
        update.reply_text("I'm up and running!")


