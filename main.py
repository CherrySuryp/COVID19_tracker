import time
import covid_info
from googletrans import Translator
import telebot
from telebot import types

translator = Translator()

bot = telebot.TeleBot(open('BOT_ACCESS').read())

# Кнопки начало
menu_keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
stat_button = types.KeyboardButton(text='Статистика')
menu_keyboard.add(stat_button)

# Кнопки меню статистики
stat_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
go_to_suggestions = types.KeyboardButton(text='Рекомендации')
stat_menu.add(go_to_suggestions)

# Кнопки меню информации и рекомендаций

how_to_protect = types.KeyboardButton(text='Меры предосторожности')
first_sug = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
first_sug.add(how_to_protect)

symptoms = types.KeyboardButton(text='Симптомы и группы риска')
second_sug = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
second_sug.add(symptoms)

myth = types.KeyboardButton(text='Мифы')
third_sug = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
third_sug.add(myth)


@bot.message_handler(commands=['start'])
def greet(message):
    global message_id
    message_id = message.chat.id
    bot.send_message(message.chat.id,
                     'Привет, <b>{0.first_name}</b>!\n'
                     'Я бот, который поможет вам узнать больше про Коронавирус(COVID19)\n\n'
                     'Нажмите кнопку <b>"статистика"</b> '
                     'и вы узнаете актуальную информацию о количестве зараженных'.format(
                         message.from_user),
                     parse_mode='html', reply_markup=menu_keyboard)


@bot.message_handler(content_types=['text'])
def statMenu(message):
    # Меню статистики
    if message.text == 'Статистика':
        bot.send_message(message.chat.id, covid_info.worldInfo().format(message.from_user),
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         covid_info.countryInfo("Russia").format(message.from_user),
                         parse_mode='html')
        time.sleep(2)
        bot.send_message(message.chat.id,
                         'Пугает статистика?\n'
                         'Меня вот пугает, хоть Я и бот\n'
                         '--------------------------------------------------------------\n'
                         'Получите полезные советы по профилактике коронавируса, нажав на кнопку <b>"Рекомендации"</b>',
                         parse_mode='html', reply_markup=stat_menu)

    # Меню рекомендаций
    elif message.text == 'Рекомендации':
        bot.send_message(message.chat.id,
                         "Отлично!\n"
                         "Я очень рад, что Вам не безразлична безопасность вас и окружающих\n\n",
                         parse_mode='html')
        time.sleep(1.5)
        bot.send_message(message.chat.id,
                         "Хотите узнать про <b>меры предосторожности?</b>\n"
                         "Тогда тыкайте на кнопку снизу",
                         parse_mode='html',
                         reply_markup=first_sug)
    elif message.text == 'Меры предосторожности':
        # первый совет
        bot.send_message(message.chat.id,
                         'Итак, начнем ликбез')
        time.sleep(1)
        bot.send_message(message.chat.id,
                         '<b>В первую очередь!</b>\n\n'
                         'Регулярно мойте руки антибактериальным мылом\n'
                         '<b>Или</b> обрабатывайте их спиртосодержащим антисептиком\n\n'
                         '--------------------------------------------------------------\n'
                         '"Но бот, все же и так моют руки"\n'
                         'Скажете вы\n'
                         '--------------------------------------------------------------\n\n'
                         'Да, это так, но хочу обратить ваше внимание на:\n\n'
                         '1)Мыло должно быть <b>антибактериальным</b>\n\n'
                         '2)Антисептик должен содержать спирт концентрации <b>не менее 60%</b> '
                         'Водка <b>не подойдет</b>',
                         parse_mode='html')
        time.sleep(11.5)
        # второй совет
        bot.send_message(message.chat.id,
                         "<b>Во вторых</b>\n\n"
                         "Соблюдайте правила респираторной гигиены\n\n"
                         "При кашле и чихании прикрывайте рот и нос салфеткой, сгибом локтя, "
                         "а лучше всего приобретите маску\n"
                         "Cразу выкидывайте салфетку в контейнер для мусора "
                         "и обрабатывайте руки спиртосодержащим антисептиком или мойте их водой с мылом\n\n"
                         "<b>Зачем это нужно?</b>\n\n"
                         "Все просто\n"
                         "Прикрывание рта и носа при кашле и чихании салфеткой позволяет предотвратить распространение "
                         "вирусов и других болезнетворных микроорганизмов\n\n"
                         "<b>ВАЖНО!</b>\n\n"
                         "Если при кашле или чихании прикрывать нос и рот ладонью, микробы могут попасть на ваши руки, "
                         "а затем на предметы или на людей, к которым вы прикасаетесь.",
                         parse_mode='html')
        time.sleep(15)
        bot.send_message(message.chat.id,
                         "Фух, ну вроде все основное рассказал\n\n")
        time.sleep(1.5)
        bot.send_message(message.chat.id,
                         "Далее у нас по плану <b>симптомы COVID-19</b>\n"
                         "Просто нажми на кнопку", parse_mode='html', reply_markup=second_sug)
    elif message.text == 'Симптомы и группы риска':
        # симптомы
        bot.send_message(message.chat.id,
                         "<b>Группы риска</b>\n\n"
                         "В группу риска входят:\n"
                         "Беременные\n"
                         "Люди с хроническими заболеваниями(астма и т.д.)\n"
                         "Диабетики\n"
                         "Младенцы\n"
                         "Пожилые люди\n\n"
                         "<b>Симптомы</b>\n\n"
                         "Инкубационные период коронавируса составляет <b>до 14 дней</b>\n\n"
                         "К наиболее распространенным симптомам COVID‑19 относятся:\n\n"
                         "1.Повышение температуры тела\n"
                         "2.Утомляемость\n"
                         "3.Сухой кашель\n\n"
                         "У некоторых людей могут отмечаться различные боли,"
                         " заложенность носа, насморк, фарингит или диарея",
                         parse_mode='html')
        time.sleep(2)
        bot.send_message(message.chat.id,
                         "Если вдруг у вас есть хоть один из этих симптомов, то не стоит медлить с визитом к врачу!",
                         reply_markup=third_sug)
        time.sleep(2)
    elif message.text == 'Мифы':
        bot.send_message(message.chat.id,
                         "<b>Немного информации про мифы</b>\n\n"
                         "Вот несколько ложных представлений и мифов:\n\n"
                         "1. Коронавирусная болезнь является неизлечимым заболеванием.\n\n"
                         "2. Употребление алкоголя защищает от COVID‑19 и может быть опасным\n\n"
                         "3. Вирус погибает при высокой температуре, поэтому нужно принять ванну\n\n"
                         "4. Обработка поверхности всего тела этанолом или хлорной "
                         "известью позволяет уничтожить новый коронавирус\n\n"
                         "5. Вирусом можно заразиться сьев импортный банан\n\n"
                         "6. Чеснок защищает от заражения")
        bot.send_message(message.chat.id,
                         "Вы сами-то в это верите? Мне вот что то не очень верится\n"
                         "Все вышеперечисленные высказывания являются <b>мифами</b> и никак научно не доказаны",
                         parse_mode='html')


#    elif message.text == 'Информация по странам':
#        msg = bot.send_message(message.chat.id, 'Введите интересующую вас страну')
#        bot.register_next_step_handler(msg, stats)


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
