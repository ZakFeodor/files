from read_txt import (
    TXTTOJSON,
)
from Product import (
    Product,
)
from json_interact import (
    JSONINTERACT,
)


def interact_with_product(product: Product) -> None:
    """Функция для взаимодействия с карточкой товара.

    Позволяет пользователю изменять поля переданного объекта Product
    через консольное меню.

    Args:
        product: Объект класса Product, который нужно изменить.
    """

    menu = '''1. Изменить название
2. Изменить количество
3. Изменить состояние
4. Изменить поставщика
5. Изменить производителя
6. Изменить стоимость
7. Изменить местоположение (адрес)
8. Изменить город
9. Изменить срок годности
10. Изменить категорию
11. Добавить примечание
12. Получить полную информацию о карточке товара
13. Назад
'''

    user_choice = 0

    while user_choice != 13:

        try:
            user_choice = int(input(menu))

            if user_choice not in range(1, 14):

                raise ValueError('Выберите число от 1 до 13')

        except ValueError as ve:
            print(ve)

            continue

        user_change = None

        if 1 <= user_choice <= 11:
            user_change = input('Введите новое значение: ')

        try:
            match user_choice:
                case 1:
                    product.set_name(user_change)
                case 2:
                    product.set_quantity(user_change)
                case 3:
                    product.set_condition(user_change)
                case 4:
                    product.set_supplier(user_change)
                case 5:
                    product.set_manufacturer(user_change)
                case 6:
                    product.set_cost(user_change)
                case 7:
                    product.set_location(user_change)
                case 8:
                    product.set_city(user_change)
                case 9:
                    product.set_expiry_date(user_change)
                case 10:
                    product.set_category(user_change)
                case 11:
                    product.set_note(user_change)
                case 12:
                    print(product.get_dict())

        except ValueError as ve:
            print(f'Ошибка при изменении данных: {ve}')


if __name__ == '__main__':
    txt = TXTTOJSON('data')
    cards = txt.read_txt()
    json_file = JSONINTERACT('data')
    dict_of_objects = txt.create_dict_of_objects()

    menu_for_cards = '''1. Выбрать существующую карточку
2. Добавить новую карточку
3. Выйти из программы
'''

    user_card_choice = 0
    user_product_choice = -1

    while user_card_choice != 3:
        print(menu_for_cards)

        try:
            user_card_choice = int(input('Введите номер одного из возможных действий: '))

            if user_card_choice not in range(1, 4):

                raise ValueError('Выберите число от 1 до 3')

        except ValueError as ve:
            print(ve)

            continue

        cards_for_user = []
        max_possible_number_of_card = 0

        for card in cards:
            if int(card['№']) > max_possible_number_of_card:
                max_possible_number_of_card = int(card['№'])

            cards_for_user.append({card['№']: card['Наименование']})

        match user_card_choice:
            case 1:
                flag_user_product_choice = True

                while flag_user_product_choice:
                    for card in cards_for_user:
                        print(f'Номер карты: {list(card.keys())[0]}, Наименование товара: {list(card.values())[0]}')

                    try:
                        user_product_choice = int(input('Введите номер необходимой карты или 0 для перехода назад: '))

                    except ValueError:
                        print('Введите число.')

                        continue

                    if user_product_choice == 0:
                        flag_user_product_choice = False

                        continue

                    if str(user_product_choice) not in dict_of_objects:
                        print('Такой карточки не существует.')

                        continue

                    new_product = dict_of_objects[str(user_product_choice)]

                    interact_with_product(new_product)

                    cards = []

                    for obj in dict_of_objects.values():
                        cards.append(obj.get_dict())

                    json_file.write_row_in_json(cards)

            case 2:
                max_possible_number_of_card += 1
                new_product = Product(number=max_possible_number_of_card)

                print(f'''Создана карточка с номером {max_possible_number_of_card}
Начните заполнение карточки, выберите одно из действий, описанных ниже: ''')

                interact_with_product(new_product)

                dict_of_objects[str(max_possible_number_of_card)] = new_product

                cards = []

                for obj in dict_of_objects.values():
                    cards.append(obj.get_dict())

                json_file.write_row_in_json(cards)

            case 3:
                print("Выход из программы.")