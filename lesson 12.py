#12.1
import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = re.sub(r'<.*?>', '', html)

    with open(result_file, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_text)

#12/2

class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'{self.name}, price: {self.price}, description: {self.description}, dimensions: {self.dimensions}'


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'{self.name} {self.surname}, phone: {self.numberphone}'


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def __str__(self):
        result = f'User: {self.user}\nItems:\n'
        for item, cnt in self.products.items():
            result += f'{item.name}: {cnt} pcs.\n'
        return result

    def get_total(self):
        self.total = sum(item.price * cnt for item, cnt in self.products.items())
        return self.total