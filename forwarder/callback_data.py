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




def main():
    start_handler = CommandHandler(
        "start", start,run_async=True
    )
