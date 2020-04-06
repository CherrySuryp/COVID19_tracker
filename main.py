import covid_info
from googletrans import Translator
import telebot
from telebot import types

translator = Translator()

bot = telebot.TeleBot(open('BOT_ACCESS').read())
# Кнопки основного меню
menu_keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
stat_button = types.KeyboardButton(text='Статистика')
info_button = types.KeyboardButton(text='Рекомендации')
menu_keyboard.add(stat_button, info_button)

# Кнопки меню статистики
stat_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
info_latest = types.KeyboardButton(text='Информация по странам')
info_back = types.KeyboardButton(text='Назад в меню')
info_ru = types.KeyboardButton(text='Информация по России')
stat_menu.add(info_latest, info_ru, info_back)

# Кнопки меню рекомендаций
suggestion_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
suggestion_menu.add(info_back)
message_id = int()


@bot.message_handler(commands=['start'])
def greet(message):
    global message_id
    message_id = message.chat.id
    bot.send_message(message.chat.id,
                     'Привет, <b>{0.first_name}</b>!\n'
                     'Я бот, который поможет тебе узнать больше про Коронавирус(COVID19)'.format(message.from_user),
                     parse_mode='html', reply_markup=menu_keyboard)


@bot.message_handler(content_types=['text'])
def statMenu(message):
    # Меню статистики
    if message.text == 'Статистика':
        bot.send_message(message.chat.id, covid_info.worldInfo().format(message.from_user),
                         parse_mode='html',
                         reply_markup=stat_menu)

    elif message.text == 'Информация по странам':
        msg = bot.send_message(message.chat.id, 'Введите интересующую вас страну')
        bot.register_next_step_handler(msg, stats)

    elif message.text == 'Информация по России':
        bot.send_message(message.chat.id,
                         covid_info.countryInfo("Russia").format(message.from_user),
                         parse_mode='html', reply_markup=menu_keyboard)

    elif message.text == 'Назад в меню':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=menu_keyboard)
    # Конец меню статистики ---------------------------------------------------------------------------

    # Меню рекомендаций
    elif message.text == 'Рекомендации':
        bot.send_message(message.chat.id,
                         "В этом меню вы можете узнать всю подробную информацию о коронавирусной инфекции\n"
                         "--------------------------------------------------------------\n\n"
                         '<b>Подробную информацию можно получить</b> '
                         '<a href = "https://coronavirus-spravka.ru/">на этом сайте</a>\n\n'
                         "<b>Или по телефону горячей линии по коронавирусу в РФ</b>\n"
                         "8(800)2000-112\n",
                         parse_mode='html',
                         disable_web_page_preview=True, reply_markup=suggestion_menu)


def stats(message):
    if message.text == 'США' or str(message.text).lower() == 'соединенные штаты':
        bot.send_message(message.chat.id,
                         covid_info.countryInfo("").format(message.from_user),
                         parse_mode='html', reply_markup=stat_menu)
    else:
        bot.send_message(message.chat.id,
                         covid_info.countryInfo(translator.translate(message.text).text).format(message.from_user),
                         parse_mode='html', reply_markup=stat_menu)


bot.polling(none_stop=True)
