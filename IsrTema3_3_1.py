from urllib.request import urlopen
from xml.etree import ElementTree as ET

class CurrencyBoard:
    __instance = None
    def __init__(self):
        if not CurrencyBoard.__instance:
            print('Делаем запрос')
        else:
            print('Запрос уже был сделан:', self.update())
    @classmethod
    def update(cls):
        if not cls.__instance:
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
            cls.__instance = result
        return cls.__instance

# инициализируем класс и выводим значения, чтобы выводились только
# наименования валют и текущий курс, используем .value(), так как получаем словарь

print(CurrencyBoard.update().values())

# проверяем, посылается ли запрос второй раз. В случае успеха,
# консоль выведет "Запрос уже был сделан", с демонстрацией хранимых данных
CurrencyBoard()