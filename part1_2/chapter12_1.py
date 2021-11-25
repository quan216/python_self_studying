class Apple:
    def __init__(self, w, c, t, p):
        self.weight = w
        self.color = c
        self.type = t
        self.price = p
        print("compare apple!")


fuji_apple = Apple(100, "red", "fuji", "$100")
us_apple = Apple(100, "light red", "usa", "$97")

A = fuji_apple.type + " apple; color: " + fuji_apple.color + "; " + fuji_apple.price
B = us_apple.type + " apple; color: "+ us_apple.color + "; " + us_apple.price

if input("what do you want to buy? (A or B): \n") == "A":
    print(A)
else: print(B)



