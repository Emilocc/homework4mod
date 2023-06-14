# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, "xml")
#
#
# def get_course(course_id):
#     return soup.find("Valute", ID=course_id).Value.text

import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "xml")


def get_course(currency):
    currency_code = {
        "доллар": "USD",
        "евро": "EUR",
        "юань":"CNY"
    }
    course_id = currency_code.get(currency.lower())
    if course_id:
        return soup.find("Valute", ID=course_id).Value.text
    else:
        return f"Курс для валюты '{currency}' не найден"
