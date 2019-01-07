# coding:utf-8

from PIL import Image

class StudentCard():
    CardList = []

    def __init__(self, id, name,text):
        self.id = id
        self.name = name
        self.balance = 0
        self.image = Image.open("./default.png")
        self.text = text
        self.last_charged_date = "チャージしていません"
        self.CardList.append(self)

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def get_charged_date(self):
        return self.last_charged_date

    def get_text(self):
        return self.text

    def set_balance(self, balance):
        self.balance = balance

    def set_name(self, name):
        self.name = name

    def set_charged_date(self, date):
        self.last_charged_date = date

    def set_image(self,image_path):
        self.image = Image.open(image_path)

    def show_image(self):
        self.image.show()