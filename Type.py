import statistics
from time import sleep
'''
x = 25
y = 3.14

print(type(x), type(y))

a = 10
b = 3
print(type(a/b))
print(type(a//b))
print(type(a*2.5))

s1 = 67
s2 = 35
s3 = 54
average = (s1 + s2 + s3)/3
print(average)

scoretable = {}

scoreEntries = int(input("Enter amount of score entries: "))

for _ in range(scoreEntries):
    name = input("Enter name: ")
    score = int(input("Enter score: "))
    scoretable.update({name: score})

print(scoretable)

score1 = int(input("Enter the first score: "))
score2 = int(input("Enter the 2nd score: "))
score3 = int(input("Enter the 3rd score: "))
scoretable = [score1, score2, score3]
print(scoretable)
averagescore = statistics.mean(score1, score2, score3)

name = "Alex"
greeting = "Hello" +name
print(greeting)
print(name.upper(),len(name))

forename = input("Enter your first name: ")
surname = input("Enter your last name: ")
fullname = forename + surname
len(fullname)

if len(fullname) > 20:
    print("Username too long, please re-enter:")
    sleep(0.5)
    forename = input("Enter your first name: ")
    surname = input("Enter your last name: ")
    fullname = forename + surname
    len(fullname)
else:
    print("Hello, "+ fullname)
'''