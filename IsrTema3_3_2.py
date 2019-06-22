from urllib.request import urlopen
from xml.etree import ElementTree as ET
import json

class CurrenciesXMLData():
    """Получаем данные XML"""
    def transmutation(self):
        currencies_ids_lst = ['R01239', 'R01235', 'R01035', 'R01010', 'R01090',
                              'R01335', 'R01350', 'R01535', 'R01625', 'R01700']

        cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")

        result = {}

        cur_res_xml = ET.parse(cur_res_str)

        root = cur_res_xml.getroot()
        valutes = root.findall('Valute')
        for el in valutes:
            valute_id = el.get('ID')

            if str(valute_id) in currencies_ids_lst:
                valute_cur_val = el.find('Value').text
                valute_cur_n = el.find('Name').text
                result[valute_id] = valute_cur_n, valute_cur_val
        return result

class CurrenciesJSONData():
    """Декоратор"""
    def __init__(self, obj):
        self.obj = obj

    def transmutation(self):
        self.obj = json.dumps(self.obj.transmutation(), ensure_ascii=False)
        return self.obj

    def serialize(self):
        with open('data.json', 'w', encoding='utf-8') as outfile:
            json.dump(self.obj, outfile, ensure_ascii=False, indent=2)
        print('Учпешно сохранено в файл!')
        pass

comp = CurrenciesXMLData()
comp = CurrenciesJSONData(comp)
print(comp.transmutation())
comp.serialize()