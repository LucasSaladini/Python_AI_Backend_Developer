file = open('lorem.txt', 'r')

# print(file.read())
# print(file.readline())
# print(file.readlines())

while len(line := file.readline()):
    print(line)

file.close()