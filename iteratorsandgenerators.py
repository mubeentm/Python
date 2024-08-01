"Iterators - are methods that are used to iterate collections like list, tuples etc."
"used to have one by one iterations"
"""
prime_numbers = [1,3,5,7,11,13,17,19,29]
pn_iterator = iter(prime_numbers)
print(next(pn_iterator))
print(next(pn_iterator))
print(next(pn_iterator))
print("*"*60)
for num in pn_iterator:
    print(num)#here the iterated starts from 4 because three of them are already iterated
"""

class PowThree:
    """Class implements an iterator of power of three"""
    def __init__(self,max=0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 3**self.n
            self.n += 1
            return result
        else:
            raise StopIteration
numbers = PowThree(10)
i = iter(numbers)
counter = 0
print("3 power ",counter, "=", next(i))
counter+=1
print("3 power ",counter, "=", next(i))
counter+=1
print("3 power ",counter, "=", next(i))
counter+=1
