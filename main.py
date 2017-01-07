import os
import glob

print("========= Welcome to my database, ver 1.0 =========")

current_table = ""


def create_table():
    print("==================== New table ====================")
    try:
        table_name = input("Enter table name: ")
        open(table_name + ".txt", "x")
        global current_table
        current_table = table_name
        print("New table successfully created!")
    except FileExistsError:
        print("Table already exists!")


def set_columns():
    print("================== Set column(s) ==================")
    print("Enter column names, separated by semicolon")
    print("For example: one;two;three")
    columns = input("Enter column names: ")
    print("You have entered: ")
    for name in columns.split(";"):
        print(name)
    table = open(current_table + ".txt", "w")
    table.write(columns)


def add_record():
    table = open(current_table + ".txt", "r")
    columns = table.readline().split(";")
    table.close()
    table = open(current_table + ".txt", "a")
    record = ""
    for column in columns:
        element = input(column.rstrip('\n') + ": ")
        record += element
        record += ";"
    table.write("\n" + record.rstrip(';'))
    table.close()


def select_table():
    print("================== Select table ===================")
    tables = glob.glob("*.txt")
    for table in tables:
        print(table.rstrip(".txt"))
    selected = input("Select table: ")
    if selected + ".txt" in tables:
        global current_table
        current_table = selected
        print("Table \"" + current_table + "\" have been selected")
    else:
        print("No such table!")


def show_table():
    print((" " + current_table + " ").center(75, "="))
    table = open(current_table + ".txt", "r")
    for line in table.readlines():
        elements = line.split(";")
        output = ""
        for element in elements:
            output += element.rstrip("\n").ljust(25)
        print(output)
    print("=" * 75)


def search():
    key = input("Search for: ")
    table = open(current_table + ".txt", "r")
    header = table.readline()
    elements = header.split(";")
    output = ""
    for element in elements:
        output += element.rstrip("\n").ljust(25)
    print((" " + current_table + " ").center(75, "="))
    print(output)
    for line in table.readlines():
        if key in line:
            elements = line.split(";")
            output = ""
            for element in elements:
                output += element.rstrip("\n").ljust(25)
            print(output)
    print("=" * 75)


while True:
    print("Choose option:")
    print("1. Create new table")
    print("2. Set column(s) in current table")
    print("3. Add record to table")
    print("4. Select table")
    print("5. Show table")
    print("6. Search in table")
    print("0. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_table()
    elif choice == 2:
        if current_table != "":
            set_columns()
        else:
            print("No selected table!")
    elif choice == 3:
        if current_table != "":
            if os.stat(current_table + ".txt").st_size != 0:
                add_record()
            else:
                print("There is no columns in table!")
        else:
            print("No selected table!")
    elif choice == 4:
        select_table()
    elif choice == 5:
        if current_table == "":
            print("No selected table!")
        elif os.stat(current_table + ".txt").st_size != 0:
            show_table()
        else:
            print("Table is empty!")
    elif choice == 6:
        if current_table == "":
            print("No selected table!")
        elif os.stat(current_table + ".txt").st_size != 0:
            search()
        else:
            print("Table is empty!")
    elif choice == 0:
        print("Goodbye!")
        break
    else:
        print("Incorrect value!")
