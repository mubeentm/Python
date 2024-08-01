'''#prob 1
class Vehicle:
    def __init__(self,max_speed,milage):
        self.max_speed=max_speed
        self.milage=milage
'''
'''
#prob2
class Vehicle:
    def __init__(self,max_speed,milage):
        self.max_speed=max_speed
        self.milage=milage
class Bus(Vehicle):
    pass
'''
'''
#prob3
class Vehicle:
    def __init__(self,max_speed,milage):
        self.max_speed=max_speed
        self.milage=milage
    def seating_capacity(self,capacity):
        print("Have a capacity of",capacity)
class Bus(Vehicle):
    def seating_capacity(self,capacity=50):
        return super().seating_capacity(capacity=50)

sbus=Bus(100,20)
sbus.seating_capacity()

'''
#prob 4
class Vehicle:
    def __init__(self,max_speed,milage,capacity):
        self.max_speed=max_speed
        self.milage=milage
        self.capacity=capacity
    def fare(self):
        return self.capacity*100

class Bus(Vehicle):
    def fare(self):
        price=super().fare()
        price += price*0.1
        return price

sbus=Bus(100,20,50)
car=Vehicle(140,30,4)
if isinstance(car,Bus):
    print("Total Fare",sbus.fare())
else:
    print("Total Fare", car.fare())
# print(isinstance(sbus,Vehicle))
'''
class Vehicle():
    def __init__(self,max_speed,min_speed,capacity):
        self.max_speed=max_speed
        self.min_speed=min_speed
        self.capacity=capacity

    def seating_capacity(self, capacity=50):
        print("seating capacity : ",self.capacity)

    def fare_charge(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self,max_speed,min_speed,capacity=50):
        super().__init__(max_speed,min_speed,capacity)
    def fare_charge(self):
        amount = super().fare_charge()
        amount += amount*0.1
        return amount
bus=Bus(10,40)
bus.seating_capacity()
bus.fare_charge()
'''

