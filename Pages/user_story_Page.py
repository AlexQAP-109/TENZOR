import os

from Pages.base import WebPage
from Pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://sbis.ru/'

        super().__init__(web_driver, url)

    """Ссылка контакты"""
    contakti = WebElement(xpath='//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a')

    """Баннер Тензор"""
    banner_tenzor = WebElement(xpath='//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')

    """Сила в людях..."""
    bloc_sila = WebElement(xpath='//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div')

    """Заголовок Сила в людях"""
    head_sila_v = WebElement(xpath='//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')

    """Ссылка ПОДРОБНЕЕ"""
    href_podrobnee = WebElement(xpath='//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')

    images = WebElement(xpath='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img')

    region = WebElement(xpath='//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')

    spisok_partner = WebElement(xpath='//*[@id="contacts_list"]/div/div[2]/div[1]/div')

    link_locaciya = WebElement(xpath='//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')

    link_kamchatskiy_kray = WebElement(xpath='//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span')

    title_kamchatka = WebElement(xpath='/html/head/title')

    linc_footer_download = WebElement(xpath='//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a')

    sbis_button_plagin_text = WebElement(xpath='/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]/div[1]')

    button_plagin = WebElement(xpath='/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]')

    text_href_download = WebElement(xpath='/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')



