##

from random import shuffle


class Card:
    """khai báo tên các quân bài"""

    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None, 
            "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                "Jack", "Queen", "King", "Ace"]




    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False


    def __gt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else: 
                return False
        return False
        """ ở đay xin giải thích rõ thêm: để so sánh được card1 với card2 tức dùng 2 phương thức __lt__ và __gt__
            (2 cái được gọi là magic method), để lấy giá trị truyền vào card1 và card2 tức suit và value để so sánh
            theo nguyen tắc thì ss value trước nếu value bằng nhau thì so sánh đến suit. suit và value lúc này đóng 
            vai trò như thứ tự của card trong mảng suits và values ở trên.
            các giá trị của mảng Suits và Values lúc này là chưa liên quan. các mảng này cố định và các phần tử trong mảng 
            cũng được sắp xếp theo thứ tự nhỏ đến bé sao cho tương ứng với biến 
        """
    def __repr__(self):
        v = self.values[self.value] + " of "\
            + self.suits[self.suit]

        return v
        """
        lúc này thì người ta mới bắt đầu động đến 2 mảng suits và values ở trên, tức lấy các index [suit]&[value]
        đã được truyền để gọi tên quân bài ra"""


class Deck:
    """ dùng hàm random để cho máy chọn bài ngẫu nhiên class 
    này không cần truyền biến số mà nó chạy bằng nội tại
    """
    
    def __init__(self):

        self.cards = []

        for i in range(2, 15):
            for j in range(4): # dùng 2 vòng lặp i, j là tạo được một mảng các quân bài 
                self.cards.append(Card(i,j)) # ví dụ sẽ có mảng cards = [2-0, 2-2, 2-3, 3-0, 3-1, ...]  
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

# deck = Deck()
# for card in deck.rm_card:
#     print(card)

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("player 1 name: ")
        name2 = input("player 2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)


    def wins(self, winner):
        w = "the winner is {}"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} was took {}, {} was took {} "
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("start the war!")
        while len(cards) >= 2:
            m = "q to quit game?"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("the winner is {}, game over ".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name

        return "引き分け❣"

game = Game()
game.play_game()