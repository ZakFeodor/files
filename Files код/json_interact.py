import json


class JsonInteract:
    """Класс для взаимодействия с JSON файлами."""

    def __init__(self, file_name: str) -> None:
        """Инициализация класса.

        Args:
            file_name: Имя файла (без расширения).
        """

        self.file_name = file_name

    def serialize(self, row: list) -> None:
        """Записывает данные в JSON файл.

        Args:
            row: Список словарей с данными карточек.
        """

        with open(f'{self.file_name}.json', 'w', encoding='utf-8') as file:
            json.dump(row, file, indent=4, ensure_ascii=False)

    def deserialize(self, number_of_card: int) -> dict | None:
        """Ищет карточку по номру в JSON файле.

        Args:
            number_of_card: Номер искомой карточки.

        Returns:
            dict: Словарь с данными карточки.
            None: Если карточка не найдена.
        """

        with open(f'{self.file_name}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for card in data:
                if int(card['№']) == number_of_card:
                    return card

            return None

    def delete_card(self, number_of_card: int) -> None:
        """Удаляет карточку по номеру из JSON файла.
        Args:
            number_of_card: Номер удаляемой карточки.
        """

        with open(f'{self.file_name}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        new_data = [card for card in data if int(card['№']) != number_of_card]

        self.serialize(new_data)