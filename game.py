import random
import turtle

def number_generator(number_one, number_two):
    #Generate a random number and return it
    generated_number = random.randrange(number_one, number_two)
    return generated_number


def check_number():
    if input_nr == gen_nr:
        print("YES!")
    elif input_nr > gen_nr:
        print("Your numeber is too big!")
    elif input_nr < gen_nr:
        print("Your number is too small!")
    else:
        print("NOPE!")


#Input the range to guess
print("Set a range!")
input_one = int(input("Your number one: "))
input_two = int(input("Your number two: "))

# Start function and store generated number into a variable
gen_nr = number_generator(input_one, input_two)

print(gen_nr)

# save input into a variable
input_nr = int(input("Your Number: "))
check_number()
