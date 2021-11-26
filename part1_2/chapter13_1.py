##
import math

class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectange(Shape):
    def __init__(self, d1, d2):
        self.dimension1 = d1
        self.dimension2 = d2
    def cal_Perimeter (self):
        return 2*(self.dimension1 + self.dimension2)



class Square(Rectange):
    def cal_are(self):
        return self.dimension1 * self.dimension2
    def change_size(self, d1, d2):
        self.dimension1 = d1
        self.dimension2 = d2








rect_a = Rectange(20,15)
rect_a.what_am_i()

print(rect_a.cal_Perimeter())
rect_b = Square(50, 49)
print(rect_b.cal_Perimeter())

print(rect_b.cal_are())

rect_b.change_size(100, 50)
print(rect_b.cal_Perimeter())
print(rect_b.cal_are())




