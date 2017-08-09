import random
import turtle
import urllib
import os


my_turtle = turtle.Turtle()

#def test():

def turtle(n):
    for i in range(n):
        my_turtle.forward(100)
        my_turtle.right(n + 10)

def number_generator(number_one, number_two):
    #Generate a random number and return it
    generated_number = random.randrange(number_one, number_two)
    return generated_number


def dec_n():
    print("Test")
    input_one = int(input("Nummer eins: "))
    input_two = int(input("Nummer zwei: "))

    random_nr = number_generator(input_one, input_two)

    input_saved = []

    while True:

        input_random = int(input("Deine Nummer: "))

        if random_nr == input_random:
            print("Genau!")
            input_saved.append(input_random)
            print(input_saved)

            turtle(input_saved[0])


            home()
            break
        elif random_nr > input_random:
            print("Nummer zu klein")
            input_saved.append(input_random)
            print(input_saved)
        elif random_nr < input_random:
            print("Nummer zu groß")
            input_saved.append(input_random)
            print(input_saved)
        else:
            print("Fehler!")




def dec_a():
    print("Test")

def dec_s():
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
