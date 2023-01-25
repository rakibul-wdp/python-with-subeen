# key -> value
# 1 -> One, 2 -> Two

# num_to_words = dict()

# num_to_words[1] = "One"
# num_to_words[2] = "Two"
# num_to_words[3] = "Three"

num_to_words = {1: 'One', 2: 'Two', 3: 'Three'}
num_to_words[4] = 'Four'

# print(num_to_words)
# print(type(num_to_words))

# print(num_to_words[5])

# if "Four" in num_to_words:
#   print('Available')
# else:
#   print('Not Found')

# del num_to_words[3]
# print(num_to_words)

# for key, value in num_to_words.items():
#   print(key, value)

# print(dir(num_to_words))

# print(num_to_words.items())

fruits = {'A': 'Apple', 'B': 'Banana', 'C': 'Coconut'}

# print(fruits.values())
# fruits.clear()
# print(fruits)

# print(fruits['D'])
print(fruits.get('D'))
