import numpy as np


class MasterMind:
    def __init__(self, n=4, trymax=100, rep=False):
        self.n = n
        self.rep = rep
        self.__code = []
        self.prop = np.array(["a", "b", "c", "d", "e", "f", "g", "h"])
        self.trymax = trymax
        self.ctry = 0

    def generate(self):
        self.__code = np.random.choice(self.prop, self.n, self.rep)

    def test_nbr(self, a):
        return len(a) == self.n

    def test_pr(self, a):
        d = {}
        for i in a:
            d[i] = d.get(i, 0) + np.count_nonzero(self.__code == i) #Problème : compte plusieurs fois la même valeur
        return sum(d.values())

    def test_place(self, a):
        l = np.zeros(self.n)
        for i in range(self.n):
            l[i] = a[i] == self.__code[i]
        return l

    def addtry(self):
        self.ctry += 1

    def reset(self):
        self.generate()
        self.ctry = 0

    def message(self,a):
        print("Try " + str(self.ctry) + ". There are " + str(self.test_pr(a)) + " good values. Your placement are : " + str(self.test_place(a)))

    def rules_message(self):
        print(("-"*10))
        print("Your rules are :")
        print("Lenght : " + str(self.n))
        print("Repetition : " + str(self.rep))
        print("Max try : " + str(self.trymax))
        print(("-"*10))

    def shot(self, a):
        if self.test_nbr(a):
            self.addtry()
            self.message(a)
            return all(a == self.__code)
        else:
            raise ValueError("You have to enter " + str(self.n) + " inputs")

    def __str__(self):
        return "The code is " + str(self.__code)
