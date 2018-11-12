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
    print(f"There are {366*24} hours in year {year}.")
else:
    print(f'There are {365*24} hours in year {year}.')

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

num = input("Enter your favorite number: ")
try:
   val = int(num)
   print(f"A better number is: {val+1}")
except ValueError:
   print("Please enter a number!")

x=input ("Press any key to next homework")

#Write an angry boss program that rudely asks what you want. Whatever you answer, the angry
#boss should yell it back to you and then fire you. For example, if you type in I want
#a raise, it should yell back like this: 'WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!'


question = input("What do you want?")
print(f"\'WHADDAYA MEAN \"{question.upper()}\"?!? YOU'RE FIRED!!\'")

x=input ("Press any key to next homework")

#Here’s something for you to do in order to play around more with center, ljust, and rjust: 
#write a program that will display a table of contents (see day3.md to review the format)

print("Table of Contents")
print("")
print("Chapter 1: Getting Started".ljust(30," ")+"page 1".ljust(20," "))
print("Chapter 2: Numbers".ljust(30," ")+"page 9".ljust(20," "))
print("Chapter 3: Letters".ljust(30," ")+"page 13".ljust(20," "))

x=input ("Press any key to next homework")

#Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”

i = 99
while i>0:
  print(f'{i}  bottles of beer on the wall, {i} bottles of beer.')
  i=i-1
  if i>0:
    print(f'Take one down and pass it around, {i} bottles of beer on the wall.')
  else:
    print('Take one down and pass it around, no more bottles of beer on the wall.')
  print(" ")
print("No more bottles of beer on the wall, no more bottles of beer.")                
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
                
x=input ("Press any key to next homework")

#Whatever you say to Grandma (whatever you type in), she should respond with this: 
#HUH?! SPEAK UP, GIRL! unless you shout it (type in all capitals). 
#If you shout, she can hear you (or at least she thinks so) and yells back: 
#NO, NOT SINCE 1938! 
#To make your program really believable, have Grandma shout a different year each time, maybe
# any year at random between 1930 and 1950.
#You can’t stop talking to Grandma until you shout BYE. 

import random
phrase = " "
while phrase !="BYE":
  phrase = input("Tell something to grandma?")
  if phrase == "BYE":
    break
  if phrase.isupper() !=True:
  		print("HUH?! SPEAK UP, GIRL!")
  else:
  		year = random.randrange(1930, 1950, 1)
  		print(f"NO, NOT SINCE {year}!")
print("Goodbye!")

#What if Grandma doesn’t want you to leave? When you shout BYE, she could pretend not to hear you. 
#Change your previous program so that you have to shout BYE three times in a row. Make sure to test your program: 
#if you shout BYE three times but not in a row, you should still be talking to Grandma.

import random
phrase = " "
#counter counts consequitive "BYE" phrases
counter = 0
#exit controls the while loop. 
exit = 0
while exit !=1:
  phrase = input("Tell something to grandma?")
  if (phrase == "BYE") and (counter == 2):
    break
  elif phrase == "BYE":
    counter=counter +1
  else:
    counter=0
  if phrase.isupper() !=True:
  		print("HUH?! SPEAK UP, GIRL!")
  else:
  		year = random.randrange(1930, 1950, 1)
  		print(f"NO, NOT SINCE {year}!")
print("Goodbye!")

#Write a program that asks for a starting year and an ending year and then puts all the leap years 
#between them (and including them, if they are also leap years). Leap years are years divisible by 
#4 (like 1984 and 2004). However, years divisible by 100 are not leap years (such as 1800 and 1900) 
#unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!

startyear = int(input("Enter starting year:"))
endyear = int(input("Enter ending year:"))
def leapyr(n):
	#divisible by for and not divisible by 100 or divisible by 4 and divisible by 400
    if (n%4==0 and n%100!=0) or (n%4==0 and n%400==0):
        print (f"{n} is a leap year.")

for year in range(startyear, endyear+1):
  leapyr(year)

#Go for a walk, look around the park, try to count something. Anything! 
#And write a program about it. e.g. number of stairs, steps, windows, leaves estimated 
#in the park, kids, dogs, estimate your books by bookshelf, toiletries, wardrobe.

printf(f"Number of stairs is {3*10*2}")

#Write the program that asks us to type as many words as we want (one word per line, continuing 
#until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. 
#Make sure to test your program thoroughly; for example, does hitting Enter on an empty line always exit your program? 
#Even on the first line? And the second? Hint: There’s a lovely array method that will give you a sorted version of 
#an array: sorted(). Use it!
array = []
while True:
  word = input("Enter a word please:")
  if len(word)==0:
    break
  else:
    array.append(word)
print(sorted(array))

#Write a table of contents program here. Start the program with a list holding all of the information for your 
#table of contents (chapter names, page numbers, and so on). Then print out the information from the list in a 
#beautifully formatted table of contents. Use string formatting such as left align, right align, center.

list = ["Table of Contents","Chapter 1: Getting Started","page 1", "Chapter 2: Numbers","page 9","Chapter 3: Letters","page 13"]

print(list[0])
print("")
print(list[1].ljust(30," ")+list[2].ljust(20," "))
print(list[3].ljust(30," ")+list[4].ljust(20," "))
print(list[5].ljust(30," ")+list[6].ljust(20," "))

#Write a function that prints out "moo" n times.
def moo(n):
  for i in range(n):
    print("moo")
number=input("Enter the number of times moo is printed:")
if number<=0:
  print("You did not enter a positive integer!")
else:
  try:
    val = int(number)
    moo(val)
  except ValueError:
    print("You did not enter an integer!")

#Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school 
#Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. Make sure to test your method on a bunch of 
#different numbers. Hint: Use the integer division and modulus methods. For reference, these are the values of the letters 
#used: I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000
def roman(n):
  romanlit =""
  while n!=0:
    if n>=1000:
      romanlit = romanlit + (n//1000)*"M"
      n=n-1000*(n//1000)
    elif n>=500:
      romanlit = romanlit + (n//500)*"D"
      n=n-500*(n//500)
    elif n>=100:
      romanlit = romanlit + (n//100)*"C"
      n=n-100*(n//100)
    elif n>=50:
      romanlit = romanlit + (n//50)*"L"
      n=n-50*(n//50)
    elif n>=10:
      romanlit = romanlit + (n//10)*"X"
      n=n-10*(n//10)
    elif n>=5:
      romanlit = romanlit + (n//5)*"V"
      n=n-5*(n//5)
    else:
      romanlit = romanlit + (n)*"I"
      n=n-1*(n//1)

  return romanlit

number=int(input("Enter a number:"))
if number<=0:
  print("You did not enter a positive integer!")
else:
  try:
    val = int(number)
    print(f"Roman numeral for this number is: {roman(val)}")
  except ValueError:
    print("You did not enter an integer!")

#Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you had to 
#subtract the smaller one. As a result of this development, you must now suffer. Rewrite your previous method to return the 
#new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.
