# def multiplication_table(n):
#   for i in range(1, 11):
#     print("{} X {} = {}".format(n, i, n * i))

# multiplication_table(3)

import json

data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])