#exercie 2, printout number 25 to 50
a = []

for i in range(25,51):
    #a = a.reverse(i)
    i += 1

print(a)

#Excercie 3

while True:
    input = input("your number, or q to quit game: ")
    if input == "q":
            print("quit game!")
            break
    try:
        input = int(input)
    except ValueError:
        print("please type a number or q to quit.")

        if input in range(25,50):
            print("you win! congrast!")
        else:
            print("again")

