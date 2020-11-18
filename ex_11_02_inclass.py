## Exercise 2: Write a program to look for lines of the form:

## New Revision: 39772

## Extract the number from each of the lines using a regular expression and the
## findall() method. Compute the average of the numbers and print out the average as an integer.

import re

fname = input("Enter a file name: ")
ofile = open(fname)
numberlist = list()

for line in ofile :
    line = line.rstrip()
    nums = re.findall('^New .*: ([0-9]+)', line)
    if len(nums) > 0 :
        for num in nums:
            num = int(num)
        numberlist.append(num)

print(int(sum(numberlist)/len(numberlist)))
