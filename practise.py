import math
a = int(input("Enter a number first:"))
b = int(input("Enter second number:"))
sum = a+b
print("The sum of numbers are:", sum)
sub = a-b
print("The subtraction of numbers is:", sub)


u = input("Enter your first name:")
print("Length of string is: ", len(u))
print(u.count("z"))


Marks = int(input("Enter marks of the student:-"))
if (Marks >= 90):
    print("Grade of student is A")
elif (90 > Marks >= 80):
    print("Grade of student is B")
else:
    print("Student is Pass")


n = int(input("Enter a number to find even or odd: "))
if (n % 2 == 0):
    print("Number entered is even")
else:
    print("Number entered is odd")


a = int(input("Enter a number:-"))
print(a)
b = int(input("Enter a number:-"))
print(b)
c = int(input("Enter a number:-"))
print(c)

if (a > b):
    if (a > c):
        print(a, "is the biggest number between these three numbers.")
elif (b > a):
    if (b > c):
        print(b, "is the  biggest number between these numberds")
else:
    print(c, "is biggest number between these three numbers")


z = int(input("Enter a number:_"))
print(z)
if (z % 7 == 0):
    print("Number is the multiple of 7")
else:
    print("Its not the multiple of 7")


l = [2, 4, 6]
l.append(8)
print(l)


L = []
for a in range(4):
    s = int(input("Enter a movie name:-"))
    L.append(s)
    u = L.sort()
    print(u)
    print(L)


t = ("C", "D", "A", "A", "B", "B", "A")
C = t.count("A")
print(C)


t = ["C", "D", "A", "A", "B", "B", "A"]
f = t.sort()
print(t)

t = ["C", "D", "A", "A", "B", "B", "A"]
u = ["1", "2"]


def str_len(list):
    print(len(list))


str_len(t)
str_len(u)


def sum():
    a = int(input())
    b = int(input())
    c = int(input())
    d = a+b+c
    print(d)


sum()


def factorial():
    n = int(input("Enter a number to find factorial:_"))
    z = math.factorial(n)
    print(z)


factorial()


def convert(US):
    US = int(input("Enter amount to convert in pkr:_"))
    PKR = US*287
    print("the amount of dollors in replacement of PKR is ", PKR)


convert(87)
11
