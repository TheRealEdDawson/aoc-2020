#aoc-2020-day2

# Problem: Validate a set of passwords.
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The policy shows a range, being the lowest and highest number of the given letter are allowed in the password.

import sys
import string

line = " "
password = "."
tripledata = []
requiredchar = " "
range = "."
rangedata = []
lowerlimit = 0
upperlimit = 0
counter = 0
charcount = 0
validpasswordcount = 0
validstate = 0

#part 1 solution
f = open("z_day-2-data.txt", "r")
for line in f:
    tripledata = line.split(' ')
    requiredchar = tripledata[1]
    requiredchar = requiredchar.strip(':')
    range = tripledata[0]
    rangedata = range.split('-')
    lowerlimit = rangedata[0]
    lowerlimit = int(lowerlimit)
    upperlimit = rangedata[1]
    upperlimit = int(upperlimit)
    password = tripledata[2]
    #print (password)
    for c in password:
        if (c == requiredchar):
            counter = counter + 1
    #print ("There was", counter, "*", requiredchar, "character(s).")
    #print ("Lower limit is", lowerlimit)
    #print ("Upper limit is", upperlimit,"\n")
    if (counter >= lowerlimit):
        if (counter <= upperlimit):
            #print ("This password is valid.\n")
            validpasswordcount = validpasswordcount + 1
    counter = 0
print ("\n\nThere were", validpasswordcount, "valid passwords (part 1).\n")
validpasswordcount = 0
#Part 2 problem: the policy now means that the given character must occur in either the first character position or the second position of the string based on the "range" data point. Also, the given character cannot occur at both specified locations.

#Part 2 Solution
f = open("z_day-2-data.txt", "r")
for line in f:
    tripledata = line.split(' ')
    #print (tripledata)
    password = tripledata[2]
    #print ("Password:", password)
    charcount = len(password)
    #print ("Actual password length is", charcount)
    charcount = (charcount - 1)
    #print ("Password length is:", charcount)
    requiredchar = tripledata[1]
    requiredchar = requiredchar.strip(':')
    range = tripledata[0]
    #process position data
    rangedata = range.split('-')
    #set up position one data
    positionone = rangedata[0]
    positionone = int(positionone)
    #print ("Position 1:", positionone)
    positionone = (positionone - 1)
    #print ("Adjusted position 1 value is", positionone)
    #set up position 2 data
    positiontwo = rangedata[1]
    positiontwo = int(positiontwo)
    #print ("Position 2:", positiontwo)
    positiontwo = (positiontwo - 1)
    #print ("Adjusted position 2 value is", positiontwo)
    #read position one
    if (requiredchar == password[positionone]):
        validstate = validstate + 1
        #print ("Position 1 match.")
    #read position two
    if (requiredchar == password[positiontwo]):
        validstate = validstate + 1
        #print ("Position 2 match.")
    #final scoring
    #if (validstate == 0):
        #print ("This password is NOT valid (no match).\n")
    if (validstate == 1):
        #print ("This password is valid (one match).\n")
        validpasswordcount = validpasswordcount + 1
    #if (validstate == 2):
        #print ("This password is NOT valid (double match).\n")
    validstate = 0

print ("\n\nThere were", validpasswordcount, "valid passwords (part 2).")
