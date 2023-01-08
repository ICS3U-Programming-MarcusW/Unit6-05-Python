#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: December 18 2022
# This program gets marks from the user and
# then calculates and displays the averages of the all
# the marks the user entered


# This function returns the average of the marks
def calc_average(list_of_marks):
    # Initializes the sum variable to 0
    sum = 0

    # Iterates through the list
    for counter in range(len(list_of_marks)):
        # Adds each mark to the sum for division
        sum += list_of_marks[counter]

    # Formula to calculate  average
    average = sum / len(list_of_marks)

    # Returns the average
    return average


# Function to get the users marks and display the average of all
# the marks
def main():
    # Explain the programs purpose
    print("This program calculates the average of all the marks entered.")
    # Set empty list to hold all marks
    all_marks = []
    # Set the users mark
    each_mark = 0

    # Try catch to catch erroneous input
    try:
        # Keep asking the user for marks until they input -1
        while each_mark != -1:
            # Get a mark from the user as a float
            each_mark = float(input("Enter a mark (input -1 to stop): "))

            # Make sure the user did not enter -1, if they did
            # leave the loop
            if each_mark == -1:
                break

            # Make sure the user did not entered a mark outside the range
            elif each_mark < -1 or each_mark > 100:
                print("Invalid mark!")
            else:
                # Add the mark to the list of marks
                all_marks.append(each_mark)

    # If there is an error, tell the user
    except Exception:
        print("You did not enter a valid mark!")
    else:
        # If the list is empty - user did not enter any marks:
        if all_marks == []:
            print("You did not enter any marks!")
        else:
            # Calls the function to calculate the average of all marks
            marks_average = calc_average(all_marks)
            # Displays the list of marks
            print(f"The list of marks is {all_marks}")
            # Displays the average of all marks
            print(f"The average is {marks_average}%")


if __name__ == "__main__":
    main()
