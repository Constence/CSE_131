"""
get temp -----> gives far to main

convert ------> gives cel to main               main 
       <------- gets far from main

display  <------- gets cel from main
"""

def getTemperature(): 
    far = input("what is the temp in far")
    return far

def convert(far): 
    cel = (far - 32) * 5/9
    return cel

def display(cel): 
    print(f"The weather in cel is {cel}") 

def main(): 
    user_far = getTemperature()
    cel = convert(user_far)
    display(cel)

    