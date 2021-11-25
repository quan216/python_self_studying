import math


class Circle:
    def __init__(self, r):
        self.radius = r
        print(math.pi)

    def area(self):
       return self.radius ** 2 * math.pi

       

A_cir = Circle(14)
print(A_cir.radius)
print(A_cir.area())


