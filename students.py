#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Sept 2019
# This program checks if ther is over 30 students


import constants


def main():
    # this function checks if ther is over 30 students

    # input
    number_of_students = int(input("Enter the number of students: "))
    print("")

    #process
    if number_of_students > constants.MAX_STUDENT_NUMBER:
        # output
        print("Too many students!")


if __name__ == "__main__":
    main()
