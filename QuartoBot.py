from telegram.ext import Updater, CommandHandler
from time import strftime

from configBot import TOKEN
up = Updater(TOKEN)

def horas(bot, update):
    msg = "Olá {user_name} agora são"
    msg += strftime('%H:%M:%S')

    bot.send_message(
        chat_id=update.message.chat_id,
        text=msg.format(
            user_name=update.message.from_user.first_name
        )
    )

up.dispatcher.add_handler(CommandHandler('horas', horas))
up.start_polling()

