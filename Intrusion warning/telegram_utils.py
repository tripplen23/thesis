import telegram


def send_telegram(photo_path="alert.png"):
    try:
        my_token = "6600484016:AAGcR0xieWIUoBkw9IfMdhwRenlG1Lqtq5Q"
        bot = telegram.Bot(token=my_token)
        bot.sendPhoto(chat_id="1910018067", photo=open(
            photo_path, "rb"), caption="Intrusion detection")
        print("Sent message successfully!")
    except Exception as ex:
        print("Cannot send message to Telegram", ex)
