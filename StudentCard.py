# coding:utf-8

from PIL import Image

class StudentCard():
    CardList = []

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.balance = 0
        self.image = Image.open("./default.png")
        self.last_charged_date = "チャージしていません"
        self.CardList.append(self)

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def get_charged_date(self):
        return self.last_charged_date

    def set_balance(self, balance):
        self.balance = balance

    def set_name(self, name):
        self.name = name

    def set_charged_date(self, date):
        self.last_charged_date = date

