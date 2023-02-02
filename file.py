# fp = open('myfile.txt', 'w')
# fp = open('myfile.txt', 'r')
fp = open('myfile.txt', 'a')
# fp.write('This is a test file\n')
lines = ["Apple\n", "Banana\n", "Coconut\n"]
fp.writelines(lines)

# content = fp.read()
# print(content)

fp.close()