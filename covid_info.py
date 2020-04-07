from covid import Covid
from googletrans import Translator

covid = Covid()

translator = Translator()


def worldInfo():
    text = f"<u>Статистика по миру</u>:\n\n" \
           f"<b>Всего случаев заболевания</b>: {str(covid.get_total_confirmed_cases())}\n\n" \
           f"<b>Всего активных зараженных</b>: {str(covid.get_total_active_cases())}\n\n" \
           f"<b>Всего Смертей</b>: {str(covid.get_total_deaths())}\n\n" \
           f"<b>Всего выздоровевших</b>: {str(covid.get_total_recovered())}"
    return text


def countryInfo(country):
    try:
        status = covid.get_status_by_country_name(country)
        text = f"<u>Статистика по стране:</u> <b>{translator.translate(status['country'], dest='ru').text}</b>\n\n" \
               f"<b>Всего случаев заболевания</b>: {status['confirmed']}\n\n" \
               f"<b>Всего активных зараженных</b>: {status['active']}\n\n" \
               f"<b>Всего Смертей</b>: {status['deaths']}\n\n" \
               f"<b>Всего выздоровевших</b>: {status['recovered']}\n"
        return text
    except ValueError:
        return "<b>Оопс.....</b>\n" \
               "Кажется Я не знаю такой страны"


# '<b>Подробную информацию можно получить</b> '
# '<a href = "https://coronavirus-spravka.ru/">на этом сайте</a>\n\n'
# "<b>Или по телефону горячей линии по коронавирусу в РФ</b>\n"
# "8(800)2000-112\n"