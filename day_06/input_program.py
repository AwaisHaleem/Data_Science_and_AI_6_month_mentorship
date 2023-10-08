name = input("What is your naem")       # take user name
print(name)


# greating
print("hello", name)


first_person_name = input("What is your name? ")
first_person_age = input("What is your age? ")

second_person_name = input("What is your name? ")
second_person_age = input("What is your age? ")

# type caste the input ages
first_person_age = int(first_person_age)
second_person_age = int(second_person_age)

if first_person_age > second_person_age:
    print(first_person_name, " is older than ", second_person_name)
else:
    print(second_person_name, " is older than ", first_person_name)
