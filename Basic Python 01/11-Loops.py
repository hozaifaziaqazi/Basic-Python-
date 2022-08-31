"""x=0
i = int(input("Enter the number:"))
while (x<=i):  # it will run till x's values reaches to 5
 print(x)
 x=x+1


for x in range(5,20): # it will start from 5, and it will end to 20
 print(x)
 x=x+1


days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for d in days:

 if d=="Fri":
     #break # it will run only till "Fri"
 continue # it will skip the "Fri"

 print(d)

for x in range(1, 11, 3):
 print(x)"""

"""number = int(input ("Enter the number of which the user wants to print the multiplication table: "))
# We are using "for loop" to iterate the multiplication 10 times.
print ("The Multiplication Table of: ", number)
for count in range(1, 11):
 print (number, 'x', count, '=', number * count)"""




"""number = int(input ("Enter the number of which the user wants to print the multiplication table: "))
times = int(input("How much time that you want to print the table"))
print ("The Multiplication Table of: ", number)
for count in range(1, times):
 print (number, 'x', count, '=', number * count)"""