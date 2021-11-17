#exercie 2, printout number 25 to 50
a = []

for i in range(25,51):
    #a = a.reverse(i)
    i += 1

print(a)

#Excercie 3

while True:
    
    bet_1 = input("your number, or q to quit game: ")

    if bet_1 == "q":
            print("quit game!")
            break
    try:
        bet_1 = int(bet_1)
    except ValueError:
        print("your input must be number or q to quit game")
        continue

    if bet_1 in range (25,50):
            print("you win! congrast!")
            break
    else:
            print("you lose! sorry!")
    

