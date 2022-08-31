print(4 == 4) # is 4 equal to 4? True
print(4 == 3) # is 4 equal to 3? False
print(4 != 4) # is 4 not equal to 4 ? False
print(6 != 4) # is 4 not equal to 4 ? True
print(10 > 7) # is 10 greater than 7? True
print(10 < 7) # is 10 less than 7? False
print(20 >= 12) # is 10 greater than or equal to 7? True
print(10 <= 7) # is 10 less than or equal to 7? False

# Application of logical operator
institute_language = "Python"
student_language = "PHP"
print(student_language==institute_language) # False
student_language2 = input("What language do you want to learn? ")
print("I got Admission : ",student_language2==institute_language)