import requests
from bs4 import BeautifulSoup

url = "https://coronavirus-spravka.ru/"
headers = {'User-Agent': open('headers').read()}
full_page = requests.get(url, headers)
info = BeautifulSoup(full_page.content, 'html.parser').find_all('div', {'class': "col-4 text-center"})
sub = BeautifulSoup(full_page.content, 'html.parser').find_all('tr')
sub_info = BeautifulSoup(full_page.content, 'html.parser').find('div', {'class': "table-responsive table-color"})
sub_list = []
for x in range(9, 88):
    sub_list.append(sub[x].text)


def cases():
    total_cases_ru = []
    for i in filter(str.isdigit, list(info[0])[3]):
        total_cases_ru.append(i)
    return total_cases_ru[0]


def deaths():
    total_deaths_ru = []
    for i in filter(str.isdigit, list(info[1])[3]):
        total_deaths_ru.append(i)
    return total_deaths_ru[0]


def recovered():
    total_recovered_ru = []
    for i in filter(str.isdigit, list(info[2])[3]):
        total_recovered_ru.append(i)
    return total_recovered_ru[0]


def your_region_info(region):
    pass


print("Забоолевших", "Умерших", "Выздоровевших")
print(cases(), deaths(), recovered())
