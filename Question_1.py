"""The Big O-notation for this algorithm is 0(n). Reason being that: For the first iteration, The Big-0 is 0(n),
and the second iteration the Big-0 is also 0(n) which brings it to 0(2n). Simplifying using drop constant method, " \
the Big-0 is therefore 0(n) """

"""lst = The list
n = length of the list
ele = element in the list
i = item/element in the new list"""

# This exception is raised in case you decide to take user input and the user inputted a char instead of an int or any
# other exceptions
try:

    '''Commented out for easy implementation, but can as well take a user input'''
    # lst = []
    # n = int(input("Enter number of elements : "))
    # print("Enter your list one at a time: ")

    def occurrence():
        """When taking a user input every new element is appended to the empty list created before this function
        The list is then printed"""
        # for i in range(0, n):
        #     ele = int(input())
        #     lst.append(ele)
        # print(lst)

        # Count every element in the list and check for repetitions using count then create a set(This is to be sure
        # if the algorithm to be implemented next actually works, especially for the user input) from the count
        # inbuilt function
        while len(lst) != 0:
            count_ele = {lst.count(item) for item in lst}
            print(count_ele)

            # Check if any item/element for all the items/elements in the set is divisible by 2 without any remainder
            if any([i % 2 == 0 for i in count_ele]):

                # Return false if there is any otherwise return true
                return False
            else:
                return True


    lst = [1, 3, 2, 2, 5, 2]
    # lst = [5, 2, 5, 2, 2, 3, 1]
except Exception as e:
    print(e)

if __name__ == '__main__':
    # noinspection PyUnboundLocalVariable
    print(occurrence())
