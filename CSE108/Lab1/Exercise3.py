#gets a word from the user
Specific_word = input("enter the word you are looking for: ").lower()

#opens the file and reads it in lower case
file = open("PythonSummary.txt","r")
lines = file.read().lower()

#counts the number of times the word appears
count = lines.count(Specific_word)
print("the word was found " + str(count) + " times")
file.close()