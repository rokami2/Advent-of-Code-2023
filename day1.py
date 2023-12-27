#imports
import re
import numpy as np

#initalize vars
numarray = []
index = 0
codeindex = -1
num = ""
converted_int = 0
code = 0
total = 0


#read each line and if it has a number add it to numstr
with open("input.txt", "r") as cypher:
        
        linenum = re.findall("[0-9]+", cypher.read())
        print(linenum)

        if linenum:
            numarray += linenum

#iterate through numstr and add numbers together
#ToDo make sure that no numbers are added more than once 
num = numarray[index]     

for index in range(0, len(numarray), 2):

    # check if the number isn't two digits and change accordingly for first number
    if int(num) < 10:
        converted_int = num + num
    # logic to check if the number is too high and change the number accordingly
    elif int(num) > 99:
        converted_int = num[0:2]
    else:
        converted_int = num

    num = numarray[index+1]

    # check if the number isn't two digits and change accordingly for second number
    if int(num) < 10:
        converted_int2 = num + num
    # check if the number is too high and change the number accordingly
    elif int(num) > 99:
        converted_int2 = num[0:2]
    else:
        converted_int2 = num

    if index % 2 == 0:
        total = int(converted_int) + int(converted_int2)
        print(total, "=", converted_int, "+", converted_int2)
        code += total
        converted_int = converted_int2
    
    index += 1

#prints the result out for input on advent of code website
print (code)