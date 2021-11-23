from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode, Update
from telegram.ext import Client, Filters

Pm = """hello"""

def /register(update: Update, _):
    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user

    if chat.type == "private":
        message.reply_text(
          Pm,
            parse_mode=ParseMode.HTML,
        )
    else:
        message.reply_text("I'm up and running!")




def main():
    start_handler = client(
        "/register", register,run_async=True
    )
