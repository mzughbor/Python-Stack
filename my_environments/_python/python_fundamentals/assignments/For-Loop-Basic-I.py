# Q-01 
# Basic - Print all integers from 0 to 150.
for i in range(151):
    print(i)
print("\n----------------------------------------------------------------------------------------\n")

# Q-02
#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5,1001,5):
    print(i)
print("\n----------------------------------------------------------------------------------------\n")

# Q-03
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(0,101):    
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
print("\n----------------------------------------------------------------------------------------\n")

# Q-04  
#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for i in range(0,500001):
    if i % 2 != 0:
        sum += i
else:
    print(f"{sum:,}") 
print("\n----------------------------------------------------------------------------------------\n")

# Q-05
#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018,0,-4):
    print(i)
print("\n----------------------------------------------------------------------------------------\n")

# Q-06
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""
lowNum = 2
highNum = 9
mult = 3 
""" 
lowNum = 92
highNum = 8
mult = -3   # it's working properly with negitve integers. and fliped high and low...
 
# doesn't make any sense to increment loop by mult, you increment any thing in 
# lower starting point var so, not getting real multiple of the mult value...
# the idea is to fix starting point to be one of the mutiples then use the incrementer in for loop.

if lowNum % mult != 0:
    lowNum += mult - (lowNum % mult) # get the right starting point so you loop as exact number you need.
    print("Fixed starting point",lowNum)

for answer in range(lowNum, highNum+1, mult): 
    print(answer)

print("\n----------------------------------------------------------------------------------------\n")