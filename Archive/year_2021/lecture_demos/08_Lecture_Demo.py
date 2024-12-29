# Code Demo for 08 Lecture
# Working with Data (Arrays as Lists) in Python
# CIS 135 - Code Demo File

# # Lecture Demo shows for loop iterating over score input app
# print("\nScore Count Example")
# print("\nAt end, (after loop) scoreCount, sumScores and numScores are printed")
# sumScores, numScores = 0, 5
# for scoreCount in range(0,numScores):
#   sumScores += int(input("\t Next Score: "))
# print("ScoreCount = ", scoreCount)
# print("sumScore = ", sumScores)
# print("numScores = ", numScores)

# # Lecture Demo shows for loop iterating over score input app
# print("\nScore Count Example; illustrates (numScores - 1)")
# print("\nAt end, (after loop) scoreCount, sumScores and numScores are printed")
# sumScores, numScores = 0, 5
# for scoreCount in range(0,numScores-1):
#   sumScores += int(input("\t Next Score: "))
# print("ScoreCount = ", scoreCount)
# print("sumScore = ", sumScores)
# print("numScores = ", numScores)

# # Lecture Demo shows computing an average after loop iterating over score input app
# print("\nScore Count Example; illustrates (numScores - 1)")
# print("\nAt end, (after loop) scoreCount, sumScores and numScores are printed")
# sumScores, numScores = 0, 5
# for scoreCount in range(0,numScores-1):
#   sumScores += int(input("\t Next Score: "))
# print("ScoreCount = ", scoreCount)
# print("sumScore = ", sumScores)
# print("numScores = ", numScores)
# print("Average of all Scores = ", sumScores/numScores)

# # Example of numeric data list; shown in lecture
# scores = []

# # Example of string data list; shown in lecture
# names = []
# # What actually happens? the old names is destroyed, and a new names list is created
# names = ['python', 'is', 'easy', 'to', 'learn']

# # example showing five separate variables storing integer values
# num1, num2, num3, num4, num5 = 1, 2, 3, 4, 5

# # Example of an array in Python called a list.
# print("\nmy_list Example")
# my_list = [1,2,3,4,5]
# print(len(my_list))
# print(type(my_list))

# # Example of an array in Python called a list.
# print("\nnum_list Example")
# num_list = [1,2,3,4,5]
# print(len(num_list))
# print(num_list)


# # example showing five separate variables storing integer values
# print("\nScore List Example")
# score_list = [11,22,33,44,55]
# print("List score_list[0] value or zeroth position = ", score_list[0])
# print("List score_list[1] value or first position = ", score_list[1])
# print("List score_list[2] value or second position = ", score_list[2])
# print("List score_list[3] value or third position = ", score_list[3])
# print("List score_list[4] value or fourth position = ", score_list[4])

# # Example from Lecture:
# print("\nTest Array List Example")
# testArray = [16, 22, 6, 8, 2, 12, 14, 56]
# print("The value of testArray[4] is: ", testArray[4])
# print("The value of testArray[2] + 1 is: ", testArray[2] + 1)
# print("The value of testArray[0] * 2 is: ", testArray[0] * 2)

# # Example from Lecture:
# testArray = [16, 22, 6, 8, 2, 12, 14, 56]
# print("\nTest Array List Example with Index as a Variable")
# idx = 5
# print("The value of testArray[idx] is: ", testArray[idx])
# print("The value of testArray[idx] + 3 is: ", testArray[idx] + 3)
# print("The value of testArray[idx + 1] is: ", testArray[idx + 1])

# # Example from Lecture:
# testArray = [16, 22, 6, 8, 2, 12, 14, 56]
# print("\nMore Test Array Examples")
# print("Value at testArray[0] = ", testArray[0])
# testArray[7] = 30
# print("The Value at testArray[7] = ", testArray[7])
# testArray[1] = int(input("Please type a number: "))
# print("Value at testArray[1] = ", testArray[1])
# print("The entire list of values in testArray:", testArray)

# # Example shows the append syntax for adding new items to the
# End of a Python List
# appendScores = [ ]
# appendScores.append("okay")
# appendScores.append(22)
# appendScores.append("the end")
# print(appendScores)

# # Example of updating scores
sum = 0
numScores = int(input("How many scores? "))
theScores = []
for scoreCount in range(0, numScores):
  score = int(input("What is the score? "))
  sum = sum + score
  theScores.append(score)
average = sum / numScores
print(average)
print(theScores)
print(theScores[0])
print(theScores[1])
print(theScores[2])