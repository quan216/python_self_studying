#bat dau code voi filegit
import csv
with open("testfile.csv", "r") as f:
    print(f.read())

ten = input("ten ban la cai lon gi: ")
age = input("tuoi la bao nhieu: ")
answer = f'{ten}, {age}\n'


with open("testfile.csv", "w", encoding="UTF-8", newline="") as f:
    f.write(answer)


