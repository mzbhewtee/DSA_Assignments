# Create an empty list that will hold the items
list1 = []
# create a list for the deleted items
delete_list = []
# create a list that wil hold the current items
current_list = []
# create a list that hold the added items
added = []
# first in last out list
redo_list = []



# create a class for the node

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# undoablelist class for the operation
class UndoableList:
    def __init__(self):
        self.head = node()

    # Create an insert function that will be appended to list1 and current_list
    def insert(self, data):
        # Create a new node
        new_node = node(data)
        current = self.head
        # Check if list is empty
        while current != None and current.next is not None:
            current = current.next
        current.next = new_node
        # append the new item to the list created above
        current_list.append(new_node.data)
        list1.append(new_node.data)
        added.append(new_node.data)
        print(sorted(current_list))

    # function for deleting node
    def delete(self, data):
        list1.append("delete")

        # Check if list is empty
        if self.head is None:
            # nothing is deleted and the program ends
            return 1
        current = self.head
        # Handle exception in case everything has been deleted and there is nothing left to delete
        try:
            while True:
                last_node = current
                current = current.next

                # make the current node the head or the one before the next node
                if current.data == data:
                    last_node.next = current.next
                    delete_list.append(data)
                    current_list.remove(data)
                    print(sorted(current_list))
                    return

        except AttributeError:
            list1.remove("delete")
            return

    # create a function for the undo
    def undo(self):
        # Checks if list is empty
        if self.head is None:
            # if it is return 1
            return 1
        # store the number of times the undo function has been called and save it
        count = list1.count("undo")
        # the new length of the list will be the old length - the number of time the undo has been called
        length = len(list1) - count

        # Check for the last function called
        if list1[length - 1] == "delete":
            list1.pop(-1)
            redo_list.append("delete")
            for i in delete_list:
                self.insert(i)
                list1.pop(-1)
                list1.append("undo")

        # confirm if the recalled list is actually added to the list
        if list1[length - 1] == "insert":
            if len(added) != len(current_list):
                added.pop(-1)
                redo_list.append("insert")
            for i in sorted(current_list):
                if added[-1] == i:
                    self.delete(i)
                    list1.pop(-1)
                    list1.append("undo")

    # The redo method undoes the undo function
    def redo(self):
        # Checks if the list is empty
        if self.head is None:
            return
        list1.append("redo")
        x = list1.count("redo")
        l = []
        for i in range(x):
            y = redo_list[-1]
            l.append(y)
        if l[-1] == "insert":
            current_list.append(added[-1])
            print(set(current_list))
        if l[-1] == "delete":
            for elem in delete_list:
                sorted(current_list).remove(elem)
                print(set(current_list))



my_list = UndoableList()

my_list.insert(2)
my_list.insert(5)
my_list.insert(7)
my_list.insert(6)
my_list.delete(5)
my_list.undo()
my_list.redo()
my_list.insert(4)
my_list.redo()
my_list.delete(3)
my_list.undo()
my_list.undo()
my_list.redo()
my_list.redo()
