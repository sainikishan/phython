tuple=(2,1,3,4,5,6,7,8)
print(type(tuple))
print(tuple[2])
print(tuple)
tuple.count(1)
# three fav movie store in list
movies=[]
mov1=input("enter a first movie:")
movies.append(mov1)
mov1=input("enter a second movie:")
movies.append(mov1)
mov1=input("enter a third movie:")
movies.append(mov1)
print(movies)
# plaidrome of elements or not
list1=[1,2,1]

copy_list1=list1.copy()
# list.copy
copy_list1.reverse()
if(copy_list1 == list1):
    print("it is a plaidrome")
else:
    print("it is not a plaidrome")
# print(list)
tuple=("a","a","c","d","a")
print(tuple.count("a"))
tuple=["a","a","c","d","a"]
tuple.sort()
print(tuple)