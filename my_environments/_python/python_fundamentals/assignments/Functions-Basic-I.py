print("\n--1-------------------------------------------------------------------------------------\n")

#1 
def a():
    return 5 
print(a())
#>>> 5

print("\n--2-------------------------------------------------------------------------------------\n")

#2
print(a()+a())
#>>> 10

print("\n--3-------------------------------------------------------------------------------------\n")

#3
def a():
    return 5  # anything after any return will not run
    return 10
print(a())
#>>> 5

print("\n--4-------------------------------------------------------------------------------------\n")

#4
def a():
    return 5 
    print(10)
print(a())
#>>> 5

print("\n--5-------------------------------------------------------------------------------------\n")

#5
def a():
    print(5)
x = a()
# >>> will print 5 but None will be assigned as a value for the x ofcourse

print("\n--6-------------------------------------------------------------------------------------\n")

#6
def a(b,c):
    print(b+c)
#print(a(1,2)+a(2,3))
# >>> 8
# ok, I didn't get it right, case I answer it quiculy the return is not added so yes TypeError, 
# unsupported type for + 'NoneType' and 'NoneType'

print("\n--7-------------------------------------------------------------------------------------\n")

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# >>> 25 as string ofcourse

print("\n--8-------------------------------------------------------------------------------------\n")

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# >>> print 100 and return 10 and print it too

print("\n--9-------------------------------------------------------------------------------------\n")

#9
def a(b,c):
    if b < c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3)+a(5,3))
# >>> print 7
# >>> print 14
# >>> print 21

print("\n--10------------------------------------------------------------------------------------\n")

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# >>> 8

print("\n--11------------------------------------------------------------------------------------\n")

#11
b = 500
print (b)
def a():
    b = 300
    print (b)
print(b)
a()
print (b)
# >>> print 500
# >>> 500
# >>> 300
# >>> 500

print("\n--12------------------------------------------------------------------------------------\n")

#12
b = 500
print (b)
def a():
    b = 300
    print (b)
    return b
print (b)
a()
print (b)
# >>> 500
# >>> 500
# >>> 300
# >>> 500

print("\n--13------------------------------------------------------------------------------------\n")

#13
b = 500
print (b)
def a():
    b = 300
    print (b)
    return b
print (b)
b=a() 
print (b)
# >>> 500
# >>> 500
# >>> 300
# >>> 300

print("\n--14------------------------------------------------------------------------------------\n")

#14
def a():
    print (1)
    b()
    print (2)
def b():
    print (3)
a()
# >>> 1
# >>> 3
# >>> 2
# >>> 

print("\n--15------------------------------------------------------------------------------------\n")

#15
def a():
    print (1)
    x = b()
    print(x)
    return 10
def b():
    print (3)
    return 5
y = a()
print(y)
# >>> 1 
# >>> 3
# >>> 5
# >>> 10