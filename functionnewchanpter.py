# Function is a block of statement that perform a specfic task
# Function can take arguments and return values
# Function can be reused in the program
# write a function
# create a dunction start with def
def sum(a,b):
    s =a + b
    return s
print(sum(2,3))
# average of 3 number an sum also
def average(a,b,c):
    s = a + b + c
    return s/3
print(average(2,3,4))
# function are two type 
# 1. built in function (print,sum)
# 2. user defined function (sum,average)  # function with argument and return valu
# function with argument and return value
def sum(a,b):
    s = a + b
    return s
    
print(sum(2,3))
cit=["a","b","c","f","d"]
# print(cit[0],end="")
def print_len(cit):
    print(len(cit))
heroes=["ksihan","kuar"]
def print_list(heroes):
    for i in heroes:
        print(i)
        print_list(heroes) # function with argument and return value
# fectorial of n
 # function with argument and return value
n=5
fact = 1
for i in range (1,n+1):
    fact = fact * i
    print(fact) # function with argument and return value

    # using function
    n = 6
    def cal(n):
        fact = 1
        for i in range (1,n+1):
            fact = fact * i
            return fact
        print(fact) # function with argument and return v
        # write a function usd to inr
        # function with argument and return value
        def converter(usd_val):
          inr_val = usd_val * 83  # Assuming 1 USD = 83 INR
    print(f"usd_val USD = inr_val INR")

# Taking user input
usd_value = float(input("Enter amount in USD: "))
converter(usd_value)
