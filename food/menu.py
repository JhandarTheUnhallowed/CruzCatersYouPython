from food import items
from food import setmenu
import main

"""
This module handles everything that is related to the list of food ideas 
and the weekly menu, from importing the saved files, to setting and changing
the menu, and adding and removing dishes from the list of food ideas.

We are importing two modules (items and setmenu) as they contain the methods
needed to load and save the files containing the food ideas and the weekly menu,
while this module handles the console interface that uses these methods.
"""

"""FILE IMPORT/SAVE SECTION"""


def load_dish():
    """
    This function loads the list of food ideas.
    """
    items.load_dish_file("dishes.txt")


def save_dish():
    """
    This function is called every time you exit the dishes menu.
    It will save the current list of dish ideas.
    """
    items.save_dish_file("dishes.txt")


def load_menu():
    """
    This function loads the weekly menu.
    """
    setmenu.load_menu_file("weeklymenu.txt")


def save_menu():
    """
    This function saves the weekly menu.
    """
    setmenu.save_menu_file("weeklymenu.txt")


def load_items():
    """
    This function unifies the two loading methods so they are called
    together whenever we enter this section of the interface.
    """
    load_dish()
    load_menu()


def load_dishes():
    """
    This function displays the current list of food ideas.
    """
    display_food_ideas = items.food_idea_to_list()
    for dish in display_food_ideas:
        print(dish)


def load_menu_dishes():
    """
    This function displays the current menu of the week.
    """
    display_menu_dishes = setmenu.weekly_menu_to_list()
    for dish in display_menu_dishes:
        print(dish)


"""CONSOLE INTERFACE SECTION"""


def display_interface():
    load_items()
    print("\n===================\nMENU AND FOOD IDEAS\n===================")
    print("1: Set/Change Menu\n2: Display Dishes")
    main_input = input("What do you want to do? ")
    if main_input == "1":
        display_set_menu()
    if main_input == "2":
        display_dishes()
    else:
        main.intro_message()


def display_dishes():
    print("\n==========\nDISH IDEAS\n==========")
    load_dishes()
    change_dish = input("Would you like to edit the list of dishes?\nY/N - Input here: ")
    if change_dish.lower() == "yes" or change_dish.lower() == "y":
        action = input(
            "What would you like to do?\n1: Add a dish to list\n2: Remove a dish from the list\n3: Go back\n=>")
        if action == "1":
            dish_id, dish_name, dish_price = input(
                "To add a dish, please use this format:\nDDD(for dish_id), name, price\n=> ").split(", ")
            print(dish_id, dish_name, dish_price)
            items.add_item(dish_id, dish_name, dish_price)
            print("Dish added to list!")
            display_dishes()
        elif action == "2":
            dish_id = input("Please input the 3-letter code of the dish you wish to remove: ")
            items.remove_item(dish_id)
            print("Dish")
            display_dishes()
        else:
            display_interface()
    else:
        save_dish()
        display_interface()


def display_set_menu():
    print("=======\nSET MENU\n========")
    load_menu_dishes()
    change_menu = input("Are you sure you want to change the menu?")
    if change_menu.lower() == "yes" or change_menu.lower() == "y":
        load_dishes()
        continue_input = True
        while continue_input:
            id_input = input("Input the three-letter ID of the food item\nyou want to add to the menu: ")
            if id_input in items.menu_idea:
                name, price = items.menu_idea[id_input]
                setmenu.add_menu_dish(name, price)
            add_more = input("Do you want to add more? ")
            if add_more.lower() != "yes" or add_more.lower() != "y":
                continue_input = False
        save_menu()
        print("Menu saved!")
    display_interface()


if __name__ == "__main__":
    try:
        display_interface()

    except Exception as e:
        print(e)
