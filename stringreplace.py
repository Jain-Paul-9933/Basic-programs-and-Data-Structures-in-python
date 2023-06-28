string1 = "hi , good morning everyone"
list = list(string1)
for i in range(len(list)):
    if list[i] == "o":
        list[i] = "5"
string2 = ''.join(list)
print(string1)
print(string2)
