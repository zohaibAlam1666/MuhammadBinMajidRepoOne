list = [1,2,4,5,6,7]

squ = [x*x for x in list]

print(squ)

import itertools

def fib(n):
     a, b = 0, 1

     for _ in range(n):
          yield a
          a, b = b, a + b

b = fib(20)

print(next(b))

print(next(b))

newseries = list(itertools.islice(b,14))


class Bank:

    def __init__(self, owner, balance=0):
          self.owner = owner
          self.balance = balance
          self.newValue = "nenenen"

    



    def  depost(self, parFirst):

         print(f"balance {self.balance}")        


account = Bank("Ali", 10000)

account.depost("skldjfkllsdj")