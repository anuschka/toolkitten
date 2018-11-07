#soc01hw

#A Few Things to Try
#1 Write a program that tells you the following:
#How many hours are in a year?
def isleapyear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
year =int(input('Enter a year:'))
if isleapyear(year):
    print(f"There are {366*24} hours in year {year}.", end=' ')
else:
    print(f'There are {365*24} hours in year {year}.', end=' ')

x=input ("Press any key to next homework")

#- Minutes in a decade. How many minutes are in a decade?
print(f'There are {10*365*24*60} in a decade.')

x=input ("Press any key to next homework")
#- Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
print(f'I am {40*365*24*60*60} seconds old.')

x=input ("Press any key to next homework")
#- Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
print(f'Andreea Visanoiu is {48618000/(365*24*60*60)} years old.')

x=input ("Press any key to next homework")

#Here are some tougher questions: - How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
print(f'It takes {pow(2,32)/(24*60*60*1000)} days for a 32-bit system to timeout.')

x=input ("Press any key to next homework")

#How about a 64-bit system?
print(f'It takes {pow(2,64)/(24*60*60*1000)} days for a 64-bit system to timeout.')

x=input ("Press any key to next homework")

#Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am
#if you know it, use 12:00 noon midday) - you will need Python modules.

import datetime
delta = datetime.datetime.now()-datetime.datetime(1980, 7, 6, 12, 0)
print (f'My exact age is {delta.days} days and {delta.seconds} seconds')

x=input ("Press any key to next homework")
#Write a program that asks for a person’s first name, then middle, and then last. 
#Finally, it should greet the person using their full name.

firstname = input("Enter your first name please:")
middlename = input("Enter your first name please:")
lastname = input("Enter your first name please:")
print(f"Hello {firstname} {middlename} {lastname}. It was nice meeting you!")

x=input ("Press any key to next homework")

#Write a program that asks for a person’s favorite number. Have your program add 1 to the
# number, and then suggest the result as a bigger and better favorite number. 
# (Do be tactful about it, though.)

num = input("Enter your favorite number")
try:
   val = int(num)
   print(f"A better number is: {val+1}")
except ValueError:
   print("Please enter a number!")

#Write an angry boss program that rudely asks what you want. Whatever you answer, the angry
#boss should yell it back to you and then fire you. For example, if you type in I want
#a raise, it should yell back like this: 'WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!'


question = input("What do you want?")
print(f"\'WHADDAYA MEAN \"{question.upper()}\"?!? YOU'RE FIRED!!\'")

#Here’s something for you to do in order to play around more with center, ljust, and rjust: 
#write a program that will display a table of contents (see day3.md to review the format)

print("Table of Contents")
print("")
print("Chapter 1: Getting Started".ljust(30," ")+"page 1".ljust(20," "))
print("Chapter 2: Numbers".ljust(30," ")+"page 9".ljust(20," "))
print("Chapter 3: Letters".ljust(30," ")+"page 13".ljust(20," "))
                
                