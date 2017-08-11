#NumberGame and NameGame
#LosBopfos 2017

#---- IMPORT ----
import random



#---- FUNCTIONS ----
def number_generator(number_one, number_two):
    #Generate a random number and return it
    generated_number = random.randrange(number_one, number_two)
    return generated_number


def home():
    print("----MENU----")
    print("[A] - NumberGame")
    print("[B] - NameGame")
    print("[Q] - Quit")
    print("------------")

    decision = input("Your decision: ")

    if decision == "A" or decision == "a":
        number_game()
    elif decision == "B" or decision == "b":
        name_game()
    elif decision == "Q" or decision == "q":
        quit()
    else:
        print("Wrong decision. Please try again!")
        home()


def number_game():
    points = 0

    print("Welcome to NumberGame!")
    print("Set a range to guess")
    num1 = int(input("Number one: "))
    num2 = int(input("Number two: "))

    random_number = number_generator(num1, num2)

    while True:
        your_number = int(input("Your number: "))

        if your_number == random_number:
            print("Correct!")
            points += 1
            print(points)
            home()
            break
        elif your_number > random_number:
            print("Too high!")
        elif your_number < random_number:
            print("Too small!")
        else:
            print("Something gone wrong...")


def name_game():
    print("Welcome to NameGame!")
    print("You have to advise the right names based on some hints.")

    names = ["Peter", "Franz", "Holger", "Anna", "Nina", "Lena", "Lea", "Lara"]

    name_len = len(names)
    choosen_name = names[random.randrange(0, name_len)]
    print(choosen_name)

    name_checker(choosen_name)


def name_checker(c_name):

    while True:
        name = c_name
        name_len = len(name)

        random_pos = random.randrange(0, name_len)
        letter = name[random_pos]

        print("The length of the name is " + str(name_len))
        print("The letter on position " + str(random_pos) + " is " + str(letter))

        input_name = input("Name: ")

        if input_name == name:
            print("Wow! You Won!")
        else:
            print("Sorry, wrong...")


def quit():
    print("quit")



home()
