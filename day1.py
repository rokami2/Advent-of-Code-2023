#imports
import re

#initalize vars
arystrTemp = []
numarray = []
converted_numbers = []
index = 0
norepeat = 0
num = ""
converted_int = 0
code = 0
total = 0


#read each line and if it has a number add it to numstr
with open("input.txt", "r") as cypher:
        
        linenum = re.findall("\d+", cypher.read())
    
        if linenum:
            numarray += linenum

#iterate through numstr and add numbers together  

for index, num in enumerate(numarray):
    print("Line", index, "number pulled", num)
    # check if the number isn't two digits and change accordingly for first number
    if int(num) < 10:
        converted_int = num + num
    # logic to check if the number is too high and change the number accordingly
    elif int(num) > 99:
        converted_int = num[0] + num[-1]
    else:
        converted_int = num

    #put converted integers into a new array
    converted_numbers.append(converted_int)

#add numbers together to create code
for index2, con_num in enumerate(converted_numbers):
     code += int(con_num)
    

#prints the result out for input on advent of code website
print(code)