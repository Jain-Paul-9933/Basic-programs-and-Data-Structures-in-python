count = 0
string = input("Enter the string  ")
j = len(string)
for i in range((len(string)//2)):
    j -= 1
    if string[i] != string[j]:
        count += 1
if count == 0:
    print("String is palindrome")
else:
    print("String is not palindrome")
