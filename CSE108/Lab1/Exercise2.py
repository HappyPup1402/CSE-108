#gets the sentence and the number of times to repeat it
sentence = input("Enter a sentence: ")
num_times = int(input("Enter a number: "))

#opens the file and writes the sentence to it
with open("CompletedPunishment.txt", "w") as f:
    for i in range(num_times):
        f.write(sentence + "\n")

print("Sentence was written to the file 'CompletedPunishment.txt'")

