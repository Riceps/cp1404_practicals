names = ["John", "Tarina", "Jake", "Kaila"]
ages = [53, 52, 22, 20]
oldest_age = 0
for i, age in enumerate(ages):
    if age > oldest_age:
        oldest_age = age
        oldest_person = names[i]
print(oldest_person)
