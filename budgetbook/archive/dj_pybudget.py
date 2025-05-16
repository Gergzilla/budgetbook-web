#!/usr/bin/python
# This file is a copy of pybudget.py but is being modified for django integration and testing
import utilities.handlers as handlers
import utilities.db_handlers as db_handlers
import os


main_menu = {
    "1": "View current expense summary",
    "2": "Modify category tags",
    "3": "Import new expense",
    "4": "Setup budget table",
    "0": "Exit"
}
def addTags():
    tag_choice = 9999
    listByMonth = handlers.monthlyQueryBuilder()
    handlers.displayPrettyExpenses(listByMonth)
    # prompt user for the entry they wish to modify
    while -1 > tag_choice or len(listByMonth) < tag_choice:
        try:
            tag_choice = int(input("Choose an entry number to add a tag to (this overwrites existing tags as well): "))
        except ValueError:
            print("Selection not in list or was not a number, try again")
    tag = input("You chose: " + str(listByMonth[tag_choice-1]).strip("()").replace("'","") + "\nEnter a tag for this charge: ")
    chosenRecord = listByMonth[tag_choice-1]
    tag = tag.upper()
    result = db_handlers.addTag(chosenRecord, tag)
    print(result)

def fileImport():
    inputfile = os.path.join("statements", "sample_data.csv") #full path doesnt work because you need absolute path, use os.path.dirname(__file__)
    handlers.csvImporter(inputfile)
    
def viewAllRecords():
    fullSummary = db_handlers.queryByYearlyTable()
    # print("Raw result is: ", fullSummary )
    # note for learning, parsing a tuple you just assign a var to each entry in the tuple and do what you want with it
    # you must account for all values in the tuple even if you dont use them
    # I am sure there is a dynamic way to do this but using a set table there is no reason it would change
    i = 1
    for charge_date, entity, expense, tag, notes in fullSummary:
        print(i, charge_date, entity, expense, tag, notes) 
        i = i + 1
    # print(fullSummary)

def main():
    mainMenu()

def parseUserChoice(menuContext, user_choice):
    # Currently only handles main menu, might be necessary to make new library for menu navigation
    if menuContext == "mainMenu" and user_choice == 1:
        viewAllRecords()
        #print("View expense summary-NYI")
    if menuContext == "mainMenu" and user_choice == 2:
        print("Calling addTags")
        addTags()
    if menuContext == "mainMenu" and user_choice == 3:
        fileImport()
    if menuContext == "mainMenu" and user_choice == 4:
        #db_handlers.createBudgetTable()
        print("disabled for Django integration")
    if menuContext == "mainMenu" and user_choice == 0:
        print("Exiting...")
        exit()

def mainMenu():
    user_selection = 99
    # os.system('cls' if os.name == 'nt' else 'clear') disabled for debug for now
    print("Welcome to my budget, choose an action below")
    for key, value in main_menu.items():
        print(key, value)
    while -1 > user_selection or len(main_menu.keys()) < user_selection:
        try:
            user_selection = int(input("Choose an option from the list: "))
        except ValueError:
            print("You must enter a valid choice from above")
    parseUserChoice("mainMenu", user_selection)

if __name__ == "__main__":
    main()