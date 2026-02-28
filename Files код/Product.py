from datetime import (
    datetime,
)


class Product:
    """Класс для управления партией товара."""

    ALLOWED_LOCATIONS = ['507 E 9th St', '201 N Tryon St', '551 S Tryon St', '750 E 9th St', 'Склад', 'Магазин',
                         'В пути']
    ALLOWED_CATEGORIES = ['electronics', 'food', 'jewelery', 'medicines', 'Не указана']
    ALLOWED_CITIES = [
        'Москва', 'Санкт-Петербург', 'Екатеринбург', 'Новосибирск',
        'Ростов-на-Дону', 'Краснодар', 'Нижний Новгород', 'Самара',
        'Омск', 'Уфа', 'Челябинск', 'Красноярск', 'Воронеж',
        'Саратов', 'Пермь', 'Иркутск', 'Хабаровск', 'Владивосток',
        'Ярославль', 'Тюмень', 'Калининград', 'Оренбург', 'Сочи',
        'Белгород', 'Астрахань', 'Пенза', 'Саранск', 'Махачкала',
        'Магнитогорск', 'Тольятти'
    ]

    def __init__(self, number: int = 0, name: str = 'Не указано', quantity: int = 0, condition: str = 'Не указано',
                 supplier: str = 'Не указан', manufacturer: str = 'Не указан', cost: int = 0,
                 location: str = 'Не указан', expiry_date: str = 'Не указана', category: str = 'Не указана',
                 city: str = 'Не указан', note: str = 'Не указана') -> None:
        """Инициализация карточки товара."""

        self.number = str(number)
        self.id = f'T{int(number):04}'
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
        """Устанавливает название товара."""

        if name:
            self.name = name
        else:
            raise ValueError('Имя должно состоять хотя бы из одного символа')

    def set_quantity(self, quantity: str) -> None:
        """Устанавливает количество товара."""

        try:
            val = int(quantity)
        except ValueError:
            raise ValueError(f'Количество должно быть целым числом. Получено: "{quantity}"')

        if val < 0:
            raise ValueError('Количество не может быть отрицательным')

        self.quantity = val

    def set_supplier(self, supplier: str) -> None:
        """Устанавливает поставщика товара."""

        self.supplier = supplier

    def set_manufacturer(self, manufacturer: str) -> None:
        """Устанавливает производителя товара."""

        self.manufacturer = manufacturer

    def set_cost(self, cost: str) -> None:
        """Устанавливает стоимость товара."""

        try:
            clean_cost = str(cost).replace('руб', '').replace('.', '').strip()
            val = int(clean_cost)
        except ValueError:
            raise ValueError(f'Стоимость должна быть целым числом. Получено: "{cost}"')

        if val < 0:
            raise ValueError('Стоимость не может быть отрицательной')

        self.cost = val

    def set_location(self, location: str) -> None:
        """Устанавливает местоположение товара на складе."""

        if location not in self.ALLOWED_LOCATIONS:
            raise ValueError(f'Недопустимая локация: "{location}".')

        self.location = location

    def set_expiry_date(self, expiry_date: str) -> None:
        """Устанавливает срок годности товара."""

        try:
            datetime.strptime(expiry_date, '%d.%m.%Y')

        except ValueError:
            raise ValueError('Некорректный формат даты. Используйте ДД.ММ.ГГГГ')

        self.expiry_date = expiry_date

    def set_category(self, category: str) -> None:
        """Устанавливает категорию товара."""

        if category not in self.ALLOWED_CATEGORIES:
            raise ValueError(f'Неизвестная категория "{category}".')

        self.category = category

    def set_condition(self, condition: str) -> None:
        """Устанавливает состояние товара."""

        self.condition = title(condition)

    def set_city(self, city: str) -> None:
        """Устанавливает город."""

        self.city = title(city)

        if city not in self.ALLOWED_CITIES:
            raise ValueError(f'Неизвестный город "{city}".')

        self.city = city

    def set_note(self, note: str) -> None:
        """Добавляет примечание к товару."""

        self.note = note

    def get_dict(self) -> dict:
        """Возвращает словарное представление полной информации о товаре.

        Returns:
            dict: Информация о товаре.
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
