# Recursion
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(5)
   
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))
def cal_sum(n):
    if(n == 0):
        return
    print(n)
# print all elemnet in a ist using recursive
lst = [1, 2, 3, 4, 5]
def print_list(lst):
    if len(lst) == 0:
        return
    print(lst[0])
    print_list(lst[1:])
    print_list(lst)
    