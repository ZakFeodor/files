import json


class JSONINTERACT:

    def __init__(self, file_name: str):
        self.file_name = file_name

    def change_category_of_card_in_json(self, number_of_card, category, change):
        with open(f'{self.file_name}.json', 'r') as file:
            data = json.load(file)
            for index_data in range(len(data)):
                if int(data[index_data]['№']) == number_of_card:
                    needed_card = data[index_data]

                    break
            needed_card.update({category: change})
            data[index_data] = needed_card
            self.write_row_in_json(data)

    def write_row_in_json(self, row):
        with open(f'{self.file_name}.json', 'w') as self.file:
            json.dump(row, self.file, indent=4, ensure_ascii=False)

    def get_card_from_json_by_number(self, number_of_card):
        with open(f'{self.file_name}.json', 'r') as file:
            data = json.load(file)

            for card in data:
                if int(card['№']) == number_of_card:

                    return card
