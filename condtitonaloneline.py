food= input("food : ")
eat = "yes" if food == "cake" else "no"
print(eat)


food = input("sweet : ")
print("sweet") if food == "cake" or food=="jalebi" else print("not seet")

# clever if ternary operator
age = int(input("age : "))
vote =("yes","no") [age < 18]