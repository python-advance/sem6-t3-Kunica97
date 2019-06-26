from urllib.request import urlopen
from xml.etree import ElementTree as ET

class CurrencyBoard:
    __instance = None # создаём переменную, в которую

    @staticmethod
    def getInstance():
        if CurrencyBoard.__instance == None: # проверяем на наличие данных
            CurrencyBoard()
        return CurrencyBoard.__instance

    def __init__(self):
        if CurrencyBoard.__instance == None:
            currencies_ids_lst = ['R01239', 'R01235', 'R01035', 'R01010', 'R01090', # список id валют
                                  'R01335', 'R01350', 'R01535', 'R01625', 'R01700'] # которые мы сами выбрали
            cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp") # получаем данные с сервера
            result = {} # создаём словарь
            cur_res_xml = ET.parse(cur_res_str) # парсим полученные данные
            root = cur_res_xml.getroot() # находим корневой элемент
            valutes = root.findall('Valute') # находим элементы с соответствующим тегом
            for el in valutes:
                valute_id = el.get('ID') # получаем все id
                if str(valute_id) in currencies_ids_lst: # находим наши id в списке всех id
                    valute_cur_val = el.find('Value').text # записываем значение курса валют
                    valute_cur_n = el.find('Name').text # записываем названия соответствующих курсов валют
                    result[valute_id] = valute_cur_n, valute_cur_val # записываем полученные данные в словарь
            CurrencyBoard.__instance = result # присваиваем переменной __instance значение словаря

a = CurrencyBoard()
print(a)

b = CurrencyBoard.getInstance()
print (b)

c = CurrencyBoard.getInstance()
print (c)
assert id(b) == id(c) # сверяем значения адресов переменных
print(id(b), id(c))
