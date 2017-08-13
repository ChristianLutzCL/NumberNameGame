#NumberGame and NameGame
#LosBopfos 2017

#---- IMPORT ----
import random
import names



#---- FUNCTIONS ----
def number_generator(number_one, number_two):
    #Generate a random number and return it
    generated_number = random.randrange(number_one, number_two)
    return generated_number


def home():
    print("--------MENU--------")
    print("[A] - NumberGame")
    print("[B] - NameGame")
    print("[Q] - Quit")
    print("--------------------")
    print("")

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
    print("Welcome to NumberGame!")
    print("Set a range to guess")
    num1 = int(input("Number one: "))
    num2 = int(input("Number two: "))

    random_number = number_generator(num1, num2)

    while True:
        your_number = int(input("Your number: "))

        if your_number == random_number:
            print("Correct!")
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

    #name = ["Peter", "Franz", "Holger", "Anna", "Nina", "Lena", "Lea", "Lara"]

    name = names.get_first_name()
    #print(name)
    name_len = len(name)
    #choosen_name = name[random.randrange(0, name_len)] # For choosing a name in the names list
    name_checker(name)


def name_checker(c_name):

    while True:
        name = c_name
        name_len = len(name)

        random_pos = random.randrange(1, name_len)
        letter_one = name[0]
        letter_rand = name[random_pos]


        def name_string_generator():
            name_string_list = []

            random_pos2 = random.randrange(1, name_len)
            letter_rand2 = name[random_pos2]

            if name_len != 5:
                print("The letter on position " + str(random_pos2) + " is " + str(letter_rand2))
                while letter_rand == letter_rand2:
                    print("letter_rand == letter_rand2")
                    break
                else:
                    print("letter_rand != letter_rand2")

            for x in name:
                if x == letter_one or x == letter_rand or x == letter_rand2:
                    name_string_list.append(x)
                else:
                    name_string_list.append("*")

            name_string = "".join(name_string_list)
            return name_string

        print("------------------------------------------------------------")
        print("The length of the name is " + str(name_len))
        print("The letter on position one is " + str(letter_one))
        print("The letter on position " + str(random_pos) + " is " + str(letter_rand))
        print(name_string_generator())
        print("------------------------------------------------------------")

        input_name = input("Name: ")

        if input_name == name:
            print("Wow! You Won!")
            home()
            break
        else:
            print("Sorry, wrong...")
            print("The right name was " + name)


def quit():
    print("quit")



home()
