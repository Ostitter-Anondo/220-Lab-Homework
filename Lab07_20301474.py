#   ____ ____  _____ ____  ____   ___  
#  / ___/ ___|| ____|___ \|___ \ / _ \ 
# | |   \___ \|  _|   __) | __) | | | |
# | |___ ___) | |___ / __/ / __/| |_| |
#  \____|____/|_____|_____|_____|\___/ 
#                                      
# 
#  _      _   ___      __ ____ 
# | |    /_\ | _ )___ /  \__  |
# | |__ / _ \| _ \___| () |/ / 
# |____/_/ \_\___/    \__//_/  







# Submitted by,
##  Jawad Ibn Mamoon
##  ID: 20301474
##  Section 02




#===========================================================================#

# *********************** Key Index Search and Sort *********************** #

#===========================================================================#


##########
# TASK_1 #
##########


class KeyIndex:
    def __init__(self, a):
        l = a[0]
        s = a[0]
        for i in a:
            if i > l:
                l = i
            if i < s:
                s = i
        if s < 0:
            x = s*(-1)
        else:
            x = 0
        self.x = x
        k = [0]*(x+l+1)
        for i in a:
            k[i+x] += 1
        self.k = k
        self.l = l
        self.s = s

    def search(self, n):
        if n > self.l or n < self.s:
            return False
        elif self.k[n+self.x] > 0:
            return True
        else:
            return False

    def sort(self):
        m = []
        for i in range(len(self.k)):
            for j in range(self.k[i]):
                m += [i-self.x]
        return m


array = KeyIndex([4, 2, 2, 3, 5, 1, 7, -4])
print(array.sort())



#===========================================================#

# *********************** Hashtable *********************** #

#===========================================================#


##########
# TASK_2 #
##########


class Hashtable:
    def __init__(self, a):
        x = len(a)
        l = [0]*x
        consonant = "BCDFGHJKLMNPQRSTVWXYZ"
        numbers = "0123456789"
        for string in a:
            con = 0
            num = 0
            for letter in string:
                if letter in consonant:
                    con += 1
                elif letter in numbers:
                    num += int(letter)
            ind = (con*24+num)%9
            if l[ind] == 0:
                l[ind] = string
            else:
                while l[ind % x] != 0:
                    ind += 1
                l[ind % x] = string
        self.l = l
    
    def show_hashtable(self):
        return self.l
