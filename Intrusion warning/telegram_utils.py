from aiogram import Bot


async def send_telegram(text):
    try:
        my_token = "6600484016:AAGcR0xieWIUoBkw9IfMdhwRenlG1Lqtq5Q"
        chat_id = "1910018067"

        bot = Bot(token=my_token)

        # Send the text message
        await bot.send_message(chat_id, text)

        print("Message sent successfully!")

    except Exception as ex:
        print("Error sending message to Telegram", str(ex))
