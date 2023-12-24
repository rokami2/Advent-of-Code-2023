#imports
import re
import numpy as np

#initalize vars
numstr = ""
numarray = []
index = -1
codeindex = -1
num = ""
converted_int = 0
code = []
total = 0

# #read the file
# cypher = open("input.txt", "r")

# #read the first line
# line = cypher.readline()
# print(line)


#read each line and if it has a number add it to numstr
with open("input.txt", "r") as cypher:
        
        linenum = re.findall("[0-9]+", cypher.read())
        print(linenum)

        if linenum:
            numstr += ''.join(linenum)
            numarray += linenum
            print(linenum)


        #if line only has one number add it twice
        # if linenum2:
        #     numstr += ''.join(linenum)
# print(numstr)
# print(numarray)
#iterate through numstr and add numbers together      
for index in range(0, len(numstr), 2):
    # print(char)

    num = numstr[index:index+2]

    converted_int2 = int(num)
    # print(num)
    if index % 2 == 0:
        converted_int2 = int(num)
        total = converted_int + converted_int2
        print(total, "=", converted_int, "+", converted_int2)
        code += str(total)
    
    converted_int = converted_int2
    index += 1
    
for codeindex in code:
     result = code[codeindex]

     print(result)