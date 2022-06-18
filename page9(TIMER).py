#Use of this page is optional. If you use code here, make sure either import page4 or from page4 import * appear on your main.py page.
import time
import os
time.sleep(1)
import page1
start = time.time()
triv0 = input("AUSTIN: Let's try this again. \nYou must answer in less than 10 seconds")
end = time.time()
triv0 = triv0.lower()
if end - start > 10:
  print("AUSTIN: Sorry, you took too long, next time, try to respond in under 10 seconds\nGame Over.")
  time.sleep(1.5)
  os.system('clear')
  import page4
elif triv0 == 'a':
  import page3
  print("AUSTIN: Wow, you're a natural! If that were an enemy they'd be toast! That was easy!")
else:
  print("AUSTIN: I really don't know what to tell you, you messed up prett bad there...")
  time.sleep(2)
  print("Maybe you're not the one for the job. Sorry to bother you, I'll see you next computer science class")