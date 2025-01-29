import sys

#how to reverse a fullname in formatting

def main11():
    first_name = input("Write the first name: ")
    last_name = input("Write the last name: ")
    print("Welcome " + last_name + ", " + first_name)
    print("Welcome {0}, {1}".format(last_name, first_name))



main11()

