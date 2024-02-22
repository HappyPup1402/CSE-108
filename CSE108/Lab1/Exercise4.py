#This class assigns the values of the input file to the object
class Course:
    def __init__(self, title, num, name, credits, days, start, end, percentage):
        self.title = title
        self.num = num
        self.name = name
        self.credits = credits
        self.days = days 
        self.start = start
        self.end = end 
        self.percentage = percentage

file = open("classesInput.txt","r")
input = int(file.readline())

#a list that holds all the objects(courses)
schedule = []

#loops through the file and creates a course object and adds it to the list
for x in range(input):
    title = file.readline().strip()
    num = file.readline().strip()
    name = file.readline().strip()
    credits = file.readline().strip()
    days = file.readline().strip()
    start = file.readline().strip()
    end = file.readline().strip()
    percentage = file.readline().strip()
    course_obj = Course(title, num, name, credits, days, start, end, percentage)
    schedule.append(course_obj)

#loop through the list and print the values of the object in schedule format
for i in range(input):
    print("COURSE " + str(i + 1) + ": " + (schedule[i].title) + (schedule[i].num) + ": " + (schedule[i].name))
    print("Number of Credits: " + schedule[i].credits)
    print("Days of Lecture: " + schedule[i].days)
    print("Lecture Time: " + schedule[i].start + " - " + schedule[i].end)
    print("Stat: on average, students get " + schedule[i].percentage + "% in this course \n")
file.close()