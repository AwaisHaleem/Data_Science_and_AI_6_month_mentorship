# * Assignment
# get a person's wheight and height and calculate his BMI
# BMI = Weight(kg) / height (m)
name = input("What is your name? ")
weight = float(input("What is your weight in Kg? "))
height = float(input("What is your height in m? "))


bmi = weight / (height*height)

if bmi <= 18.4:
    print(f"Mr. {name}! you are under weight")
elif bmi > 18.5 and bmi < 24.9:
    print(f"Mr. {name}! your weight is normal")
elif bmi > 25 and bmi < 39.9:
    print(f"Mr. {name}! you are over weight")
else:
    print(f"Mr. {name}! you are obese")
