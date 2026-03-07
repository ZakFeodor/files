from datetime import datetime


class Product:
    """Класс для управления партией товара."""

    LIST_OF_POSSIBLE_LOCATIONS = ['Склад', 'Магазин', 'В пути']
    LIST_OF_POSSIBLE_CATEGORIES = ['Электроника', 'Еда', 'Ювелирия',
                                   'Медикаменты', 'Не указана']
    LIST_OF_POSSIBLE_CITIES = [
        'Москва', 'Санкт-Петербург', 'Екатеринбург', 'Новосибирск',
        'Ростов-на-Дону', 'Краснодар', 'Нижний Новгород', 'Самара',
        'Омск', 'Уфа', 'Челябинск', 'Красноярск', 'Воронеж',
        'Саратов', 'Пермь', 'Иркутск', 'Хабаровск', 'Владивосток',
        'Ярославль', 'Тюмень', 'Калининград', 'Оренбург', 'Сочи',
        'Белгород', 'Астрахань', 'Пенза', 'Саранск', 'Махачкала',
        'Магнитогорск', 'Тольятти'
    ]

    def __init__(self, number: int = 0, name: str = 'Не указано',
                 quantity: int = 0, condition: str = 'Не указано',
                 supplier: str = 'Не указан', manufacturer: str = 'Не указан',
                 cost: int = 0, location: str = 'Не указан',
                 expiry_date: str = 'Не указана',
                 category: str = 'Не указана',
                 city: str = 'Не указан', note: str = 'Не указана') -> None:
        """Инициализация карточки товара.

        Args:
            number (int, optional): Уникальный номер товара. По умолчанию 0.
            name (str, optional): Название товара. По умолчанию 'Не указано'.
            quantity (int, optional): Количество товара. По умолчанию 0.
            condition (str, optional): Состояние товара. По умолчанию 'Не указано'.
            supplier (str, optional): Поставщик товара. По умолчанию 'Не указан'.
            manufacturer (str, optional): Производитель товара. По умолчанию 'Не указан'.
            cost (int, optional): Стоимость товара. По умолчанию 0.
            location (str, optional): Местоположение товара. По умолчанию 'Не указан'.
            expiry_date (str, optional): Срок годности. По умолчанию 'Не указана'.
            category (str, optional): Категория товара. По умолчанию 'Не указана'.
            city (str, optional): Город нахождения. По умолчанию 'Не указан'.
            note (str, optional): Примечание к товару. По умолчанию 'Не указана'.
        """

        self.number = number
        self.id = f'T{number:04}'
        self.name = name
        self.quantity = quantity
        self.condition = condition
        self.supplier = supplier
        self.manufacturer = manufacturer
        self.cost = cost
        self.location = location
        self.expiry_date = expiry_date
        self.category = category
        self.city = city
        self.note = note

    def set_name(self, name: str) -> None:
        """Устанавливает название товара.

        Args:
            name (str): Название товара.

        Raises:
            ValueError: Если имя пустое или равно None.
        """

        if name:
            self.name = name
        else:
            raise ValueError('Имя должно состоять хотя бы из одного символа')

    def set_quantity(self, quantity: int) -> None:
        """Устанавливает количество товара.

        Args:
            quantity (int): Количество товара.

        Raises:
            ValueError: Если передано не целое число или число меньше нуля.
        """

        try:
            val = int(quantity)
        except ValueError:
            raise ValueError(f'Количество должно быть целым числом. Получено: "{quantity}"')

        if val < 0:
            raise ValueError('Количество не может быть отрицательным')
        else:
            self.quantity = val

    def set_supplier(self, supplier: str) -> None:
        """Устанавливает поставщика товара.

        Args:
            supplier (str): Название поставщика.

        Raises:
            ValueError: Если название поставщика пустое.
        """

        if supplier:
            self.supplier = supplier
        else:
            raise ValueError('Название поставщика должно состоять хотя бы из одного символа')

    def set_manufacturer(self, manufacturer: str) -> None:
        """Устанавливает производителя товара.

        Args:
            manufacturer (str): Название производителя.

        Raises:
            ValueError: Если название производителя пустое.
        """

        if manufacturer:
            self.manufacturer = manufacturer
        else:
            raise ValueError('Название производителя должно состоять хотя бы из одного символа')

    def set_cost(self, cost: int) -> None:
        """Устанавливает стоимость товара.

        Очищает строку от 'руб' и '.' перед преобразованием.

        Args:
            cost (int): Стоимость товара.

        Raises:
            ValueError: Если передано не число или число меньше нуля.
        """

        try:
            clean_cost = str(cost).replace('руб', '').replace('.', '').strip()
            val = int(clean_cost)
        except ValueError:
            raise ValueError(f'Стоимость должна быть целым числом. Получено: "{cost}"')

        if val < 0:
            raise ValueError('Стоимость не может быть отрицательной')
        else:
            self.cost = val

    def set_location(self, location: str) -> None:
        """Устанавливает местоположение товара на складе.

        Проверяет наличие локации в списке допустимых значений.

        Args:
            location (str): Местоположение.

        Raises:
            ValueError: Если локации нет в списке допустимых.
        """

        if location not in self.LIST_OF_POSSIBLE_LOCATIONS:
            raise ValueError(f'Недопустимая локация: "{location}".')
        else:
            self.location = location

    def set_expiry_date(self, expiry_date: str) -> None:
        """Устанавливает срок годности товара.

        Args:
            expiry_date (str): Дата в формате 'ДД.ММ.ГГГГ'.

        Raises:
            ValueError: Если формат даты некорректен.
        """

        try:
            datetime.strptime(expiry_date, '%d.%m.%Y')
        except ValueError:
            raise ValueError('Некорректный формат даты. Используйте ДД.ММ.ГГГГ')
        else:
            self.expiry_date = expiry_date

    def set_category(self, category: str) -> None:
        """Устанавливает категорию товара.

        Args:
            category (str): Категория товара.

        Raises:
            ValueError: Если категории нет в списке допустимых.
        """

        if category not in self.LIST_OF_POSSIBLE_CATEGORIES:
            raise ValueError(f'Неизвестная категория "{category}".')
        else:
            self.category = category

    def set_condition(self, condition: str) -> None:
        """Устанавливает состояние товара.


        Args:
            condition (str): Состояние товара.

        Raises:
            ValueError: Если название состояния пустое
        """

        if condition:
            self.condition = condition
        else:
            raise ValueError('Состояние должно состоять хотя бы из одного символа')

    def set_city(self, city: str) -> None:
        """Устанавливает город нахождения товара.

        Args:
            city (str): Название города.

        Raises:
            ValueError: Если города нет в списке допустимых.
        """

        if city not in self.LIST_OF_POSSIBLE_CITIES:
            raise ValueError(f'Неизвестный город "{city}".')
        else:
            self.city = city

    def set_note(self, note: str) -> None:
        """Добавляет примечание к товару.

        Args:
            note (str): Текст примечания.
        """

        self.note = note

    def get_dict(self) -> dict:
        """Возвращает словарное представление полной информации о товаре.

        Returns:
            dict: Словарь, содержащий все атрибуты товара (№, ID, Наименование и т.д.).
        """

        return {
            "№": self.number,
            "ID": self.id,
            "Наименование": self.name,
            "Количество": self.quantity,
            "Состояние": self.condition,
            "Поставщик": self.supplier,
            "Производитель": self.manufacturer,
            "Стоимость": self.cost,
            "Местоположение": self.location,
            "Город": self.city,
            "Срок годности": self.expiry_date,
            "Заметка": self.note
        }
