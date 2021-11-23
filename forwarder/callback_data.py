from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode, Update
from telegram.ext import Client, Filters

Pm = """hello"""

def /register(update: Update, _):
    data = update.data
    if data == "/register":
        update.reply_text(
          Pm,
            parse_mode=ParseMode.HTML,
        )
    else:
        update.reply_text("I'm up and running!")




def main():
    CallbackQuery = CallbackQuery(
        "/register", register,run_async=True
    )
