# coding:utf-8
class StudentCard():
    CardList = []

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.balance = 0
        self.CardList.append(self)

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def set_balance(self, balance):
        self.balance = balance

    def set_name(self, name):
        self.name = name


