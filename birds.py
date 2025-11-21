import time
import os

frame_a = r"""
         _/ '>           
    _ _.-'(   )'-._ _     
   '=._.=-(   )-=._.='    
          |/-\|           
          Y   Y 
Gwaaak!          
"""
frame_b = r"""                 
_-  \_   _/"=_   _/  -_ 
-_    `-'(   )`-'    _- 
 `=.__.=-(   )-=.__.='  
         |/-\|           
"""

print("I hear something in the distance!")
time.sleep(1)
print("what could it be?")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
print("Arhaaaaa!#!!")
time.sleep(0.5)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(0.5)
print("!!!!!Arhaaaaa!#!!!!!!")

while True:   
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(frame_a)
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(frame_b)