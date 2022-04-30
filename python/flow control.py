# x=int(input("2+2="))
# if x==4:
#     print("...It's a corect answer")
# else:
#     print("...try agan")

grade = int(input('Enter your grade:'))
if grade >= 90 and grade <=100:
    print('A')
elif grade >= 80 and grade <90:
    print('B')
elif grade >= 70 and grade <80:
    print('C')
elif grade >= 60 and grade <70:
    print('D')
elif grade >100:
    print("Undefined grade")
else:
    print('F')
