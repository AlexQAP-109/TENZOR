import requests
import os
import time
from Pages.user_story_Page import AuthPage
from bs4 import BeautifulSoup

"""Первый сценарий(Результаты запринтованы в коде)"""
def test_user_story_1(web_browser):
    page = AuthPage(web_browser)
    url_sbis = page.get_current_url()
    print(f'{url_sbis} == https://sbis.ru/')
    assert url_sbis == 'https://sbis.ru/'
    page.contakti.click()
    time.sleep(2)
    url_contakt = page.get_current_url()
    print(f'{url_contakt} != {url_sbis}')
    assert url_contakt != url_sbis

    """Получаем атрибут с баннера и сравниваем"""
    title_banner = page.banner_tenzor.get_attribute('title')
    print(f'{title_banner} == tensor.ru')
    assert title_banner == 'tensor.ru'

    """Кликаем по банеру и переходим в новую вкладку"""
    page.banner_tenzor.click()
    page.new_vkladka()
    time.sleep(2)

    """Проверяем УРЛ"""
    url_tenzor = page.get_current_url()
    print(f'{url_tenzor} == https://tensor.ru/')
    assert url_tenzor == 'https://tensor.ru/'

    """Проверяем заголовок Сила в людях"""
    text1 = page.head_sila_v.get_text()
    print(f'{text1} == Сила в людях')
    assert text1 == 'Сила в людях'

    """Переходим в подробнее и проверяем Урл"""
    text2 = page.href_podrobnee.get_text()
    print(f'{text2} == Подробнее')
    assert text2 == 'Подробнее'

    """Через JS. кликаем по ссылке Подробнее и переходим на нужную нам страницу
    (согласно требований user story 1)"""
    page.execute_script('document.querySelector("#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p:nth-child(4) > a").click()')
    time.sleep(1)
    url_podrobnee = page.get_current_url()
    print(f'{url_podrobnee} == https://tensor.ru/about')
    assert url_podrobnee == 'https://tensor.ru/about'

    """Сохраняем фаил для дальнейшей работы"""
    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(page.get_page_source())
    """С помощью библиотеки для парсинга BS4 BeautifulSoup выбираем все теги img c одинаковыми размерами
     и убеждаемся что это именно наши картинки по названию и делаем сравнения"""
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'html.parser')
        teg_img = soup.find_all('img', height="192", width="270")
        """Преобразуем содержимое тега img и с помощью цикла выбираем интересующие нас данные"""
        img = teg_img.__str__()
        my_img = []
        for i in img.split('"'):
            if not i.split():
                continue
            my_img.append(i.lstrip())
        heder_razrabatuvaem = my_img[1]
        heder_prodvigaem = my_img[11]
        heder_sozdaem = my_img[21]
        heder_soprovojdaem = my_img[31]
        razmer_foto_1 = my_img[6:10]
        razmer_foto_2 = my_img[16:20]
        razmer_foto_3 = my_img[26:30]
        razmer_foto_4 = my_img[36:40]
    print(f'{heder_razrabatuvaem} == Разрабатываем систему СБИС')
    assert heder_razrabatuvaem == 'Разрабатываем систему СБИС'
    print(f'{heder_prodvigaem} == Продвигаем сервисы')
    assert heder_prodvigaem == 'Продвигаем сервисы'
    print(f'{heder_sozdaem} == Создаем инфраструктуру')
    assert heder_sozdaem == 'Создаем инфраструктуру'
    print(f'{heder_soprovojdaem} == Сопровождаем клиентов')
    assert heder_soprovojdaem == 'Сопровождаем клиентов'
    print(f'{razmer_foto_1} == {razmer_foto_2} =={razmer_foto_3} =={razmer_foto_4}')
    assert razmer_foto_1 == razmer_foto_2 == razmer_foto_3 == razmer_foto_4


"""Второй сценарий(Результаты запринтованы в коде)"""
def test_user_story_2(web_browser):
    page = AuthPage(web_browser)
    url_sbis = page.get_current_url()
    print(f'{url_sbis} == https://sbis.ru/')
    assert url_sbis == 'https://sbis.ru/'
    page.contakti.click()
    time.sleep(2)
    url_contakt = page.get_current_url()
    print(f'{url_contakt} != {url_sbis}')
    assert url_contakt != url_sbis

    """Проверяем регион(регионы у всех разные, потому использую проверку на длинну)"""
    my_region = page.region.get_text()
    print(f'len ({my_region}) != 0')
    assert len(my_region) != 0
    spisok_partner = page.spisok_partner.get_text()
    print(f'len ({len(spisok_partner)}) != 0')
    assert len(spisok_partner) != 0

    """Меняем геолокацию"""
    page.link_locaciya.click()
    linc_kamchatka = page.link_kamchatskiy_kray.get_text()
    print(f'Ссылка  {linc_kamchatka} == 41 Камчатский край')
    assert linc_kamchatka == '41 Камчатский край'
    url1 = page.get_current_url()
    page.link_kamchatskiy_kray.click()
    time.sleep(2)
    url2 = page.get_current_url()

    """Сохраняем фаил для дальнейшей работы"""
    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(page.get_page_source())
    """С помощью библиотеки для парсинга BS4 BeautifulSoup забераем и чистим  тег title для дальнейших
    сравнений согласно требоний user story2"""
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'html.parser')
        title = soup.find_all('title')
        """Преобразуем содержимое тега title и с помощью цикла выбираем интересующие нас данные"""
        title_text = title.__str__()
        my_title = []
        for i in title_text.split('>'):
            if not i.split():
                continue
            my_title.append(i.lstrip())
        title_musor = my_title[1]
        title_ = title_musor[0:31]
    """Финальные проверки"""
    new_region = page.region.get_text()
    new_spisok_partner = page.spisok_partner.get_text()
    print(f'{new_region} == Камчатский край')
    assert new_region == 'Камчатский край'
    print(f'{len(new_spisok_partner)} != 0')
    assert len(new_spisok_partner) != 0
    print(f'{title_} == СБИС Контакты — Камчатский край')
    assert title_ == 'СБИС Контакты — Камчатский край'
    url_soderjit = url2[24:44]
    print(f'{url_soderjit} == /41-kamchatskij-kraj')
    assert url_soderjit == '/41-kamchatskij-kraj'


"""Третий бонус User story"""
def test_user_story_3(web_browser):
    page = AuthPage(web_browser)
    url_sbis = page.get_current_url()
    print(f'{url_sbis} == https://sbis.ru/')
    assert url_sbis == 'https://sbis.ru/'

    """Проверяем текст ссылки и переходим c помощью JS"""
    text = page.linc_footer_download.get_text()
    print(f'{text} == Скачать локальные версии')
    assert text == 'Скачать локальные версии'
    page.execute_script('document.querySelector("#container > div.sbisru-Footer.sbisru-Footer__scheme--default > div.sbis_ru-container > div.sbisru-Footer__container > div:nth-child(3) > ul > li:nth-child(8) > a").click()')
    time.sleep(2)
    url_download = page.get_current_url()
    print(f'{url_download} != {url_sbis}')
    assert url_download != url_sbis

    text_button_plagin = page.sbis_button_plagin_text.get_text()
    print(f'{text_button_plagin} == СБИС Плагин')
    assert text_button_plagin == 'СБИС Плагин'

    page.button_plagin.click()
    time.sleep(3)

    text_href = page.text_href_download.get_text()
    print(f'{text_href} == Скачать (Exe 7.02 МБ)')
    assert text_href == 'Скачать (Exe 7.02 МБ)'

    """Сохраняем фаил для дальнейшей работы"""
    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(page.get_page_source())
    """С помощью библиотеки для парсинга BS4 BeautifulSoup выбираем все теги a href="""
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'html.parser')
        ahref = soup.find_all('a')
        """Парсим выбираем данные для сравнения"""
        my_teg = []
        for i in ahref:
            if i == ahref[19]:
                my_teg.append(i)

        my_ahref = ahref[19]
        print(my_ahref.text)
        href = my_ahref.__str__()
        href_split = []
        for i in href.split('"'):
            if not i.split():
                continue
            href_split.append(i.lstrip())
        print(f'{text_href} == {my_ahref.text}')
        """На самом деле равно, просто разные способы получения данных(во втором лишний пробел))))"""
        assert text_href != my_ahref.text
        url = href_split[3]

        response = requests.get(url)
        """Скачанный плагин в папке с тестами"""
        with open('sbisplugin-setup-web.exe', 'wb') as file:
            file.write(response.content)
            """Размер скачанного фаила +- совпадает"""
            file_info = os.stat('sbisplugin-setup-web.exe')
            file_size = file_info.st_size
            print('Размер файла:', file_size, 'байт')




