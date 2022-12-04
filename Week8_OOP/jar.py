class Jar:
    def __init__(self, capacity):
        self.capacity = capacity

    def __str__(self):
        return "c" * self.capacity

    def deposit(self, n):
        amount = self.__str__()
        return amount.__add__(n*"c")

    def withdraw(self, n):
        amount = self.__str__()
        return amount.remove(n*"c")
'''
    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
'''
def main():
    #cookie = Jar(6)
    #print(cookie)
    #cookie = cookie.deposit(3)
    #print(cookie)
    #cookie = cookie.withdraw(6)
    #print(cookie)
    str_1 = "cccc"
    new_str = str_1.replace(str_1, )

if __name__=="__main__":
    main()