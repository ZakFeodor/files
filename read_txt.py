import json
from Product import (
    Product,
)


class TxtInteract:
    """Класс для взаимодействия с файлом формата txt."""

    def __init__(self, file_name: str) -> None:
        """Инициализация класса.

        Args:
            file_name: Имя файла (без расширения).
        """

        self.file_name = file_name
        self.list_of_dicts_of_rows = []

    def deserialize(self) -> list:
        """Считывает данные из txt, преобразует типы и сохраняет в JSON.

        Returns:
            list: Список словарей с данными товаров.
        """

        with open(f'{self.file_name}.txt', 'r', encoding='UTF-8') as file:
            lines = file.readlines()

        if not lines:
            return []

        headers = lines.pop(0).rstrip().split(';')

        list_of_dicts_of_rows = []

        for line in lines:
            values = line.rstrip().split(';')
            row_dict = {}

            for i in range(len(headers)):
                key = headers[i]
                val = values[i]

                if key == 'Количество':
                    try:
                        val = int(val.strip())
                    except ValueError:
                        val = 0

                elif key == 'Стоимость':
                    try:
                        clean_val = val.replace('руб.', '').replace('руб', '').strip()
                        val = int(clean_val)
                    except ValueError:
                        val = 0

                row_dict[key] = val

            list_of_dicts_of_rows.append(row_dict)

        self.list_of_dicts_of_rows = list_of_dicts_of_rows
        self.__write_txt_rows_in_json()

        return self.list_of_dicts_of_rows

    def __write_txt_rows_in_json(self) -> None:
        """Записывает обработанные данные в JSON файл."""

        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(self.list_of_dicts_of_rows, file, indent=4, ensure_ascii=False)

    def create_dict_of_objects(self) -> dict:
        """Создает словарь объектов Product из загруженных данных.

        Returns:
            dict: Словарь вида {'номер_товара': объект_Product}.
        """

        dict_of_objects = {}

        for card in self.list_of_dicts_of_rows:
            dict_of_objects[str(card['№'])] = Product(
                number=int(card['№']),
                name=card['Наименование'],
                quantity=card['Количество'],
                condition=card['Состояние'],
                supplier=card['Поставщик'],
                manufacturer=card['Производитель'],
                cost=card['Стоимость'],
                location=card['Местоположение'],
                city=card['Город']
            )

        return dict_of_objects
