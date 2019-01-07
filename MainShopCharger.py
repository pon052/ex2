# coding:utf-8
from StudentCard import StudentCard

class MainShopCharger:
    def __init__(self):
        self.inserted_student_card = None

    def insert_card(self,num):
        self.inserted_student_card = StudentCard.CardList[num]

    def charge_money(self,money):
        if(self.inserted_student_card is not None):
            self.inserted_student_card.set_balance(self.inserted_student_card.get_balance() + money)
            self.print_account_balance()
        else:
            print("学生証が挿入されていません．")

    def print_account_balance(self):
        print("残高を表示します")
        print("学生名：" + self.inserted_student_card.get_name())
        print("残高：" + str(self.inserted_student_card.get_balance()))

    def main(self):
        # Main Sentences
        # 学生証インスタンスの作成
        student_card_1 = StudentCard(0, "tut")
        student_card_2 = StudentCard(1, "tempaku")

        # 初期残高の設定
        student_card_1.set_balance(1000)

        #エラー処理の表示
        self.charge_money(200)

        # 学生証１枚目のカードをセット
        self.insert_card(0)

        # 加算
        self.charge_money(1000)

        # 減算
        self.charge_money(-300)

        # 学生証の２枚目の挿入とチャージ
        self.insert_card(1)

        # 加算
        self.charge_money(500)

        # 引き出し
        self.charge_money(-100)

if __name__ == '__main__':
    Charger = MainShopCharger()
    Charger.main()