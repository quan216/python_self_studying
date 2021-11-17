#bat dau code voi filegit
import csv
from os import name
with open("testfile.csv", "r") as f:
    print(f.read())
data_total = []


for i in range(0,2):

    name = input("ten ban la cai lon gi: ")
    age = input("tuoi la bao nhieu: ")
    data_total = f"{name}, {age}, \n"
    print(data_total)

    with open("testfile.csv", "a", encoding="UTF-8", newline="") as f:
        # w = csv.writer(f, delimiter = ",")
        # w.writerow(data_total)
        f.write(data_total)
        


