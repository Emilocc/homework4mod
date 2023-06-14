import requests
import xml.etree.ElementTree as ET

url = "http://www.cbr.ru/scripts/XML_daily.asp"
response = requests.get(url)

tree = ET.fromstring(response.content)

for valute in tree.iter('Valute'):
    valute_id = valute.attrib['ID']
    valute_name = valute.find('Name').text
    print(valute_id, valute_name)
