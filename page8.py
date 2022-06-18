import time
import os
from threading import Timer

timeout = 1
t = Timer(timeout, print, ['AUSTIN: Sorry, you took too long, next time, try to respond in under 10 seconds '])
t.start()
triv0 = input("AUSTIN: What is the first letter of the alphabet? You must answer in less than 10 seconds")
print(answer)
print(triv0)
t.cancel()