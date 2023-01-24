def generate_multiplication_table(n):
  print(n, "X 1 =", n * 1)
  print(n, "X 1 =", n * 2)

n = input("Enter number: ")
n= int(n)
value = generate_multiplication_table(n)
print(value)