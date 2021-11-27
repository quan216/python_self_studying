import math

class Circle:
    def __init__(self, r):
        self.radius = r
        print(math.pi)

    def area(self):
       return self.radius ** 2 * math.pi



class Triangle:
    def __init__(self, d1, d2, d3):
        self.dimension1 = d1
        self.dimension2 = d2
        self.dimension3 = d3
        self.S = (self.dimension1 + self.dimension2\
                    + self.dimension3)/2

    def area_cal(self):
        return math.sqrt(self.S*(self.S- self.dimension1)*\
            (self.S - self.dimension2)*(self.S - self.dimension3))





print(" 3 canh cua tam giac (a, b, c): ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if abs(b-c) < a and a < a+b :
    t_triangle = Triangle(a, b, c)
    print("area of trigangle is ")
    print(t_triangle.area_cal())
else: 
    print("these dimensions are not become a triangle ")
