#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from Pages.base import WebPage
from Pages.elements import WebElement
from Pages.elements import ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://mevikon.ru/'

        super().__init__(web_driver, url)

    """Блок с новостями"""
    blok_news = WebElement(xpath='/html/body/div[1]/section[1]/div[1]')

    """Кнопка Записаться"""
    button_rec = WebElement(xpath='/html/body/div[1]/section[1]/div[1]/button')

    """Заголовок Уменя есть..."""
    heading = WebElement(xpath='//*[@id="section-chat"]/h2')

    """Блок1 'что тебя ждет на фесте'"""
    blok_4_card = WebElement(xpath='/html/body/div[1]/section[3]')

    """Кнопка Записаться на PRO-FEST блок 1"""
    button_rec_pro_fest = WebElement(xpath='/html/body/div[1]/section[3]/button')

    """Блок2 - Разыгрываем... (тело страницы)"""
    blok_4_card2 = WebElement(xpath='/html/body/div[1]/section[4]')

    """Кнопка Записаться на PRO-FEST блок 2"""
    button_rec_pro_fest2 = WebElement(xpath='/html/body/div[1]/section[4]/button')

    """Логотип в самом верху переход на Логин"""
    logotip_top_banner = WebElement(xpath='/html/body/div[1]/header/div/a/img')

    """Логотип внизу"""
    logotipe_ffoter = WebElement(xpath='/html/body/footer/div[1]/div[1]/div[1]/img')

    """Договор оферты ссылка"""
    dogovor = WebElement(xpath='/html/body/footer/div[1]/div[1]/div[2]/a[1]')

    """Политика конфиденциальности ссылка"""
    politic_conf = WebElement(xpath='/html/body/footer/div[1]/div[1]/div[2]/a[2]')



    """ЧАТ БОТ НА ГЛАВНОЙ СТРАНИЦЕ"""
    """Строка ввода в чат"""
    input_usser = WebElement(xpath='//*[@id="user-input"]')

    """Кнопка отправить Чат - бот"""
    button_send = WebElement(xpath='//*[@id="send-button"]')

    """Введеные данные юзером в чате"""
    respons_user = WebElement(xpath='//*[@id="chat-messages"]/div[2]/span')

    """Введеные данные юзером в чате второй цикл"""
    respons_user2 = WebElement(xpath='//*[@id="chat-messages"]/div[4]/span')

    """Введеные данные юзером в чат 3 цыкл"""
    respons_user3 = WebElement(xpath='//*[@id="chat-messages"]/div[6]/span')

    """Введеные данные юзером в чат 4 цыкл"""
    respons_user4 = WebElement(xpath='//*[@id="chat-messages"]/div[8]/span')

    """Введеные данные юзером в чат 5 цыкл"""
    respons_user5 = WebElement(xpath='//*[@id="chat-messages"]/div[10]/span')

    """Введеные данные юзером в чат 6 цыкл"""
    respons_user6 = WebElement(xpath='//*[@id="chat-messages"]/div[12]/span')

    """Введеные данные юзером в чат 7 цыкл"""
    respons_user7 = WebElement(xpath='//*[@id="chat-messages"]/div[14]/span')

    """Введеные данные юзером в чат 8 цыкл"""
    respons_user8 = WebElement(xpath='//*[@id="chat-messages"]/div[16]/span')

    """Кнопка Смотри результат"""
    button_rezultate = WebElement(xpath='//*[@id="btn-result"]')

    """Заголовок ДОСТИГАТОР..."""
    heading_dostigator = WebElement(xpath='//*[@id="popup-title"]')

    """Ссылка поделиться"""
    linc_podelitsa = WebElement(xpath='//*[@id="popup"]/div/div[1]/div/span')

    """Кнопка Забрать стиккеры"""
    button_zabrat_stik = WebElement(xpath='//*[@id="popup"]/div/div[2]/button')



    """СТРАНИЦА АВТОРИЗАЦИИ В АДМИН"""
    login = WebElement(xpath='/html/body/div[2]/form/input[2]')
    passw = WebElement(xpath='/html/body/div[2]/form/input[3]')
    button_enter = WebElement(xpath='/html/body/div[2]/form/button')