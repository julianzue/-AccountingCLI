import time
from colorama import Fore, init
import os

init()

# variables
filename = "data.txt"

#colors
g = Fore.LIGHTGREEN_EX
r = Fore.LIGHTRED_EX
y = Fore.LIGHTYELLOW_EX
c = Fore.LIGHTCYAN_EX
R = Fore.RESET

class Buchhaltung():
    def __init__(self):
        x = input(">> ")
        s = x.split("  ")

        if s[0] == "add":
            self.add(s[1], s[2])

        elif s[0] == "list":
            self.listing()
        
        elif s[0] == "help":
            if len(s) > 1:
                if s[1] == "add":
                    print("add  <price>  <name>")
            else:
                print("")
                print("HELP")
                print("")
                print("add  <price>  <name>")

        elif s[0] == "change":
            self.change()

        elif s[0] == "exit" or s[0] == "q":
            print("")
            print(r + "[*] " + R + "Program closed.")
            print("")
            quit()

        else:
            print("")
            print(r + "[!] Unknown command." + R)
            print("")
            self.__init__()

    def add(self, price, name):
        file = open(filename, "a")
        file.write(time.strftime("%Y-%m-%d %H:%M") + " | todo | " + "{:6.2f}".format(float(price)) + " | " + name + "\n")
        file.close()

        print(c + "[*] " + R + "Successfully added to " + c + filename + R + ".")
        print("")
        self.__init__()

    def listing(self):
        print("")

        file = open(filename, "r")
        price = 0.0
        todo_value = 0.0

        for i, line in enumerate(file.readlines()):

            price += float(line.strip("\n").split(" | ")[2])

            if line.split(" | ")[1] == "todo":
                todo_value += float(line.strip("\n").split(" | ")[2])

            print("{:03d}".format(i + 1) + " | " + line.strip("\n"))

        print("-------------")
        print("Total: " + "{:6.2f}".format(price))
        print("Todo:  " + "{:6.2f}".format(todo_value))
        print("")
        self.__init__()

    def change(self):
        print("")

        file = open(filename, "r")

        read = file.readlines()

        for i, line in enumerate(read):
            print("{:03d}".format(i + 1) + " | " + line.strip("\n"))

        number = input(y + "[+] " + R + "Enter Number: ")
        lines = []

        for i, line in enumerate(read):
            if (i + 1) == int(number):
                split = line.split(" | ")

                if split[1] == "todo":
                    new_value = "done"
                else:
                    new_value = "todo"

                changed_line = split[0] + " | " + new_value + " | " + split[2] + " | " + split[3]

                lines.append(changed_line)

            else:
                lines.append(line)

        file.close()

        clear_file = open(filename, "w")
        clear_file.write("")
        clear_file.close()
        
        write_file = open(filename, "a")

        for line in lines:
            write_file.write(line)

        write_file.close()

        print(c + "[*] " + R + "Successfully change line " + "{:03d}".format(int(number)) + " of " + c + filename + R + ".")

        print("")
        
        self.__init__()

Buchhaltung()