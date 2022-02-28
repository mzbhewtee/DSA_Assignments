"""The big 0 of this algorithm is 0n2"""
def knapsack(v, w, capacity):
    """This is the dynamic programming method. This method is best in solving the problem. First an empty dictionary is
    set to store the chosen pellet"""
    chosen_pellet = {}

    # check for each item capacity in the capacity (in an increasing order until you get the maximum capacity)
    for c in range(capacity + 1):

        # if the item chosen is zero the profit will be zero
        chosen_pellet[(0, c)] = 0

    # check the value of each pellet as the selection occur
    for i in range(1, (len(value) + 1)):

        # check if the item is not more than the capacity as the loop runs
        for j in range(capacity + 1):

            # if the weight of the previous pellet is less than or equal to the capacity
            if weight[i - 1] <= j:

                # formular for calculating the profit to be made from each selection. Take the max value from the
                # previous pellet or the value of the previous pellet + the previous pellet -
                # the weight of the previous pellet
                chosen_pellet[(i, j)] = max(chosen_pellet[(i - 1, j)],

                                            value[i - 1] + chosen_pellet[(i - 1, j - weight[i - 1])])
            #     if the item weight and the capacity is equal to the previous pellet weight and capacity,
            #     the previous pellet will be chosen
            else:
                chosen_pellet[(i, j)] = chosen_pellet[(i - 1, j)]

    # Check for the pellet chosen
    for i in range(len(value), 0, -1):
        #
        if chosen_pellet[(i, j)] != chosen_pellet[(i - 1, j)]:
            print(name[i - 1], "=>", weight[i - 1], "kg which has the profit of", "$", value[i - 1])
            j -= weight[i - 1]
    return "Profit Incurred",f"${chosen_pellet[(len(value), capacity)]}"


name = ["Gold_1", "Gold_2", "Gold_3", "Gold_4", "Gold_5", "Gold_6", "Gold_7", "Gold_8", ]
value = [2500, 1700, 1200, 3000, 4100, 2000, 7000, 7500]
weight = [5, 3, 1, 6, 8, 4, 11, 12]
Capacity = 20

print(knapsack(value, weight, Capacity))
