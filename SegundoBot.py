import telegram

from time import sleep
from configBot import TOKEN

try:
    from urllib.error import URLError
except ImportError:
    from urllib.request import urlopen

def main():
    update_id = None
    bot = telegram.Bot(TOKEN)
    print('Bot Telegram iniciando...')

    while True:
        try:
            update_id = priscylaBot(bot, update_id)
        except telegram.TelegramError as e:
            if e.message in ("Bad Gateway", "Timed out"):
                sleep(1)
            else:
                raise e
        except URLError as e:
            sleep(1)


def priscylaBot(bot, update_id):
    for update in bot.getUpdates(offset=update_id, timeout=10):
        chat_id = update.message.chat_id
        update_id = update.update_id + 1
        message = update.message.text

        if message:
            bot.send_message(chat_id=chat_id, text=message)
        return update_id

if __name__ == '__main__':
    main()
