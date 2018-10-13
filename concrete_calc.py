#!usr/bin/python3
import math

def get_length():
    while True:
        try:
            length = float (input("Length in feet: "))
        except ValueError:
            print("Input must be numeric")
        else:
            return length

def get_width():
    while True:
        try:
            width = float (input("Width in feet: "))
        except ValueError:
            print("Input must be numeric")
        else:
            return width

def get_depth():
    while True:
        try:
            depth = float (input("Depth in inches: "))
        except ValueError:
            print("Input must be numeric")
        else:
            return depth


length = get_length()
width = get_width()
depth = get_depth()

""" According to https://www.convert-me.com/en/bb/viewtopic.php?t=4226 
an 80 lbs of concrete is 0.6 cubic yards"""
a = 27*0.6
# cubic inches in one bag
EightyLbBag = a * 12
area = (length * width) * 12

print("Area in square inches ", area)


volumeRequired = area * depth
print("Volume required in cubic inches = ", volumeRequired)

numberOfBags = math.ceil(volumeRequired / EightyLbBag)
print("Number of 80lb bags of concrere required = ", numberOfBags)
