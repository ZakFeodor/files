import json
from Product import Product


class TXTTOJSON:

    def __init__(self, file_name):
        self.file_name = file_name
    
    def read_txt(self):
        
        with open(f'{self.file_name}.txt', 'r', encoding='UTF-8') as self.file:
            list_of_rows = []
            for line in self.file.readlines():
                rows = line.rstrip().split(';')
                list_of_rows.append(rows)
            main_row = list_of_rows.pop(0)
            dict_from_txt = {}
            list_of_dicts_of_rows = []
            for row in list_of_rows:
                for column_number in range(len(main_row)):
                    dict_from_txt[main_row[column_number]] = row[column_number]
                copy_dict_from_txt = dict_from_txt.copy()
                list_of_dicts_of_rows.append(copy_dict_from_txt)

            self.list_of_dicts_of_rows = list_of_dicts_of_rows
            self.__write_txt_rows_in_json()

            return self.list_of_dicts_of_rows
    
    def __write_txt_rows_in_json(self):
        with open('data.json', 'w') as self.file:
            json.dump(self.list_of_dicts_of_rows, self.file, indent=4, ensure_ascii=False)

    def create_dict_of_objects(self):
        dict_of_objects = {}

        for card in self.list_of_dicts_of_rows:
            dict_of_objects[card['№']] = Product(card['№'], card['Наименование'], card['Количество'], card['Состояние'],
            card['Поставщик'], card['Производитель'], card['Стоимость'], card['Местоположение'], city=card['Город'])

        return dict_of_objects


