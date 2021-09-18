#   ____ ____  _____ ____  ____   ___  
#  / ___/ ___|| ____|___ \|___ \ / _ \ 
# | |   \___ \|  _|   __) | __) | | | |
# | |___ ___) | |___ / __/ / __/| |_| |
#  \____|____/|_____|_____|_____|\___/ 
#                                      
#  _      _   ___      __  _ 
# | |    /_\ | _ )___ /  \/ |
# | |__ / _ \| _ \___| () | |
# |____/_/ \_\___/    \__/|_|
                            




# Submitted by,
##  Jawad Ibn Mamoon
##  ID: 20301474
##  Section 02




# _____________________________________________________________
#
# *********************** Linear Arrays ***********************
# _____________________________________________________________



#############
# PROBLEM_1 #
#############

def shiftLeft(s, k):
    for i in range(len(s)):
        if i+k >= len(s):
            s[i] = 0
        else:
            s[i] = s[i+k]
    print(s)


#==============================================================


#############
# PROBLEM_2 #
#############

def rotateLeft(s, k):
    d = [0]*len(s)
    for i in range(len(s)):
        d[i-k] = s[i]
    s = d
    print(s)


#==============================================================


#############
# PROBLEM_3 #
#############

def remove(array, size, idx):
    i = idx
    while i < size:
        if i < (size - 1):
            array[i] = array[i+1]
        else:
            array[i] = 0
        i += 1
    print(array)


#==============================================================


#############
# PROBLEM_4 #
#############

def removeAll(array, size, element):
    while True:
        i = 0
        condition = 0
        while i < size-1:
            if array[i] == element:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
            i += 1
        for i in range(size-1):
            if array[i] == element and array[i] != array[i+1]:
                condition = 1
        if condition == 0:
            break
    for item in range(size):
        if array[item] == element:
            array[item] = 0
    print(array)


#==============================================================


#############
# PROBLEM_5 #
#############

def arraySplit(array):
    condition = "false"
    for i in range(len(array)-1):
        sum1 = 0
        for j in range(i+1):
            sum1 += array[j]
        k = len(array)-1
        sum2 = 0
        while k >= (i+1):
            sum2 += array[k]
            k -= 1
        if sum1 == sum2:
            condition = "true"
            break
    print(condition)


#==============================================================


#############
# PROBLEM_6 #
#############

def seriesN(n):
    array = []
    x2 = n
    while x2 > 0:
        x1 = 1
        i = n
        while x1 <= n:
            if x1 >= x2:
                array += [i]
            else:
                array += [0]
            i -= 1
            x1 += 1
        x2 -= 1
    print(array)


#==============================================================


#############
# PROBLEM_7 #
#############

def bunchCounter(array):
    bunch = 0
    counter = 1
    for i in range(len(array)-1):
        if array[i+1] == array[i]:
            counter += 1
            if bunch < counter:
                bunch = counter
        elif array[i+1] != array[i]:
            if bunch < counter:
                bunch = counter
            counter = 1
    print(bunch)


#==============================================================


#############
# PROBLEM_8 #
#############

def repitionReturner(array):
    dic = {}
    condition = "False"
    for i in array:
        if i not in dic:
            dic[i] = 0
    for i in array:
        dic[i] += 1
    for i in dic:
        for j in dic:
            if i != j:
                if dic[i] == dic[j] > 1:
                    condition = "True"
    print(condition)


#==============================================================




# _____________________________________________________________
#
# ********************** Circular Arrays **********************
# _____________________________________________________________



#############
# PROBLEM_1 #
#############

def circlePalindrome(array, start, size):
    checker = []
    n = start
    s = size-1
    while n-start < int(size//2+1):
        if array[n%len(array)] == array[(n+s)%len(array)]:
            checker.append("yes")
        else:
            checker.append("no")
        n += 1
        s -= 2
    if "no" in checker:
        print(False)
    else:
        print(True)


#==============================================================


#############
# PROBLEM_2 #
#############

def commonCheck(circ1, start1, size1, circ2, start2, size2):
    final = []
    n1 = start1
    n2 = start2
    while n1-start1 < size1:
        if circ1[n1%len(circ1)] in circ2 and circ1[n1%len(circ1)] not in final:
            final += [circ1[n1%len(circ1)]]
        n1 += 1
    while n2-start2 < size2:
        if circ2[n2%len(circ2)] in circ1 and circ2[n2%len(circ2)] not in final:
            final += [(circ2[n2%len(circ2)])]
        n2 += 1
    print(final)


#==============================================================


#############
# PROBLEM_3 #
#############

import random

players = [1, 2, 3, 4, 5, 6, 7]
player_name = {1: "Player 1", 2: "Player 2", 3: "Player 3", 4: "Player 4", 5: "Player 5", 6: "Player 6", 7: "Player 7"}
size = 7
while size >= 1:
    if size > 1:
        chosen = random.randint(0, 3)
        print(chosen)
        if chosen == 1:
            print("Music stops")
            elim = players[int(size//2) - 1]
            players[int(size//2) - 1] = 0
            print(player_name[elim], "has been eliminated.")
            size -= 1
            for i in range(size):
                if players[i] == 0:
                    players[i] = players[i+1]
                    players[i+1] = 0
            d = [0]*size
            for i in range(size):
                d[(i+1)%len(d)] = players[i%size]
            for i in range(size):
                players[i] = d[i]
        else:
            print("Music continues")
            d = [0]*size
            for i in range(size):
                d[(i+1)%len(d)] = players[i%size]
            for i in range(size):
                players[i] = d[i]

    elif size == 1:
        print(player_name[players[0]], "is the winner.")
        break


#==============================================================