# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# hw_assignment_7_clinton.py
# CIS-135 Python
# Homework Assignment #7 - Data Analytics App for Grades

# Code Summary:
# This program will perform a statistial grade analysis on grades/scores
# entered by a user. After a welcome message and app description, the
# user is prompted to declare how many scores will be analyzed.
# The program then takes the information in from the user, and
# when the input is complete, the app determines the highest, lowest
# and average scores, and computes the number of score in ranges
# from 90-100, 80-89, 70-79, 60-69 and below sixty. The output
# from the program includes a table and information on the high,
# low and average score.

# Change-Log:
# 1) The algorithm updates the proper score ranges from the
# original reqruiement so they do not overlap for example B was given
# as 80-90 but should be 80-89
# 2) input_fuction added as seen in flowchart. This function does not appear
# in the pseudocode or the original requirements
# 3) data_analysis function returns range_data not range_list as shown in flowchart

# Start Data Analysis Function Declaration
def data_analysis(score_count, score_list):
  # Determine and save the High Score (high_score)
  high_score = max(score_list)
  # Determine and save the Low Score (low_score)
  low_score = min(score_list)
  range_data = [0,0,0,0,0]
  average_score = 0.00
  grand_total = 0
  for item in range(len(score_list)):
    # Use another Python list to store range_data:
    # For each score determine range and save in [range_data] list
    if score_list[item] >= 90:
      # [index 0] 90 +   if each_score
      range_data[0] = range_data[0] + 1
    elif (score_list[item] >= 80) and (score_list[item] < 90):
      # [index 1] 80-89  if each_score
      range_data[1] = range_data[1] + 1
    elif (score_list[item] >= 70) and (score_list[item] < 80):
      # [index 2] 70-79  if each_score
      range_data[2] = range_data[2] + 1
    elif (score_list[item] >= 60) and (score_list[item] < 70):
      # [index 3] 60-69  if each_score
      range_data[3] = range_data[3] + 1
    else:
      # [index 4] 59 and below
      range_data[4] = range_data[4] + 1
    # update Grand Total for eventual Average Calculation
    grand_total += score_list[item]
  # Determine and save the Average Score (average_score)
  if score_count == 0:
    average_score = 0.00
  else:
    average_score = grand_total / score_count
  return range_data, high_score, low_score, average_score

# Display Results Function Declaration
def print_results(range_data, high_score, low_score, average_score):
  # Print a Table using range_data:
  print_statement_header = "\t\t{:>5}{:>25}{:>15}"
  print_statement_data = "\t\t{:>5}{:>25}{:>15d}"
  print("\n\t\tScore Report")
  print(print_statement_header.format("Grade","Range of Quiz Scores", "Scores Found"))
  print(print_statement_data.format("A","90 and Above",int(range_data[0])))
  print(print_statement_data.format("B","80 - 89",int(range_data[1])))
  print(print_statement_data.format("C","70 - 79",int(range_data[2])))
  print(print_statement_data.format("D","60 - 79",int(range_data[3])))
  print(print_statement_data.format("F","59 and below",int(range_data[4])))
  print("\n\t\tThe highest score found was", high_score)
  print("\t\tThe lowest score found was", low_score)
  print("\t\tThe average score was", average_score)
  return

def input_function(score_count):
  score_list = []
  # Loop on the total value of score_count:
  for item in range(score_count):
    # Prompt the user to enter the next score
    # For each score entered save to score_list
    score_list.append(int(input("\t\tPlease enter the score: ")))
  return score_list

# Start Main Function Declaration
def main():
  #   Welcome the User
  print("\nWelcome to the Quiz Score Application\n")
  # Explain the Application
  print("\tThis app will take quiz scores and compute the")
  print("\thigh, low and average score, and also print a table")
  print("\twith the scores found in ranges, 90+, 80-89, 70-79, 60-69")
  print("\tand below 60.")
  # Prompt user for total score to enter = score_count
  score_count = int(input("\n\tPlease enter the total number of scores to report: "))
  score_list = input_function(score_count)
  print("\t\tThank you for the data")
  # print(score_list)
  # Run Data Analysis Function
  # catch (range_data, high_score, low_score, average_score)
  # send in (score_list, score_count)
  range_data, high_score, low_score, average_score = data_analysis(score_count, score_list)
  # print(range_data)
  # print(high_score)
  # print(low_score)
  # print(average_score)
  # Run Display Results Function
  # send in (range_data, high_score, low_score, average_score)
  print_results(range_data, high_score, low_score, average_score)
  # Thank the user and print a final exit message.
  print("\nThank you for using Quiz Score Application")
  return

# Run Main
main()

