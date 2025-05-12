import random
names= input("what are names? write here ")
name =names.split(",")

who_will_pay = random.choice(name)
print(who_will_pay+" will pay the bill today!!")