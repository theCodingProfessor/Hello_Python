# Code Demo for 10 Lecture
# Working with Multi-Dimensional Data (Arrays as Lists) in Python
# CIS 135 - Code Demo File

# Example array shown in lecture 10
print("\nPrinting simple single-dimensional number list: ")
numbers = [45,16,12,5,23]
print(numbers)

# Example array shown in lecture 10
print("\nPrinting simple single-dimensional sales_amounts list: ")
sales_amounts = [30123,25589,10550,15000,18556]
print(sales_amounts)

# Five separate lists with Car Data
ford = ["Ford",0,15000,15125]
honda = ["Honda",8500,8500,8589]
jeep = ["Jeep",5250,5300,0]
toyota = ["Toyota",5000,5000,5000]
chevy = ["Chevy",6185,6185,6185]
print("\nPrinting each list declared as a separate array: ")
print(ford)
print(honda)
print(jeep)
print(toyota)
print(chevy)

# Multi-Dimensional Array (five lists, nested into a single list
cars = [ ["Ford",0,15000,15125], ["Honda",8500,8500,8589], ["Jeep",5250,5300,0], ["Toyota",5000,5000,5000], ["Chevy",6185,6185,6185] ]
print("\nPrinting multi-dimensional list declared as five arrays in a single list: ")
print(cars)

# Three row, five column Multi-Dimensional Array of numbers
numberArray = [ [91,92,93,94,95], [16,15,14,13,12], [77,66,55,44,33] ]
print("\nNumbers array is:", numberArray)

# Verify data can be found using two-dimensional array index:
print("\nIndividual item Lookup in numbers_array is:", numberArray)
print("numberArray[0][0] is", numberArray[0][0])
print("numberArray[1][4] is", numberArray[1][4])
print("numberArray[2][1] is", numberArray[2][1])

# Lecture example for lookup table
# Populate the Arrays and ask the uesr for data
print("\nNested Loop to Receive Car Sales Data")
# cars_original = [ ["Ford",0,15000,15125], ["Honda",8500,8500,8589], ["Jeep",5250,5300,0], ["Toyota",5000,5000,5000], ["Chevy",6185,6185,6185] ]
cars = ["Ford", "Honda", "Jeep", "Toyota", "Chevy"]
months = ["January", "February", "March"]
sales_data = []
for each in range (0, len(cars)):
    sales_data.append([0,0,0])
    for month in range(0,len(months)):
      sales_data[each][month] = int(input(f'Please enter the amount for {cars[each]} in {months[month]}: '))
    print()
print(sales_data)

# Lecture example for sales data
# Calculate the total for each car
car_sub_total= 0
for car in range (0, len(cars)):
  car_sub_total = 0
  for month in range(0,len(months)):
    car_sub_total += sales_data[car][month]
  sales_data[car].append(car_sub_total)
print()
print("Sales data by car for each month, including totals: ", sales_data)

# Calculate the total for each each month
monthly_totals = ["Totals",0,0,0,0]
monthly_sub_total = 0
#end_value = len(months)
for month in range (0, (len(months)+1)):
  monthly_sub_total = 0
  for each_car in range(0,5):
    monthly_sub_total += sales_data[each_car][month]
  monthly_totals[month+1] = monthly_sub_total
print()
print("Monthly totals: ", monthly_totals)

# Lecture Exercise, Printing out the final (with totals in a nicely formatted fashion
print("\nMonthly Car Sales Data")
dstyle = "{data:10,d}"
sstyle = "{data:>12}"
print(f'\t\t\t{sstyle.format(data=months[0])}{sstyle.format(data=months[1])}{sstyle.format(data=months[2])}\t\tMonthly Totals')
for each in range(0,5):
  print(f'\t{cars[each]}\t{dstyle.format(data=sales_data[each][0])}\t{dstyle.format(data=sales_data[each][1])}\t\t{dstyle.format(data=sales_data[each][2])}\t\t\t{dstyle.format(data=sales_data[each][3])}')
print(f'\t{monthly_totals[0]}\t{dstyle.format(data=monthly_totals[1])}\t{dstyle.format(data=monthly_totals[2])}\t\t{dstyle.format(data=monthly_totals[3])}\t\t\t{dstyle.format(data=monthly_totals[4])}')
