MIN_AGE = 0
MAX_AGE = 150
age = int(input("What is your age? "))
while MIN_AGE > age or age > MAX_AGE:
    age = int(input("What is your age? "))
if age >= 18:
    print("Adult")
else:
    print("Child")
print(age)
