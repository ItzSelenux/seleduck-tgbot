import os

with open(os.path.join(os.getcwd(), 'bot_token'), 'r') as file:
    bot_token = file.read().strip()

print(bot_token)
