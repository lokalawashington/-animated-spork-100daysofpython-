import random
name_string = input("Give me everybody names separated by commas")
name = name_string.split(",")
print(name_string)

random_name = len(name)
random_choice = random.randint(0,random_name-1)
#picks a random name
print(random_choice)
person_who_wil_pay = name[random_choice]
print(f"{person_who_wil_pay} is going to pay")


