import telegram
from telegram.ext import Updater, MessageHandler, CallbackContext

# Replace YOUR_TOKEN with your actual bot token
bot = telegram.Bot(token='YOUR_TOKEN')

def greet_user(update: telegram.Update, context: CallbackContext):
    """Greet new users when they join the group"""
    message = f"Hi {update.message.new_chat_members[0].first_name}, welcome to the group!"
    bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    """Start the bot"""
    updater = Updater('5910905057:AAE5XSruU0OHCxIjum-KJfgwCbStQ-TUf88', use_context=True)
    dispatcher = updater.dispatcher

    # Add handler to greet new users when they join the group
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, greet_user))

    updater.start_polling()
    updater.idle()
bot.polling()
