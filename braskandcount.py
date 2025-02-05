# break used
# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1
# print("end")


# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# x = 6
# i = 0
# while i < len(nums):
#     if nums[i] == x:
#         print("Found at index", i)
#         break  # Stops the loop when found
#     i += 1  # Move to the next index
# else:
#     print("Not found")  # Runs if the loop completes without finding `x`


# continue
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)

x = 6
i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at index", i)
        continue  # Stops the loop when found
    i += 1  # Move to the next index
else:
    print("Not found")

  