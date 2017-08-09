import random
import turtle
import urllib
import os

my_turtle = turtle.Turtle()

#def test():

def turtle():
    for i in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)

def number_generator(number_one, number_two):
    #Generate a random number and return it
    generated_number = random.randrange(number_one, number_two)
    return generated_number

def dec_n():
    os.system('clear')
    print("Test")

def home():
    print("------Welcome------")
    print("Choose the type of the game")
    print("-N- Normal")
    print("-A- Advanced")
    print("-S- Simple")


    decision = input("Decision: ")

    if decision == "N" or decision == "n":
        print("Pressed: N")
        dec_n()
    elif decision == "A" or decision == "a":
        print("Pressed: A")
        dec_a()
    elif decision == "S" or decision == "s":
        print("Pressed: S")
        dec_s()
    else:
        print("Wrong decision")


def check_number():
    while True:
        # save input into a variable
        input_nr = int(input("Your Number: "))
        my_turtle.forward(input_nr)

        # Try to find the correct number. If found, break the while loop
        if input_nr == gen_nr:
            print("Yes!")
            turtle()
            break
        elif input_nr > gen_nr:
            print("Too big")
        elif input_nr < gen_nr:
            print("Too small")
        else:
            print("Wrong!")

home()
#Input the range to guess
#print("Set a range!")
#input_one = int(input("Your number one: "))
#input_two = int(input("Your number two: "))

# Start function and store generated number into a variable
#gen_nr = number_generator(input_one, input_two)

#print(gen_nr) # gen_nr output

#check_number()
