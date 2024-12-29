# Code Demo for 09 Lecture
# Working with Data (Arrays as Lists) in Python
# CIS 135 - Code Demo File

# # Example of an array in Python called a list.
# print("\nmy_list Example")
# my_list = [1,2,3]
# print(len(my_list))

# # Example of an array in Python called a list.
# print("\nnum_list Example")
# num_list = [1,2,3,4,5]
# print(len(num_list))

# # Example from Lecture:
# print("\nTest Array List Example")
# testArray = [16, 22, 6, 8, 2, 12, 14, 56]
# print("The value of testArray[4] is: ", testArray[4])
# print("The value of testArray[2] + 1 is: ", testArray[2] + 1)
# print("The value of testArray[0] * 2 is: ", testArray[0] * 2)

# # Lecture 8 Final Example of updating scores in a Python List
# sum = 0
# numScores = int(input("How many scores? "))
# theScores = []
# for scoreCount in range(0, numScores):
#   score = int(input("What is the score? "))
#   sum = sum + score
#   theScores.append(score)
# average = sum / numScores
# print(average)

# # Lecture 8 Final Example of updating scores in a Python List
# sum = 0
# numScores = int(input("How many scores? "))
# theScores = []
# for scoreCount in range(0, numScores):
#   score = int(input("What is the score? "))
#   sum = sum + score
#   theScores.append(score)
# average = sum / numScores
# print(average)

# # Example of a Python list nested within a list
# players_records = [ ["Jones", 25 ], ["Raji", 27], ["Bethany", 31] ]
# print(players_records)
# print(type(players_records))
# print(players_records[0])
# print(players_records[1][1])

# # Example of Python dictionary which stores key: value pairs
# players_dict = {"Jones": 25, "Raji":27, "Bethany":31 }
# print(players_dict)

# # Lecture Example of Parallel Lists in Python
# sum = 0
# numScores = 0
# numScores = int(input("How many scores? "))
# names = []
# scores = []
# for scoreCount in range(0, numScores):
#   names.append(input("Please enter the player name: "))
#   theScore = int(input("Please enter the player score: "))
#   scores.append(theScore)
#   sum += theScore
# average = sum / numScores
# print("The average score is:", average)
# print(scores)
# print(names)
# # Finding the high score (by looping over the data)

# Finding the high score by using max() function in Python
# player_name = ['Squarepants', 'Starr', 'Krabb', 'Tentacles', 'Snail' ]
# player_score = [88, 56, 35, 99, 22]
# print(max(player_score))

# Finding the high score by using max() function in Python
# player_name = ['Squarepants', 'Starr', 'Krabb', 'Tentacles', 'Snail' ]
# player_score = [88, 56, 35, 99, 22]
# high_score, score_index, this_score = 0,0,0
# for each in player_score:
#   if each >= high_score:
#     high_score = each
#     score_index = player_score.index(each)
# print("Player ", player_name[score_index], "has the high score of", player_score[score_index])


# Finding the high score by using max() function in Python
# player_name = ['Squarepants', 'Starr', 'Krabb', 'Tentacles', 'Snail' ]
# player_score = [88, 56, 35, 99, 22]
# max_score = max(player_score)
# max_index = player_score.index(max_score)
# print("Player ", player_name[max_index], "has the high score of", player_score[max_index])

# Parts Example Search list for string
# parts = ["hammer", "nails", "wrench", "ladder"]
# searchTerm = input("Part to search for: ")
# index = 0
# searchTermIndex = -1
# while searchTermIndex == -1 and index <= 5:
#   if searchTerm == parts[index]:
#     searchTermIndex = index
#     print("Found ", searchTerm, "at index #", index )
#   else:
#     index = index + 1

