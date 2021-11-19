# summary knowledge
# viet game hangerman

import random
import string
import time

random_word = random.sample(string.ascii_lowercase, 3)
machine_word = "".join(random_word)


def hangerman(word):            # word la bien cua ham, sau nay khi goi 
                                #ham chi can thay word vo la giong nhu cau do ma player1 dua ra
    wrong = 0                   # dem so lan wrong

        # ve hinh hangerman
    picture = [" "
                    " _______________",
                    " |          |   ",
                    " |          O   ",
                    " |         /|\  ",
                    " |          |   ",
                    " |         / \  ",
                    " |        /   \ ",
                    " |              ",
                    " |              ",
                    "_|__            ",
                    ]

        #tao mot cai board de hien thi so chu dang duoc dau
    board = ["_"]*len(word)
    win = False              # xac dinh xem thang hay thua, tai thoi diem hien tai chua doan nen mac dinh la thua
        
    rletter = list(word)     # dung ham list de chuyen doi chuoi ki tu thanh list()
    hangerman = "\n".join(picture)




    while wrong < len(picture):

        mesage = ("your word?: \n")
        char = input(mesage)

        if char in rletter:
            cbin = rletter.index(char)
            board[cbin] = char      # thay the ki tu "_" bang "char" tai vi tri trung vs word
            rletter[cbin] = "$"  
            print(board)         # doi ki tu tai vi tri (char) cuar rletter thanh "$" de vong lap sau khong lap lai      
            
        else:
            wrong += 1
            time =  len(picture)-wrong
            mesage2 = f"you still have {time} tiems be carefull!"
            print(mesage2)

        if "_" not in board:
            print("Congrast, you win! \n with answer of:")
            print("".join(board))
            win = True
            break

    if not win:
        print(hangerman)
        print("Sorry, you lose! \n")
        print("answer is: \n ")
        print(word)
        


hangerman(machine_word)





        
        










    
