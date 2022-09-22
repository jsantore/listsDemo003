courses_file = open("requiredCS.txt", 'r')
lines_from_file = courses_file.readlines()
for line in lines_from_file:
    print(line)