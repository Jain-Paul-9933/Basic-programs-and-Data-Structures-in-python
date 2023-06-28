written_test = int(input("Enter the written test score  "))
lab_exam = int(input("Enter the lab exam score  "))
assignments = int(input("Enter the assignments score  "))
grade = (written_test*70)/100+(lab_exam*20)/100+(assignments*10)/100
print(f"Aruns overall grade = {grade}")
