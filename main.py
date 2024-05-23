## Standard Library && and, or
## https://docs.python.org/3/library/index.html

from random import randint

print("roll the dice!");
dice = randint(0, 7)
if dice > 0 and dice  < 7 :
  print("you roll a ",dice)
elif dice == 0 or dice == 7 :
  print(dice, " is an invaid value in this dice")