'''
Created on Dec 19, 2016

@author: yru289
'''
print("Hello World")

int = 7
print(int)

# float = 7.0
# print (float)

float = float(7.23)
print float


# Apostrophes Usage
bonjour = "hello's"
hello = "hello"
print bonjour

three = 3
one = 1
solution = three + one + float
print solution

# Array List Testing
array = []
array.append(4)
array.append(5)
array.append(6)
for x in array : print x

# Printing an Array Index
arraytest = 4, 5, 6, 3, 3
print arraytest[1]


# If statements with strings (use format function to print placeholders in string
if bonjour == "hello's" : print "Bonjour: %s" % bonjour
if bonjour == "hello" : print "Bonjour: {0}".format(hello)

print "The sum of 1 + 2 is {0} ".format(1 + 2) * 2


# Arithmatic
number = 1 + 2 * 3 / 4.0
print(number)

# Exponents
answer = 7 ** 2
print answer


# % Operator & format functions
name='John'
last='Smith'
print "Hello, %s" % name
print "Hello, {0} {1}".format(name,last)

data = ('John', 'Doe', 53.44)
print "Hello {0} {1} Your current balance is ${2}".format(data)