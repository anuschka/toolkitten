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




