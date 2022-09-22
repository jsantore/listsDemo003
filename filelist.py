courses_file = open("requiredCS.txt", 'r')
lines_from_file = courses_file.readlines()
for line in lines_from_file:
    loud_line = line.upper()
    course_and_title = line.split(" : ")
#    loud_line = loud_line.strip()
    print(course_and_title[0])
    print(course_and_title[1])
print("those are the classes you HAVE to take for the CS Major")