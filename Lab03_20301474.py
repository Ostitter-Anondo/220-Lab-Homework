#   ____ ____  _____ ____  ____   ___  
#  / ___/ ___|| ____|___ \|___ \ / _ \ 
# | |   \___ \|  _|   __) | __) | | | |
# | |___ ___) | |___ / __/ / __/| |_| |
#  \____|____/|_____|_____|_____|\___/ 
#                                      
#  _      _   ___      __ ____
# | |    /_\ | _ )___ /  \__ /
# | |__ / _ \| _ \___| () |_ \
# |____/_/ \_\___/    \__/___/
                             
                             
                            




# Submitted by,
##  Jawad Ibn Mamoon
##  ID: 20301474
##  Section 02




#===========================================================================================#
#							                                 #
# *********************** Dummy Headed Circular Doubly Linked Lists *********************** #
#							                                 #
#===========================================================================================#


##########
# TASK_1 #
##########


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyList:
    head = None

    ##########
    # TASK_2 #
    ##########
    
    # Problem_1
    def __init__(self, a):
        counter = 0
        for i in a:
            counter += 1
        self.head = Node(a[0])
        self.tail = self.head
        self.size = 0
        if counter == 0:
            self.tail = self.head
            self.head.next = self.tail
            self.tail.prev = self.tail
            print("Array empty.")
        else:
            temp = self.head
            for i in range(1, counter):
                temp.next = Node(a[i], None, temp)
                temp = temp.next
                self.tail = temp
                self.size += 1


    # Problem_2
    def showList(self):
        if self.size == 0:
            print("Empty List")
        else:
            out = ""
            temp = self.head
            while temp is not None:
                if temp.next is None:
                    out += str(temp.data)
                else:
                    out += str(temp.data) + "<=>"
                temp = temp.next
            return out

    
    # Problem_3
    def insert(self, newElement):
        condition = False
        temp = self.head.next
        while temp != self.head:
            if temp.data == newElement:
                condition = True
                break
        if condition is True:
            print("New Element Already Exists In The List")
        else:
            n = Node(newElement)
            n.prev = self.tail
            n.next = self.head
            self.tail.next = n
            self.head.prev = n
            self.tail = n
            self.size += 1

# Please note that the original question does not specify anything about how to deal with 2 methods having the same name
    # and the faculties have left previous queries regarding the matter unanswered, therefore I have taken the liberty
    # to resolve the issue on my own accord.
    
    # Extra
    def get_node(self, index):
        if index < 0 or index > self.size:
            print("Wrong Index Value")
        else:
            value = self.head.next
            for i in range(index):
                value = value.next
            return value

    # Problem_4
    def insertAt(self, newElement, index):
        if index < 0 or index > self.size:
            print("Index Invalid")
        else:
            condition = False
            temp = self.head.next
            while temp != self.head:
                if temp.data == newElement:
                    condition = True
                    break
            if condition is True:
                print("New Element Already Exists In The List")
            else:
                n = Node(newElement)
                b = self.get_node(index)
                a = b.prev
                n.next = b
                n.prev = a
                a.next = n
                b.prev = n
                if index == self.size:
                    self.tail = n
                self.size += 1

    # Problem_5
    def remove(self, index):
        if self.size == 0:
            print("Nothing to remove.")
        else:
            if index < 0 or index > self.size:
                print("Index Invalid")
            n = self.get_node(index)
            data = n.data
            a = n.prev
            b = n.next
            a.next = b
            b.prev = a
            if index == self.size-1:
                self.tail = a
            self.size -= 1
            print(data)

    # Problem_6
    def removeKey(self, deleteKey):
        if self.size == 0:
            print("Nothing to remove.")
        else:
            condition = False
            temp = self.head.next
            while temp != self.head:
                if temp.data == deleteKey:
                    condition = True
                    break
                temp = temp.next
            if condition is True:
                data = temp.data
                a = temp.prev
                b = temp.next
                a.next = b
                b.prev = a
                if self.tail == temp:
                    self.tail = a
                self.size -= 1
                print(data)
            else:
                print("Nothing to remove.")



#==============================================================


