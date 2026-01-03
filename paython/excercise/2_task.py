#write a program to calculate and display area of rectangle using given length and width 
#variable create 
length = 0
width = 0

length = input("Enter length")
width = input("Enter width")

#convert input into integer because input is always string 
length = int(length)
width = int(width)

#process/expression 
# variable-name = variable-name2 symbol(+-*/) variable-name3
area = length * width
print("Area is =",area)