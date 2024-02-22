#ask the user for an input of numbers
users_input = input('Enter elements of a list separated by space \n')

#Turns the input into a list
nums_list = users_input.split()

#variable that holds the sum of the list
sum = 0

#Check if the sum should be printed or not
valid = 0

#first i check is the list is less than 2 numbers
#if not, I loop through the list adding all the numbers together and only breaking the loop if i encounter a string
if len(nums_list) < 2:
    print("ERROR: The list is less than two numbers")
    valid = 1
else:
    for i in range(len(nums_list)):
        try:
            if isinstance(float(nums_list[i]), float) == True:
                sum += float(nums_list[i])
        except:
            print("ERROR: The list contains a string")
            valid = 1
            break

if valid == 0:
    print(sum)