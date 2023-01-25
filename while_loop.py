# i = 1

# while i <= 10:
#   print(i)
#   i += 1

def multiplication_table(n):
  for i in range(1, 11):
    print("{} X {} = {}".format(n, i, n *i))

n = input("Enter a number (0 to exit): ")

while n != 0:
  multiplication_table(int(n))
  print("")
  n = int(input("Enter a number (0 to exit): "))