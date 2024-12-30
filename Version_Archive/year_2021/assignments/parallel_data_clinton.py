# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# parallel_data_clinton.py
# CIS-135 Python
# Assignment #18 Handling Parallel Data Collections

# Rubric 1 point:
# Create four parallel data structures named: colors, red_code, green_code, and
# blue_code which together will store a matrix of data.
# colors = "Red", "Yellow", "Lime", "Blue", "Aqua", "Fuchsia", "Silver", "Gray", "Maroon", "Olive", "Green", "Purple", "Teal", "Navy"
# red_code = 255,255,1,1,1,255,192,128,128,128,1,128,1,1
# green_code = 1,255,255,1,255,1,192,128,1,128,128,1,128,1
# blue_code = 1,1,1,255,255,255,192,128,1,1,1,128,128,128
colors = ["Red", "Yellow", "Lime", "Blue", "Aqua", "Fuchsia", "Silver", "Gray", "Maroon", "Olive", "Green", "Purple", "Teal", "Navy"]
red_code = [255,255,1,1,1,255,192,128,128,128,1,128,1,1]
green_code = [1,255,255,1,255,1,192,128,1,128,128,1,128,1]
blue_code = [1,1,1,255,255,255,192,128,1,1,1,128,128,128]

# Rubric 2 Points:
# Once the four data collections are populated, create a Python function
# named allColors which contains a loop that will output (use only a single
# print statement) each color's name, as well as it's correct (corresponding)
# r-g-b data for each item in the collection. (The function should accept each
# of the four data structures as incoming parameters).
# For example: "The rgb color values for Red are red='255', blue='1', green='1'"
def allColors(c,r,g,b):
  count = 0
  for each in c:
    print("The rgb color values for %s are red='%d', green='%d', blue='%d'" %(c[count],r[count],g[count],b[count]))
    count += 1
  return

allColors(colors,red_code,green_code,blue_code)

# Rubric 2 Points: Create another Python function called askColor (which again
# accepts the four data structures as incoming parameters) and prompts the user
# to enter the name of a color to search for. If the color is found in the
# collection, display the color name, as well as it's RGB color codes (as done
# in allColors above).

def askColor(cr,rc,gc,bc):
  getColor = input("What color would you like to look up? ")
  if getColor in cr: # does not know about red it only knows "Red"
    spot_is = cr.index(getColor)
    print("The rgb color values for %s are red='%d', green='%d', blue='%d'" %(cr[spot_is],rc[spot_is],gc[spot_is],bc[spot_is]))
  return

askColor(colors,red_code,green_code,blue_code)

# Extra Point: Create a function called askColors which can handle mixed capitalization
# (lower and upper case letters) and to respond with 'color not found' message if
# the user enters a color which is not in the collection like the color "Busse".
# Allow the user unlimited search attempts, or to exit the loop by entering 'q'.
def askColors(cr,rc,gc,bc):
  go = ''
  while go != 'q':
    getColor = input("What color would you like to look up? ")
    if getColor.capitalize() in cr: #red > Red, bLUE > Blue, OraNGE > Orange
      spot_is = cr.index(getColor.capitalize())
      print("The rgb color values for %s are red='%d', blue='%d', green='%d'" %(cr[spot_is],rc[spot_is],gc[spot_is],bc[spot_is]))
    else:
      print("Sorry, %s was not found in the collection." %(getColor.capitalize()))
    go = input("Press 'y' to search for another color or type 'q' to exit.")
  return

askColors(colors,red_code,green_code,blue_code)
