#write a python function that prompts the user for her last name and gender.... return their name 

Lname = input("what is your last name?")
gender = input("what is your gender m or f")

def lastname(Lname, gender):
    if gender == 'm':
        accronuim = 'Mr.' 
    elif gender == 'f':
        accronuim = 'Miss.'
    
    output = accronuim + Lname

    return output

print(lastname(Lname, gender))


# write a function that asks what year you where born and returns your age 

userYear = input('What year were you born?')

def ageCalc(userYear):
        age = 2026 - userYear 
        return age 

print(f"You are {ageCalc(userYear)} years old")


