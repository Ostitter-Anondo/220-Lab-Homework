#   ____ ____  _____ ____  ____   ___  
#  / ___/ ___|| ____|___ \|___ \ / _ \ 
# | |   \___ \|  _|   __) | __) | | | |
# | |___ ___) | |___ / __/ / __/| |_| |
#  \____|____/|_____|_____|_____|\___/ 
#                                      
#  _      _   ___      __  _ _  
# | |    /_\ | _ )___ /  \| | | 
# | |__ / _ \| _ \___| () |_  _|
# |____/_/ \_\___/    \__/  |_| 
                               
                             
                             
                            




# Submitted by,
##  Jawad Ibn Mamoon
##  ID: 20301474
##  Section 02




#===============================================================================#
#							                     #
# *********************** Stack - Parenthesis Balancing *********************** #
#							                     #
#===============================================================================#


##########
# TASK_1 #
##########


class StackArray:
    def __init__(self):
        self.top = -1
        self.size = 0
        self.stack = []

    def push(self, item):
        self.stack += [item]
        self.top += 1
        self.size += 1

    def pop(self):
        if self.size > 0:
            data = self.stack[self.top]
            self.stack = self.stack[:(self.size-1)]
            self.top -= 1
            self.size -= 1
            return data
        else:
            return "Nothing to pop"

    def peek(self):
        if self.size > 0:
            return self.stack[self.top]
        else:
            return "Nothing to see"



def ParenthesisBalanceArray(string):
    par = StackArray()
    start = "[{("
    end = "]})"
    counter = 0
    j = "null"
    ind = []
    m = -1
    empty = "nay"
    b = "null"
    for i in string:
        counter += 1
        if i in start:
            par.push(i)
            ind += [counter]
            m += 1
        elif i in end:
            if i == "]":
                j = "["
            elif i == "}":
                j = "{"
            elif i == ")":
                j = "("
            if j == par.peek():
                par.pop()
                ind = ind[:m]
                m -= 1
            else:
                if par.size == 0:
                    empty = "aye"
                    j = i
                    b = str(counter)
                else:
                    empty = "nay"
                break
    if par.size != 0:
        n = par.peek()
        k = str(ind[m])
        return string + "\nThis expression is NOT correct.\nError at character # " + k + ". ‘" + n + "‘- not closed."
    else:
        if empty == "aye":
            n = j
            k = b
            return string + "\nThis expression is NOT correct.\nError at character # " + k + ". ‘" + n + "‘- not opened."
        else:
            return string+"\nThis expression is correct."


#==============================================================



##########
# TASK_2 #
##########

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class StackLinked:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        n = Node(item)
        n.next = self.top
        self.top = n
        self.size += 1

    def pop(self):
        if self.size > 0:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data
        else:
            return "Nothing to pop"

    def peek(self):
        if self.size > 0:
            return self.top.data
        else:
            return "Nothing to see"



def ParenthesisBalanceLinked(string):
    par = StackLinked()
    start = "[{("
    end = "]})"
    counter = 0
    j = "null"
    ind = []
    m = -1
    empty = "nay"
    b = "null"
    for i in string:
        counter += 1
        if i in start:
            par.push(i)
            ind += [counter]
            m += 1
        elif i in end:
            if i == "]":
                j = "["
            elif i == "}":
                j = "{"
            elif i == ")":
                j = "("
            if j == par.peek():
                par.pop()
                ind = ind[:m]
                m -= 1
            else:
                if par.size == 0:
                    empty = "aye"
                    j = i
                    b = str(counter)
                else:
                    empty = "nay"
                break
    if par.size != 0:
        n = par.peek()
        k = str(ind[m])
        return string + "\nThis expression is NOT correct.\nError at character # " + k + ". ‘" + n + "‘- not closed."
    else:
        if empty == "aye":
            n = j
            k = b
            return string + "\nThis expression is NOT correct.\nError at character # " + k + ". ‘" + n + "‘- not opened."
        else:
            return string + "\nThis expression is correct."


#==============================================================


