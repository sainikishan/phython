list = [1,2,3,4,5,6]
for val in list:
    print(val)
veggies=["a","b","c","d","f"]
for val in veggies:
 print(val)

 str ="kisham siani"
 for char in str:
    print(char)

# for loop with else
 str ="kishansaini"
 for char in str:
    if char == "a":
       print("a found")
       break
    print(char)
    
else:
    print("ended")

    # range
    print(range(5))
    for i in range(5):
       print(i)
    #    range start and stop
    for i in range(1,9):
       print(i)
for i in range(1,4,9):
       print(i)
      #  Practice Question
# find n number using while naytral
n = 10
sum=0
for i in range(n+1):
 
   sum += i
   print("total sum is =",sum)
   # factiroal n natural number
   n = 10
   sum = 1
   for i in range(1,n+1):
      sum *= i
      print("factorial of",n,"is =",sum)
      