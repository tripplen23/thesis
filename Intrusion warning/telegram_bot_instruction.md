# 1. Create a Telegram account

# 2. Create a Telegram bot with BotFather (verified)

    ## 2.1. BotFather (verified):

    ![Alt text](./img/BotFather_verified.png)

    ## 2.2. Click to start button:

    ![Alt text](./img/Start.png)

    ## 2.3. Create new bot:

    ![Alt text](./img/NewBot.png)

    ## 2.4. Set Bot information and get token of our bot:

    ![Alt text](./img/GetToken.png)

# 3. Create a group chat and get chat ID of user

- Make a warning: When you need to send a warning to a person, you need to have the chat ID of that person

  ## 3.1. Access for chatting to the bot so that Telegram API could fetch our data information

  ![Alt text](./img/AccessBot.png)

  ## 3.2. After click to the start button:

  GET USER ID here:
  http://api.telegram.org/bot[TOKEN]/getUpdates
  ![Alt text](./img/GetUserID.png)

  SEND Message to the User through(optional):
  http://api.telegram.org/bot[TOKEN]/sendMessage?chat_id=[CHAT_ID]&text=[MY_MESSAGE_TEXT]
  ![Alt text](./img/SendMessage.png)
  ![Alt text](./img/ReceivedMessage.png)

# 4. Add library python-telegram-bot or aiogram

# 5. Write code to send text and image
