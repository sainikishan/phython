# marks=int(input("Enter a marks:"))

# if(marks >= 90):
#    grade="A"
# elif(marks>= 80 and marks < 90):
#    grade="B"
# elif(marks >= 70 and marks < 60):
#    grade="C"
# elif(marks >= 50 and marks < 40):
#     grade="D"
# else:
#    grade="F"

# print("grade of the studen:", grade)



marks = int(input("Enter marks:"))

if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 60 and marks < 80:  # Adjusted range for C
    grade = "C"
elif marks >= 40 and marks < 60:  # Adjusted range for D
    grade = "D"
else:
    grade = "F"

print("Grade of the student:", grade)
