# week menu: name, price
week_menu = {}


def load_menu_file(filename: str):
    """
    This will load the menu of the week into the application

    :param filename: file that contains menu of the week
    :type filename: str

    Precondition
    ------------
    The target file exists and contains values. If the file
    is empty or doesn't exist, the program will create one,
    but there will be no values loaded to the application.

    Postcondition
    -------------
    The week_menu dictionary will be filled with the dishes
    picked out for the week.
    """
    try:
        with open(filename, "r") as file:
            for line in file:
                name, price = line.rstrip().split(", ")
                add_menu_dish(name, price)
    except Exception as e:
        print(e)


def save_menu_file(filename: str):
    """
    This will save all chosen dishes for the week in a file.

    :param filename:
    :type filename: str

    Precondition
    ------------
    The target file exists. If not, the program will create one.

    Postcondition
    -------------
    The target file will contain the weekly menu
    created by the user.
    """
    try:
        with open(filename, "w") as file:
            for dish in week_menu:
                name, price = dish, week_menu[dish]
                file.writelines(f"{name}, {price}")
    except Exception as e:
        print(e)


def add_menu_dish(name: str, price: int):
    """
    This method allows the user to add a dish to the
    weekly menu

    :param name: the name of the dish
    :type name: str

    :param price: the price of the dish
    :type price: int

    Precondition
    ------------
    - The price number must be an integer
    - The dish must not have already been put in the menu

    Postcondition
    -------------
    - The dish is added to the weekly menu

    """
    if name not in week_menu:
        week_menu[name] = price


def clear_menu():
    """
    Clears the weekly menu
    """
    week_menu.clear()


def weekly_menu_to_list():
    """
    This function converts the dictionary
    into a list to be viewed by the interface
    :return: converted list of the weekly menu
    """
    return [(name, price) for name, price in week_menu.items()]


if __name__ == "__main__":
    try:
        week_menu = {"Test1": 12, "Test2": 10, "Test3": 8}
        save_menu_file("weeklymenu.txt")
        load_menu_file("weeklymenu.txt")
        week_test_menu = weekly_menu_to_list()
        print(week_test_menu)
    except Exception as e:
        print(e)
