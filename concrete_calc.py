#!usr/bin/python
import math

""" According to https://www.convert-me.com/en/bb/viewtopic.php?t=4226 
an 80 lbs of concrete is 0.6 cubic yards"""

# define cubic inches in one bag of 80lb cement
# cubic feet in one bag
a = 27*0.6
#cubic inches in one bag
EightyLbBag = a * 12

# get the area in square inches
length = input("Length in feet:  ")
width = input("Width in feet:  ")
area = (length * width) * 12
print "Area in square inches ", area

# get the depth in inches
depth = input("Depth in inches:  ")

volumeRequired = area * depth
print "Volume required in cubic inches = ", volumeRequired

numberOfBags = math.ceil(volumeRequired / EightyLbBag)
print "Number of 80lb bags of concrere required = ", numberOfBags
