import telebot
import os
import random


with open(os.path.join(os.getcwd(), 'bot_token'), 'r') as file:
    bot_token = file.read().strip()
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola, soy las funcionalidades Extras de @seleduckbot")

@bot.message_handler(commands=['meme'])
def send_meme(message):
    images = os.listdir('memes')
    image_path = os.path.join('memes', random.choice(images))
    with open(image_path, 'rb') as f:
        bot.send_photo(message.chat.id, f, reply_to_message_id=message.message_id)
        
@bot.message_handler(commands=['captcha'])
def send_captcha(message):
    images = os.listdir('captcha')
    image_path = os.path.join('captcha', random.choice(images))
    with open(image_path, 'rb') as f:
        bot.send_photo(message.chat.id, f, caption="¿Esto es un pato?", reply_markup=telebot.types.InlineKeyboardMarkup().row(
            telebot.types.InlineKeyboardButton("Sí", callback_data='yes'),
            telebot.types.InlineKeyboardButton("No", callback_data='no')
        ), reply_to_message_id=message.message_id)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.message.photo:
        # Obtiene el archivo de imagen a partir del mensaje.
        image_file = bot.get_file(call.message.photo[-1].file_id)
        image_path = image_file.file_path
        print(image_path)
        if image_path.endswith('captcha/duck') and call.data == 'yes':
            bot.send_message(call.message.chat.id, "Correcto")
        elif not image_path.endswith('captcha/duck') and call.data == 'no':
            bot.send_message(call.message.chat.id, "Correcto")
        else:
            bot.send_message(call.message.chat.id, "Incorrecto")

@bot.message_handler(commands=['react'])
def send_react(message):
    sticker_packs = ['internetexplorers', 'videogamesgirls']
    sticker_pack = random.choice(sticker_packs)
    pack = bot.get_sticker_set(sticker_pack)
    sticker = random.choice(pack.stickers)
    bot.send_sticker(message.chat.id, sticker.file_id, reply_to_message_id=message.message_id)
    
@bot.message_handler(commands=['helldance'])
def send_react(message):
    sticker_pack = 'HelltakerSwidly'
    pack = bot.get_sticker_set(sticker_pack)
    sticker = random.choice(pack.stickers)
    bot.send_sticker(message.chat.id, sticker.file_id, reply_to_message_id=message.message_id)

# Start the bot
bot.polling()
