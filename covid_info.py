from covid import Covid
from googletrans import Translator

covid = Covid()

translator = Translator()


def worldInfo():
    text = "<b>Статистика по миру:</b>\n\n" \
           f"<b><u>Всего случаев заболевания</u></b>: {str(covid.get_total_confirmed_cases())}\n\n" \
           f"<b><u>Всего активных зараженных</u></b>: {str(covid.get_total_active_cases())}\n\n" \
           f"<b><u>Всего Смертей</u></b>: {str(covid.get_total_deaths())}\n\n" \
           f"<b><u>Всего выздоровевших</u></b>: {str(covid.get_total_recovered())}"
    return text


def countryInfo(country):
    try:
        status = covid.get_status_by_country_name(country)
        text = f"<u>Страна</u>: <b>{translator.translate(status['country'], dest='ru').text}</b>\n\n" \
               f"<b><u>Всего случаев заболевания</u></b>: {status['confirmed']}\n\n" \
               f"<b><u>Всего активных зараженных</u></b>: {status['active']}\n\n" \
               f"<b><u>Всего Смертей</u></b>: {status['deaths']}\n\n" \
               f"<b><u>Всего выздоровевших</u></b>: {status['recovered']}\n" \
               f"----------------------------------------------------\n" \
               f'Кстати!\n' \
               f'Узнать чем можно заняться во время самоизоляции можно в ' \
               f'<a href="https://t.me/ClassesForAllOccasions"> нашем телеграм канале</a>'
        return text
    except ValueError:
        return "<b>Оопс.....</b>\n" \
               "Кажется Я не знаю такой страны"
