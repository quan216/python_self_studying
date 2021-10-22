string = ("カミュ")
string = str(string)

for i in string:
    print(i)

# challeges 4

Sample_string = "どこで, だれか, いつ"
a = Sample_string.split(",")
print(a)

#Challeges 5

list = ["the", "fox", "jump", "over", "the", "fence", "."]
result5 = " ".join(list)
print(result5.replace(" .",".").capitalize())


#Challenges 9
list6 = "three three three"

list6_split = list6.split(" ")
plus_list = " + ".join(list6_split)

print(plus_list)

multi_list = plus_list.replace("+", "*")
print(multi_list)

#Challenges10
list10 = "四月の晴れた寒い日ので、時計はどこでも十三時を打っていた"

list10_split = list10.split("、")
print(list10_split)
print("                          ")
print(f'{list10_split[0]}\n{list10_split[1]}')






