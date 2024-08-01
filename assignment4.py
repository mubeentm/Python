"""create a coustemisable iterator which will give next prime number"""

class Primeiterator:
    def __init__(self,min,max):
        self.min = min
        self.max = max
    def __iter__(self):
        self.n = self.min
        return self
    def primenumbers(self):
        for i in range(self.n, self.max):
            count = 0
            for j in range(2, i + 1):
                if i % j == 0:
                    count += 1
            if count == 1:
                self.n += 1
                return i

            else:
                self.n += 1
    def __next__(self):
        if self.n>=self.min and self.n<=self.max:
            result = self.primenumbers()
            return result
        else:
            return StopIteration

number = Primeiterator(10,20)
i = iter(number)
print(next((i)))
print(next((i)))
print(next((i)))
print(next((i)))
