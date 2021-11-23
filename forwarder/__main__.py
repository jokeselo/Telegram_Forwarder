import importlib
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode, Update
from telegram.ext import CommandHandler, Filters

from forwarder import (API_KEY, CERT_PATH, IP_ADDRESS, LOGGER, OWNER_ID, PORT,
                       URL, WEBHOOK, dispatcher, updater)
from forwarder.modules import ALL_MODULES

JOIN_BUTTONS = [
    InlineKeyboardButton(
        text='Contact For More Help',
        url='https://t.me/mhdfajis'
    )
]

BUTTONS = InlineKeyboardMarkup(
    [JOIN_BUTTONS]
)
PM_START_TEXT = """
Hey {}, I'm {}!

I'm a bot used to add Views On All Upcoming Posts Of A Channel.

For Access Click /Register 

Plan Starting From 15k 
To obtain a list of plan , use /help.
"""

Register_TEXT = """
Please Enter Your Channel Username For Registration

Note : Before Request For Register Should Be Pay The Plan Charge
"""

PM_HELP_TEXT = """
<b>Here is a list of plans:</b>

- 15k : 2k views On All Posts , 100 post daily , 1 month validity.

- 25k : 5k views On All Posts , 160 Posts Daily, 45 days validity.

- 35k : 10k views On All Posts , unlimited Post,30 days validity.

Contact @mhdfajis for payment Details
"""

for module in ALL_MODULES:
    importlib.import_module("forwarder.modules." + module)


def start(update: Update, _):
    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user

    if chat.type == "private":
        message.reply_text(
            PM_START_TEXT.format(user.first_name, dispatcher.bot.first_name),
            reply_markup=BUTTONS,
            parse_mode=ParseMode.HTML,
        )
    else:
        message.reply_text("I'm up and running!")


def help(update: Update, _):
    chat = update.effective_chat
    message = update.effective_message

    if not chat.type == "private":
        message.reply_text("Contact me via PM Ti Get Details.")
    else:
        message.reply_text(PM_HELP_TEXT,
       reply_markup=BUTTONS,
       parse_mode=ParseMode.HTML)

def Add(update: Update, _):
    chat = update.effective_chat
    message = update.effective_message

    if not chat.type == "private":
        message.reply_text("Contact me via Pm For Details To Register.")
    else:
        message.reply_text(Register_TEXT,
       parse_mode=ParseMode.HTML)
CommandHandler.register_next_step_handler(message, username)

def main():
    start_handler = CommandHandler(
        "start", start,run_async=True
    )
    help_handler = CommandHandler(
        "help", help, run_async=True
    )

    Add_handler = CommandHandler(
        "Add",Add,run_async=True
    )

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(Add_handler)


def username(message):
   try:
    if len(message.text) == 5:
       message.reply_text("💹Your Trx wallet set to")


    if WEBHOOK and URL:
        LOGGER.info("Using webhooks.")
        updater.start_webhook(listen=IP_ADDRESS, port=PORT, url_path=API_KEY)

        if CERT_PATH:
            updater.bot.set_webhook(
                url=URL + API_KEY, certificate=open(CERT_PATH, "rb")
            )
        else:
            updater.bot.set_webhook(url=URL + API_KEY)

    else:
        LOGGER.info("Using long polling.")
        updater.start_polling(timeout=15, read_latency=4)

    updater.idle()


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    main()
