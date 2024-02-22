import json

def writeToFile(dataDict, fileName):
    with open(fileName, 'w') as textFile:
        json.dump(dataDict, textFile)

with open('grades.txt') as file:
    data = file.read()

dict = json.loads(data)

running = "run"

while(running != "stop"):
    decision = input("would you like to add a new student? (Y/N): ")
    if(decision == "Y"):
        name = input("Please enter the first and last name of the student: ")
        grade = input("Please enter their grade: ")
        dict[name] = grade
        writeToFile(dict, "grades.txt")
        
    
    decision = input("would like to view, edit, or delete a students grade? (view/edit/delete): ")
    if(decision == "view"):
        name = input("Please enter the first and last name of the student: ")
        print(dict[name])
    elif(decision == "edit"):
        name = input("Please enter the first and last name of the student: ")
        grade = input("Please enter their new grade: ")
        dict[name] = grade
        writeToFile(dict, "grades.txt")
    elif(decision == "delete"):
        name = input("Please enter the first and last name of the student: ")
        dict.pop(name)
        writeToFile(dict, "grades.txt")
    
    running = input("Would you like to continue? (run/stop): ")
    
print("printing the updated dictionary: ")
print(dict)
file.close()