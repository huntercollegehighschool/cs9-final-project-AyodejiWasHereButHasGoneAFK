#HANG MANNN
'''
   _ _
 / o o \
|   ^   |
 \ _ _ /
   /|\
  / | \
 /  |  \
    |
   / \
 _/   \_
'''
#possible hangman minigame
import random
import time
import os
os.system('clear')
us = "_ "
tries = 6
attempt = 0
words = ["computer", "coding", "print", "import", "racket", "hunter", "logic", "input", "final", "syntax", "string"]
x = random.randint(1,10)
wordcount = list(words[x])
wc = (len(wordcount))
space = us*wc
import page6
print("   _ _")
print(" / o o \\")
print("|   ^   |")
print(" \ _ _ /")
print("   /|\\")
print("  / | \\")
print(" /  |  \\")
print("    |") 
print("   / \\")
print(" _/   \\_")
print(space)
SpacLis = list(space)
print(wordcount)
print("Welcome to HANGMAN!")
time.sleep(1)
kr = 0
yas = 0
while tries > 0:
  g1 = input("Guess a letter! ")
  g1 = g1.lower()
  read = 0
  read2 = 0
  os.system('clear')
  if g1 in wordcount:
    yas = 0
    kr = 0
    g1mod = [g1]
    while str(g1mod) != str(list(wordcount[read])):
      read = read + 1
    print(read)
    while str(kr) <= str(2*(read+1)):
      if list(space[kr]) != ['_'] and list(space[kr]) != [' ']:
      yas = yas +1
      kr = kr + 1
      read = read - yas
    space = space.replace('_', str(g1), read+1)
    space = space.replace(str(g1), '_', read)
    print(space)
  else:
    print(space)  
    print("Your letter was not in the word. ")
    tries = tries -1
  if us not in space:
    print("YOU WON!")
    tries = -1
if tries == 0:
  print("You're out of tries!!")

'''
g2 = input("Guess another letter: ")
g2 = g2.lower()
read = 0
os.system('clear')
if g2 in wordcount:
  g2mod = [g2]
  while str(g2mod) != str(list(wordcount[read])):
    read = read +1
  space = space.replace('_', str(g2), read+1)
  space = space.replace(str(g2), '_', read)
  print(space)
  print(read)
elif g2 == g1:
  print("You've already picked this letter.")
else:
  print("Your letter was not in the word. ")
  tries = tries -1
g3 = input("Guess another letter: ")
g3 = g3.lower()
read = 0
os.system('clear')
if g3 in wordcount:
  g3mod = [g3]
  while str(g3mod) != str(list(wordcount[read])):
    read = read +1
  space = space.replace('_', str(g3), read+1)
  space = space.replace(str(g3), '_', read)
  print(space)
  print(read)
elif g3 == g2 or g3 == g1:
  print("You've already picked this letter.")
else:
  print("Your letter was not in the word. ")

g4 = input("Guess another letter: ")
g4 = g4.lower()
read = 0
os.system('clear')
if g4 in wordcount:
  g4mod = [g4]
  while str(g4mod) != str(list(wordcount[read])):
    read = read +1
  space = space.replace('_', str(g4), read+1)
  space = space.replace(str(g4), '_', read)
  print(space)
  print(read)
elif g4 == g1 or g4 == g3 or g4 == g2:
  print("You've already picked this letter.")
else:
  print("Your letter was not in the word. ")
'''