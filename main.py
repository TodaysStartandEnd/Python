## list, tuple, dictionary

#list
score = [10,20,30,40,50,"A"]
print(score.append("A+"))
print(score.insert(2,25))
print(score.remove(50))
print(score[-1])

#tuple(*immutable)
dumbbell_weight = (10,20,30,10)
print(dumbbell_weight.index(10))
print(dumbbell_weight.count(10))

#dictionary
student = {
  "name": "Sunny",
  "age": 100,
  "is_hungry": True,
   1: "one" ## checking integer key is available
}

print(student.get("name"))
print(student[1])
student.update(is_hungry=False)
print(student)
print(student.pop("age"))
print(student)