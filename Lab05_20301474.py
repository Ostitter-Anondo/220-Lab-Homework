#   ____ ____  _____ ____  ____   ___  
#  / ___/ ___|| ____|___ \|___ \ / _ \ 
# | |   \___ \|  _|   __) | __) | | | |
# | |___ ___) | |___ / __/ / __/| |_| |
#  \____|____/|_____|_____|_____|\___/ 
#                                      
#  _      _   ___      __  ___ 
# | |    /_\ | _ )___ /  \| __|
# | |__ / _ \| _ \___| () |__ \
# |____/_/ \_\___/    \__/|___/
                              
                             
                             
                            




# Submitted by,
##  Jawad Ibn Mamoon
##  ID: 20301474
##  Section 02




#===========================================================#
#						         #
# *********************** Recursion *********************** #
#						         #
#===========================================================#


##########
# TASK_1 #
##########


# Problem_a


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


# Problem_b


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


# Problem_c


def print_array(a, size):
    if size == 0:
        return ""
    else:
        n = str(a[size-1])
        size -= 1
        return print_array(a, size)+n+"\n"


# Problem_d


def powerN(n, p):
    if p == 0:
        return 1
    elif p > 0:
        return n*powerN(n, p-1)
    elif p < 0:
        return (1/n)*powerN(n, p+1)


#==============================================================



##########
# TASK_2 #
##########


# Problem_a


def dec_to_bin(n):
    if n == 0:
        return ""
    else:
        m = str(n%2)
        n = int(n//2)
        return dec_to_bin(n)+m


# Problem_b


def linked_sum(head):
    if head is None:
        return 0
    else:
        temp = head.data
        head = head.next
        return temp+linked_sum(head)


# Problem_c


def print_linked(a):
    if a is None:
        return ""
    else:
        m = str(a.data)
        a = a.next
        return m+"\n"+print_linked(a)


#==============================================================



##########
# TASK_3 #
##########


def hoc_builder(n):
    if n == 1:
        return 8
    else:
        return 5+hoc_builder(n-1)


#==============================================================



##########
# TASK_4 #
##########


# Problem_a


def pattern_a(n):
    if n == 0:
        return ""
    else:
        tex = ""
        for i in range(n):
            tex += str(i+1)+" "
        n -= 1
        return pattern_a(n)+tex+"\n"


# Problem_b


def pattern_a(n, m=0):  # as the question did not specifically forbid me from using a second value,
    if n == 0:          # I used a second value at my own discretion
        return ""       # and based its use on what I learned in the past
    else:
        tex = ""
        for i in range(n):
            tex += str(i + 1) + " "
        n -= 1
        tex = 2 * m * " " + tex + "\n"
        m += 1
        return pattern_a(n, m) + tex


#==============================================================



##########
# TASK_5 #
##########


import sys

sys.setrecursionlimit(5000)


class FinalQ:
    def calcProfit(self, investment):
        if investment == 25000:
            return 0
        elif investment <= 100000:
            investment -= 100
            return 4.5+self.calcProfit(investment)
        else:
            investment -= 100
            return 8+self.calcProfit(investment)

    def print(self, array, idx=0):
        if idx < len(array):
            profit = self.calcProfit(array[idx])
            tex = str(idx+1) + ". Investment: " + str(array[idx]) + "; Profit: " + str(profit) + "\n"
            idx += 1
            return tex + self.print(array, idx)
        else:
            return ""
#==============================================================


