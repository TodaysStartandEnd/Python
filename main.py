## control statement : if, elif, else
## elif and else may or may not be used. 

score = int(input("Enter your score: "))
if score >= 90:
  print("A+")
elif score >= 80:
  print("A")
elif score >= 70:
  print("B+")
elif score >= 60:
  print("B")
elif score >= 50:
  print("C+")
elif score >= 40:
  print("C")
else :
  print("F")