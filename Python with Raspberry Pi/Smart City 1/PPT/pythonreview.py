
#Python review

#Python data types --- string

s1 = "foo bar" 
print(s1)
s2 = 'foo bar' 
print(s2)
s3 = r"c:\dir\new" # raw (== 'c:\\dir\\new') 
print(s3)
s4 = """Hello 
    world""" 
print(s4)
len = len(s4) 
print(len)

#Python data types --- list

L1 = [1, 2, 3, 4, 5]
print("List ", L1)
P1 = L1[0] # single position 
P2 = L1[0:3] # the first three elements 
print("L[0] is ", P1, " L[0:3] are ", P2)
P3 = L1[-2:] # the last two elements 
P4 = L1[1:4] = [7,8] # substitute
print("L[-2] is ", P3, "L[1:4]are ", P4)

del L1[2] # remove elements 
print("List after del L1[2] ", L1)
L1.append(6) # x is a value 
print("List after append(6) ", L1)
L2 = [7, 8, 9]
L1.extend(L2) # or: L3 = L + L2 
print("List after extend(L2) ", L1, " L2 ", L2)
L1.pop() # simple stack (with append) 
print("List after pop() ", L1)
L1.sort() 
print("List after sort() ", L1)

x = 5
ret = x in L1 # does L1 contain x? 
print(" x in L1 ", ret)
index = L1.index(x) # index of the first occurrence 
print("L1.index(x) ", index)

#Python data types --- tuple
t1 = ('Jan', 'Feb', 2017, 2018)
print(" t1 ", t1)
t2 = (1, 2, 3, 4, 5, 6, 7 )
print(" t2 ", t2)
print("t1[0]: ", t1[0])
print "t2[1:5]: ", t2[1:5];
t3 = t1 + t2
print("t1 + t2 ", t3)
for x in t1: print x

#Python data types --- dictionary
D1 = {'f1': 10, 'f2': 20} # dict creation
print("D1 ", D1)

for k in D1: print(k) # keys 
for v in D1.values(): print(v) # values 
L1 = list(D1.keys()) # list of keys 
print("list(D1.keys()) ", L1)
S1 = sorted(D1.keys()) # sorted list of keys
print("sorted(D1.keys()) ", S1)

D3 = {} 
D3[(1,8,5)] = 100 # 3D sparse matrix 
print("D3 after D3[(1,8,5)] = 100 ", D3)
S2 = D3.get((1,8,5))
print("D3 after D3.get((1,8,5)) ", S2)

#Python data types --- loops
for x in range(1,6): print(x) # 1, 2, 3, 4, 5 

# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
	
#Python data types --- functions
# Define our 3 functions
def func1():
    print("Hello Func1!")

def func2_with_args(name, greeting):
    print("Hello, %s I wish you %s"%(name, greeting))

def plusnum(n1, n2):
    return n1 + n2

# print(a simple greeting)
func1()

#prints - "Hello, David, I wish you a happy new year!"
func2_with_args("David ", "a happy new year!")

# after this line x will hold the value 3!
x = plusnum(23, 12)
print("plusnum(23, 12) ", x)

#Python data types --- input / output (can not be demonstrate online)
import sys
x = raw_input("Name: ") 
for line in sys.stdin: 
    print(line)

#String input buffer
from StringIO import StringIO 
buf = StringIO() 
sys.stdout = buf 
print("Hello") 
x = buf.getvalue()

#Python data types --- exception handle
try:
    num = float(input("Your number: "))
    ret = 1.0 / num
    print("ret = 1.0 / num ", ret)
except ValueError:
    print("input should be either int or a float")
except ZeroDivisionError:
    print("Infinity")
finally:
    print("There may or may not have been an exception.")
	
#Python data types --- object oriented programming
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Honda"
car1.color = "black"
car1.kind = "sedan"
car1.value = 24000.00

car2 = Vehicle()
car2.name = "Toyota"
car2.color = "white"
car2.kind = "suv"
car2.value = 36000.00

# test code
print(car1.description())
print(car2.description())
