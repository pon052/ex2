# coding:utf-8
import gensim

from StudentCard import StudentCard
from datetime import datetime

class MainShopCharger:

    model = gensim.models.Word2Vec.load("./word2vec.gensim.model")

    def __init__(self):
        self.inserted_student_card = None
        self.last_charged_date = "チャージしていません"

    def insert_card(self,num):
        self.inserted_student_card = StudentCard.CardList[num]

    def charge_money(self,money):
        if(self.inserted_student_card is not None):
            self.inserted_student_card.set_balance(self.inserted_student_card.get_balance() + money)
            self.last_charged_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            self.inserted_student_card.set_charged_date(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            self.print_usage_information()
        else:
            print("学生証が挿入されていません．")

    def print_account_balance(self):
        print("--カード利用情報--")
        print("学生名：" + self.inserted_student_card.get_name())
        print("残高：" + str(self.inserted_student_card.get_balance()))
        print("最終利用日：" + self.inserted_student_card.get_charged_date())

    def print_charger_information(self):
        print("--チャージャ利用情報--")
        print("最終利用日：" + self.last_charged_date)

    def print_usage_information(self):
        print("-----利用情報-----")
        self.print_charger_information()
        print("")
        self.print_account_balance()
        print("------------------")

    def most_similar(self):
        if(self.inserted_student_card is not None):
            text = self.inserted_student_card.get_text()
            tokens = text.split("/")
            vectors = []
            for token in tokens:
                vectors.append(token)
            print("関連ワード :")
            results = MainShopCharger.model.most_similar(positive = vectors,negative = [],topn=5)
            for result in results:
                print(str(result[0]) + " : " + str(result[1]))
        else:
            print("学生証が挿入されていません．")

    def main(self):
        # Main Sentences
        # 学生証インスタンスの作成
        student_card_1 = StudentCard(0, "tut","とんかつ/からあげ/エビフライ")
        student_card_2 = StudentCard(1, "tempaku","内田真礼/水瀬いのり/佐倉綾音/佐藤聡美/種田梨沙")

        # 初期残高の設定
        student_card_1.set_balance(1000)

        #エラー処理の表示
        self.charge_money(200)

        # 学生証１枚目のカードをセット
        self.insert_card(0)

        self.most_similar()
        # 加算
        self.charge_money(1000)

        # 減算
        #self.charge_money(-300)

        # 学生証の２枚目の挿入とチャージ
        self.insert_card(1)

        # 加算
        self.charge_money(500)

        # 引き出し
        #self.charge_money(-100)

        self.most_similar()

if __name__ == '__main__':
    Charger = MainShopCharger()
    Charger.main()