class Jar:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "c" * self.size

    def deposit(self, n):
       self.size += n

    def withdraw(self, n):
        self.size -= n
'''
    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
'''
def main():
    cookie = Jar(12)
    cookie.deposit(5)
    cookie.withdraw(3)
    print(cookie)
    
    


if __name__=="__main__":
    main()