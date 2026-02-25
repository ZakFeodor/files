from datetime import datetime


class Product:
    """Класс для управления партией товара."""

    ALLOWED_CITIES = [
        'Москва', 'Санкт-Петербург', 'Екатеринбург', 'Новосибирск',
        'Ростов-на-Дону', 'Краснодар', 'Нижний Новгород', 'Самара',
        'Омск', 'Уфа', 'Челябинск', 'Красноярск', 'Воронеж',
        'Саратов', 'Пермь', 'Иркутск', 'Хабаровск', 'Владивосток',
        'Ярославль', 'Тюмень', 'Калининград', 'Оренбург', 'Сочи',
        'Белгород', 'Астрахань', 'Пенза', 'Саранск', 'Махачкала',
        'Магнитогорск', 'Тольятти'
    ]

    ALLOWED_LOCATIONS = [
        'Склад', 'Магазин', 'В пути', '507 E 9th St',
        '201 N Tryon St', '551 S Tryon St'
    ]

    ALLOWED_CATEGORIES = [
        'electronics', 'food', 'jewelery', 'medicines',
        'Не указана', 'furniture', 'clothing'
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

    def set_name(self, name: str):
        """Устанавливает название товара."""

        if name and str(name).strip():
            self.name = name
        else:
            raise ValueError('Имя должно состоять хотя бы из одного символа')

    def set_quantity(self, quantity: str):
        """Устанавливает количество товара (int)."""

        try:
            val = int(quantity)

        except ValueError:
            raise ValueError(f'Количество должно быть целым числом. Получено: "{quantity}"')

        if val < 0:
            raise ValueError('Количество не может быть отрицательным')

        self.quantity = val

    def set_cost(self, cost: str):
        """Устанавливает стоимость товара (int)."""

        try:
            clean_cost = str(cost).replace('руб', '').replace('.', '').strip()
            val = int(clean_cost)

        except ValueError:
            raise ValueError(f'Стоимость должна быть целым числом. Получено: "{cost}"')

        if val < 0:
            raise ValueError('Стоимость не может быть отрицательной')

        self.cost = val

    def set_supplier(self, supplier: str):
        """Устанавливает поставщика товара."""

        if not supplier.strip():
            raise ValueError('Поле "Поставщик" не может быть пустым')

        self.supplier = supplier

    def set_manufacturer(self, manufacturer: str):
        """Устанавливает производителя товара."""

        if not manufacturer.strip():
            raise ValueError('Поле "Производитель" не может быть пустым')

        self.manufacturer = manufacturer

    def set_location(self, location: str):
        """Устанавливает местоположение товара на складе.
        Проверяет наличие локации в списке допустимых.
        """

        if location not in self.ALLOWED_LOCATIONS:
            valid_list = ", ".join(self.ALLOWED_LOCATIONS)

            raise ValueError(f'Недопустимая локация: "{location}".\nДоступные варианты: {valid_list}')

        self.location = location

    def set_city(self, city: str):
        """Устанавливает город.
        Проверяет наличие города в списке обслуживаемых городов.
        """

        formatted_city = city.strip().title()

        if formatted_city not in self.ALLOWED_CITIES:
            raise ValueError(f'Город "{city}" не обслуживается или написан с ошибкой.')

        self.city = formatted_city

    def set_category(self, category: str):
        """Устанавливает категорию товара."""

        if category not in self.ALLOWED_CATEGORIES:
            valid_list = ", ".join(self.ALLOWED_CATEGORIES)

            raise ValueError(f'Неизвестная категория "{category}".\nДоступные: {valid_list}')

        self.category = category

    def set_expiry_date(self, expiry_date: str):
        """Устанавливает срок годности товара (ДД.ММ.ГГГГ)."""

        try:
            datetime.strptime(expiry_date, '%d.%m.%Y')

        except ValueError:
            raise ValueError('Некорректный формат даты. Используйте ДД.ММ.ГГГГ (например, 31.12.2023)')

        self.expiry_date = expiry_date

    def set_condition(self, condition: str):
        """Устанавливает состояние товара."""

        if not condition.strip():
            raise ValueError('Состояние не может быть пустым')

        self.condition = condition

    def set_note(self, note: str):
        """Добавляет примечание к товару."""

        self.note = note

    def get_dict(self):
        """Возвращает словарь. Преобразует числа в строки для JSON (если нужно)."""

        return {
            "№": self.number,
            "ID": self.id,
            "Наименование": self.name,
            "Количество": str(self.quantity),
            "Состояние": self.condition,
            "Поставщик": self.supplier,
            "Производитель": self.manufacturer,
            "Стоимость": f"{self.cost} руб.",
            "Местоположение": self.location,
            "Город": self.city,
            "Срок годности": self.expiry_date,
            "Заметка": self.note
        }