total_mark = float(input("Enter the total percentage  "))
if total_mark >= 90:
    print("A")
elif total_mark >= 80 and total_mark < 90:
    print("B")
elif total_mark >= 70 and total_mark < 80:
    print("C")
elif total_mark >= 60 and total_mark < 70:
    print("D")
elif total_mark >= 50 and total_mark < 60:
    print("E")
else:
    print("Failed")
