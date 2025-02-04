import telebot
import webbrowser
from telebot import types
bot = telebot.TeleBot('7698187197:AAFFNNogj49D1OxUMThQHozGeYOTnKiJKgA')


@bot.message_handler(comands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('пупи тут')
    markup.row(btn1)
    btn2 = types.KeyboardButton('удалить фото')
    btn3 = types.KeyboardButton('изменить ответ')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Привет еще и тут', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('пупи тут', url='https://www.youtube.com/shorts/3cOnrftz5uY')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('изменить ответ', callback_data='edit')
    markup.row(btn2,btn3)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == "edit":
        bot.edit_message_text('Уже некрасивое фото', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com/shorts/3cOnrftz5uY')


@bot.message_handler(commands=['inf'])
def main(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}, от пипикалки, написанной на Python!')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Тут</b> <em><u>никто</u></em> не помахает только попипикают', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}, риветриветривет')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.from_user.id}')


bot.polling(none_stop=True)
