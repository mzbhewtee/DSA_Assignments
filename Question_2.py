
# This exception is raised in case you decide to take user input and the user inputted a char instead of an int or any
# other exceptions
try:

    # Initialize the list to be empty then take a user input for the list and the number to be summed
    list1 = []
    list_length = int(input("Enter number of elements : "))
    k = int(input("Enter the number of the highest numbers to be summed up: "))


    def summation():
        """Define a function that first check if the number to be summed up is less than or equal to the length list:
        if it is then continues the programme else print an information to the user and end the programme"""

        if k <= list_length:
            print("Enter your list one at a time: ")

            # Append every item inputted in the range the user want then sort the list
            for i in range(0, list_length):
                if any(list1.count(i) > 1 for i in list1):
                    print("No repeated digit, please")
                    quit()
                item = int(input("Enter a digit: "))
                list1.append(item)
                list1.sort()

                # Create a variable that stores the sum of the chosen number of highest numbers to be summed
                summed_list = sum(list1[-k:])

            # Print the list for verification
            print("Your input list: ", list1, "\nNumber of highest to be summed: ", k)

            print("The sum is: ", summed_list)

        # Exemption
        else:
            print("Input a digit less than or equal to the length of the list")

except Exception as e:
    print(e)

if __name__ == '__main__':
    summation()

"""The big 0 of this algorithm is 0n"""