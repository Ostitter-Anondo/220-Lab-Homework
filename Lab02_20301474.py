#   ____ ____  _____ ____  ____   ___  
#  / ___/ ___|| ____|___ \|___ \ / _ \ 
# | |   \___ \|  _|   __) | __) | | | |
# | |___ ___) | |___ / __/ / __/| |_| |
#  \____|____/|_____|_____|_____|\___/ 
#                                      
#  _      _   ___      __ ___ 
# | |    /_\ | _ )___ /  \_  )
# | |__ / _ \| _ \___| () / / 
# |____/_/ \_\___/    \__/___|
                             
                            




# Submitted by,
##  Jawad Ibn Mamoon
##  ID: 20301474
##  Section 02




#==============================================================#
#							    #
# *********************** Linked Lists *********************** #
#							    #
#==============================================================#


##########
# TASK_1 #
##########


class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data


class MyList:

    ##########
    # TASK_2 #
    ##########

    # Problem_1
    def __init__(self, a):
        counter = 0
        for i in a:
            counter += 1
        if counter == 0:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head = Node(a[0])
            self.tail = self.head
            self.size = 1
            for i in range(1, counter-1):
                n = Node(a[i])
                self.tail.next = n
                self.tail = n
                self.size += 1

    # Problem_2
    def showList(self):
        if self.size == 0:
            return "Empty List"
        else:
            data = ""
            item = self.head
            while item is not None:
                if item.next is not None:
                    data += str(item.data) + " " + "->" + " "
                else:
                    data += str(item.data)
                item = item.next
            return data

    # Problem_3
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    # Problem_4
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Problem_5
    def insert(self, newElement):
        if self.size == 0:
            self.head = newElement
            self.tail = newElement
            self.size += 1
        else:
            condition = False
            temp = self.head
            while temp is not None:
                if temp.data == newElement:
                    condition = True
                    break
            if condition is True:
                print("New Element Already Exists In The List")
            else:
                n = Node(newElement)
                self.tail.next = n
                self.tail = n
                self.size += 1

    # Problem_6
    def insertAt(self, newElement, index):
        if index < 0 or index > self.size:
            print("Index Invalid")
        elif self.size == 0:
            self.head = newElement
            self.tail = newElement
            self.size += 1
        else:
            condition = False
            temp = self.head
            while temp is not None:
                if temp.data == newElement:
                    condition = True
                    break
            if condition is True:
                print("New Element Already Exists In The List")
            else:
                n = Node(newElement)
                if index == 0:
                    n.next = self.head
                    self.head = n
                elif index == self.size:
                    self.tail.next = n
                    self.tail = n
                else:
                    pred = None
                    fwd = self.head
                    for i in range(index):
                        pred = fwd
                        fwd = fwd.next
                    n.next = fwd
                    pred.next = n
                    self.size += 1

    # Problem_7
    def remove(self, deletekey):
        if self.size == 0:
            return "Nothing to remove."
        else:
            if deletekey < 0 or deletekey > self.size:
                print("Invalid index")
            elif deletekey == 0:
                data = self.head.data
                self.head = self.head.next
                self.size -= 1
                return data
            elif deletekey == self.size-1:
                temp = self.head
                data = self.tail.data
                while temp.next is not None:
                    temp = temp.next
                self.tail = temp
                self.size -= 1
                return data
            else:
                pred = self.head
                fwd = self.head
                for i in range(deletekey-1):
                    pred = pred.next
                for i in range(deletekey):
                    fwd = fwd.next
                data = fwd.data
                pred.next = fwd.next
                self.size -= 1
                return data

    # EXTRA
    def get_node(self, index):
        if index < 0 or index > self.size:
            print("Wrong Index Value")
        else:
            value = self.head
            for i in range(index):
                value = value.next
            return value


##########
# TASK_3 #
##########

# Problem_1
def evenFinder(l_list):
    temp = l_list.head
    to_print = []
    while temp is not None:
        if temp.data%2 == 0:
            to_print += [temp.data]
    final = MyList(to_print)
    return final.showList()


# Problem_2
def elementFinder(l_list, element):
    temp = l_list.head
    condition = False
    while temp is not None:
        if temp.data == element:
            condition = True
            break
    return condition


# Problem_3
def reverse_linked(l_list):
    size = l_list.size
    for i in range(int(size//2)):
        if i == 0:
            swapa = l_list.head
            swapb = l_list.tail
            tempa = l_list.get_node(1)
            tempb = l_list.get_node(size-2)
            tempb.next = swapa
            swapb.next = tempa
            l_list.head = swapb
            l_list.tail = swapa
        elif size%2 == 0 and i == int((size//2)-1):
            swapa = l_list.get_node(i)
            swapb = l_list.get_node(size - i - 1)
            tempa = l_list.get_node(i - 1)
            tempa.next = swapb
            swapa.next = swapa.next.next
            swapb.next = swapa
        else:
            swapa = l_list.get_node(i)
            swapb = l_list.get_node(size-i-1)
            tempa = l_list.get_node(i-1)
            tempb = l_list.get_node(size-i)
            swapb.next = tempa.next.next
            swapa.next = tempb.next.next
            tempb.next = swapa
            tempa.next = swapb


# Problem_4
def sort_ascend(lis):
    while True:
        temp = lis.head
        condition = False
        for i in range(lis.size-2):
            a = temp
            b = temp.next
            if a > b:
                condition = True
                if a == lis.head:
                    a.next = b.next
                    b.next = a
                    lis.head = b
                elif b == lis.tail:
                    c = lis.get_node(i-1)
                    c.next = b
                    b.next = a
                    a.next = None
                    lis.tail = a
                else:
                    c = lis.get_node(i-1)
                    c.next = b
                    a.next = b.next
                    b.next = a
                break
        if condition is False:
            break
    return lis


# Problem_5
def sumElements(l_list):
    temp = l_list.head
    total = 0
    while temp is not None:
        total += temp.data
    return total


# Problem_6
def rotate(lis, dir, n):
    if dir == "left":
        for i in range(n):
            newtail = lis.head
            lis.head = lis.head.next
            lis.tail.next = newtail
            lis.tail = newtail
            lis.tail.next = None
    elif dir == "right":
        for i in range(n):
            newtail = lis.get_node(lis.size-2)
            lis.tail.next = lis.head
            lis.head = lis.tail
            lis.tail = newtail
            lis.tail.next = None
    return lis


#==============================================================


