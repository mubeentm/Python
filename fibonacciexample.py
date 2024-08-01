def fibonacci_numbers(nums):
    x,y = 0,1
    for _ in range(nums):
        x,y = y,x+y
        yield x


def primenumbers(nums):
    # l=x
    l = list(nums)
    print(l)
    for i in range(l[0],l[len(l)-1]):
        value = l[0]
        count = 0
        for j in range(2, i + 1):
            if i % j == 0:
                count += 1
        if count == 1:
            value += 1
            yield i
        else:
            value += 1

for value in primenumbers(fibonacci_numbers(10)):
    print(value)