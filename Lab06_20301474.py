#   ____ ____  _____ ____  ____   ___  
#  / ___/ ___|| ____|___ \|___ \ / _ \ 
# | |   \___ \|  _|   __) | __) | | | |
# | |___ ___) | |___ / __/ / __/| |_| |
#  \____|____/|_____|_____|_____|\___/ 
#                                      
# 
#  _      _   ___      __   __ 
# | |    /_\ | _ )___ /  \ / / 
# | |__ / _ \| _ \___| () / _ \
# |____/_/ \_\___/    \__/\___/
                              
                              
                             
                             
                            




# Submitted by,
##  Jawad Ibn Mamoon
##  ID: 20301474
##  Section 02




#=================================================================#
#						               #
# *********************** Search and Sort *********************** #
#						               #
#=================================================================#


##########
# TASK_1 #
##########


def selection_sort(a, i=0, max_idx=0):
    l = len(a)
    l -= i
    i += 1
    if l == 1:
        return a
    else:
        max_n = a[max_idx]
        for item in range(l):
            if a[item] >= max_n:
                max_n = a[item]
                max_idx = item
        a[max_idx] = a[l-1]
        a[l-1] = max_n
        return selection_sort(a, i, max_idx)


##########
# TASK_2 #
##########


def insertion_sort(a, i=0):
    l = len(a)-1
    if i == l:
        return a
    else:
        j-1 = i + 1
        temp = a[j]
        while j >= 0 and temp <= a[j - 1]:
            a[j] = a[j - 1]
            a[j - 1] = temp
            j -= 1
        return insertion_sort(a, i + 1)



####################
# Linked List Code #
####################


class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data


class MyList:
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
            for i in range(1, counter):
                n = Node(a[i])
                self.tail.next = n
                self.tail = n
                self.size += 1

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


##########
# TASK_3 #
##########


def bubble_sort_linked(linked, size="null"):
    temp = linked.head
    if size == "null":
        l = 0
        while temp is not None:
            l += 1
            temp = temp.next
        size = l
    temp = linked.head
    for i in range(size):
        stemp = linked.head
        for j in range(size-1):
            if stemp.data >= stemp.next.data:
                temper = stemp.data
                stemp.data = stemp.next.data
                stemp.next.data = temper
            stemp = stemp.next
        temp = temp.next


##########
# TASK_4 #
##########


def selection_sort_linked(linked, size="null", tail="null"):
    temp = linked.head
    if size == "null" and tail == "null":
        tail = None
        l = 0
        while temp is not None:
            l += 1
            if temp.next is None:
                tail = temp
            temp = temp.next
        size = l
    if size == 1:
        return linked
    else:
        temp = linked.head
        max_node = tail
        for i in range(size):
            if temp.data>=max_node.data:
                max_node = temp
            temp = temp.next
        temp_data = tail.data
        tail.data = max_node.data
        max_node.data = temp_data
        size -= 1
        temp = linked.head
        for i in range(size):
            if i == size-1:
                tail = temp
            temp = temp.next
        return selection_sort_linked(linked, size, tail)



###########################
# Doubly Linked List Code #
###########################


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyList:
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


##########
# TASK_5 #
##########


def insertion_doubly(linked):
    i = linked.head
    while i is not None:
        j = i
        while j.prev is not None:
            temp = j.data
            if temp <= j.prev.data:
                j.data = j.prev.data
                j.prev.data = temp
            j = j.prev
        i = i.next


##########
# TASK_6 #
##########


def binary_search_recursive(a, item, l=None, r=None):
    if l is None and r is None:
        l = 0
        r = len(a) - 1
    n = (l + r) // 2
    if item == a[n]:
        return n
    elif item > a[n]:
        return binary_search_recursive(a, item, n + 1, r)
    elif item < a[n]:
        return binary_search_recursive(a, item, l, n - 1)


##########
# TASK_7 #
##########


fib_series = ["null"]*1000


def fib_memoization(n):
    if n == 1 or n == 0:
        return 1
    elif fib_series[n] != "null":
        return fib_series[n]
    else:
        fib_series[n] = fib_memoization(n-1) + fib_memoization(n-2)
        return fib_series[n]