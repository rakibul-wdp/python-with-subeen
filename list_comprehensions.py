li = ['apple', 'banana', 'orange', 'mango']
fruits = [fruit.capitalize() for fruit in li]
# print(fruits)

li_len = [len(x) for x in li]
# print(li_len)

cube_list = [x * x * x for x in range(1, 11)]
# print(cube_list)

cube_list = [x for x in range(1, 11) if x % 2 == 1]
# print(cube_list)
cube_list = [x*x*x for x in range(1, 11) if x % 2 == 1]
print(cube_list)