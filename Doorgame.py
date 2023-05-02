import random

name = input("Please insert your Charecters name:")
print("Hello", name)
print("")


def intro():
    print("Welcome to the DoorGame!")
    Title()


def Title():
    print("This is the DoorGame. Where you will have to enter through the correct doors to escape. But entering into the wrong door will result in unknown tragedy!")
    print("")
    start_game()


def start_game():
    start = input("To start the game type Yes to exit type  No:")
    print("")
    if start == "Yes":
        doors_outcome1()
    elif start == "No":
        exit()


def door_choice1(decision):
    print("You have enterd a cold wet room. Choose the correct door to escape out of the 4 doors.  Eachdoor is labeled 1-4.")

    choice = input("Enter which door number you would like to enter: ")
    print("")
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("Please enter a valid answer")
        return False
    elif int(choice) == decision:
        return True


def door_choice2(decision1, decision2, death_door):
    choice = input(
        "Each of the 8 doors is labeled 1-8 enter the which door number you would like to enter: ")
    print("")

    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8":
        print("Please enter a valid answer")
        return False
    elif int(choice) == decision1:
        print(
            "You have escaped to the land  of  paradise congragulations", name)
        return True
    elif int(choice) == decision2:
        print("You have escaped to the land of treasures congragulations", name)
    elif int(choice) == death_door:
        print("You chose the death door", name, "you have died")
        return True


def doors_outcome1():
    correct_door = random.randint(1, 4)
    while not door_choice1(correct_door):
        print("Sorry", name,
              " the door you have entered was full of fire please try again.")
    print("Congragulations ", name, " you have entered the correct door")
    door_outcome2()


def door_outcome2():
    print("You have entered a new room ", name,
          " with 8 doors all doors are bright red with gold knobs.")
    print("This room has a giant dragon in a room full of warm sand.")
    print("The dragon says that there is 8 doors and 2 doors that will lead you to escape, 1 of them will lead you to treasures the other will lead to a land of paradise")
    print("")

    escape_door1 = random.randint(1, 8)
    escape_door2 = random.randint(1, 8)
    death_door = random.randint(1, 8)

    while escape_door1 == escape_door2:
        escape_door2 = random.randint(1, 8)

    while death_door == escape_door1 or death_door == escape_door2:
        escape_door2 = random.randint(1, 8)

    while not door_choice2(escape_door1, escape_door2, death_door):
        print("The Door you have entered floors have Plummeted try again.")


intro()
