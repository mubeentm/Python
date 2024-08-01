#Generator is a function that returns an iterator that produces a sequence of values
#when iterated over
"""
def custom_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1
value=custom_generator(10)
print(next(value))
print()
for value in custom_generator(10):
    print(value)

"""
"""
cubes_generator = (i*i*i for i in range(5))
for j in cubes_generator:
    print(j)
"""
"""
class PowerThree:
    def __init__(self,max=0):
        self.n=0
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if self.n>self.max:
            raise StopIteration
        result = 3**self.n
        self.n+=1
        return result
def GenPowerThree(max=0):
    value=0
    while value < max:
        yield 3**value
        value += 1
number = PowerThree(10)
i=iter(number)
print(next(i))
print(next(i))
print(next(i))
"""

def fibonacci_numbers(nums):
    x,y = 0,1
    for _ in range(nums):
        x,y = y,x+y
        yield x
def square(nums):
    for num in nums:
        yield num ** 2

'''
for value in fibonacci_numbers(10):
    print(value,end=" ")
'''
for value in square(fibonacci_numbers(4)):
    print(value)
print(sum(square(fibonacci_numbers(4))))
