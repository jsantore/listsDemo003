# open the faculty.txt file for reading
faculty_file = open("faculty.txt", 'r')
# read all lines from faculty.txt into a list of strings called all_faculty
all_faculty = faculty_file.readlines()
# do lines 7-12 once for each line in the file
for faculty_line in all_faculty:
    # remove the \n from the end of the current line
    faculty_line = faculty_line.strip()
    # break the current line into a list with ['name', 'years'] on the '-' character
    name_and_years = faculty_line.split("-")
    # print out a statement using the line that was split in two
    print(f"Prof. {name_and_years[0]} has been at BSU for {name_and_years[1]} years")