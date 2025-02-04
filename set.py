
#set is unorder values ignore duplicate value
collection={1,2,3,3,4,5,6}
print(collection)
print(type(collection))
print(len(collection))
# create a empty set
# set method
# add() method set ke adar sab hash value adte haii
collection=set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(6)
collection.add(6)
# collection.remove(6)
# print(collection.pop())
collection1={1,2,3,3,4,5,6}
collection2={1,2,3,3,4,5,6}
print(collection.union(collection2)) 
# intersection

print(collection.intersection(collection2))
