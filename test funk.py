'''Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.

1. Спрашивать у пользователя первоначальный запрос.

2. Переходить по первоначальному запросу в Википедии.

3. Предлагать пользователю три варианта действий:

листать параграфы текущей статьи;
перейти на одну из связанных страниц — и снова выбор из двух пунктов:
- листать параграфы статьи;

- перейти на одну из внутренних статей.

выйти из программы.'''

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random
import time

wiki_url = ''
browser = webdriver.Chrome()
browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
def close():
    quit()

def par():
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')
    for paragraph in paragraphs:
        print(paragraph.text)
        input()
        menu()

def go_page():
    hatnotes = []

    for element in browser.find_elements(By.TAG_NAME, 'div'):
        cl = element.get_attribute('class')
        if cl == 'hatnote navigation-not-searchable ts-main':
            hatnotes.append(element)

    print(hatnotes)
    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, 'a').get_attribute('href')
    browser.get(link)
    time.sleep(1)

    menu()


def menu():
    menu = input('Листать параграфы (Введите П)\n'  
          'Перейти на одну из внутренних статей (Введите С)\n'
          'Хотите закрыть программу?(Введите Д)')

    if menu == 'Д':  # Закрыть
        close()

    if menu == 'П':  # Листать
        par()

    if menu == 'С':  # Перейти
        go_page()

try:
    while True:

        ask = input('Введите свой первоначальный запрос:')

        assert 'Википедия' in browser.title
        time.sleep(1)
        search_box = browser.find_element(By.ID, 'searchInput')
        search_box.send_keys(ask)
        time.sleep(1)
        search_box.send_keys(Keys.RETURN)
        menu()

except:
    print('Произошла ошибка')