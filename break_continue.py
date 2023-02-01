# while True:
#   s = input()
#   if s == "q":
#     break
#   print(s.upper())

while True:
  s = input()
  print(s.upper())
  s = input("Do you want to continue? (y/n)")
  if s == "y":
    continue
  print("bye bye")
  break