institute_attendance = 80
#student_attendance = 90
# Can student can continue in Million Coders
student_attendance = int(input("How Many Students Are There : "))
if student_attendance==institute_attendance :
            print("Student can continue in Million Coders")
elif student_attendance > institute_attendance :
     print("Student is punctual and good")
elif student_attendance < institute_attendance:
       print("Student can not continue in Million Coders")