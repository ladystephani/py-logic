## functions syntax
# def in python is like function in JS
def calculation(a, b):
    c = a + b
    return c
# print(calculation(1,2))

# something JS don't use - tuple
# uses () instead of []
def order(*caf_food):
    return caf_food
# print(order('红香肠', '玉子烧')) # order()
# output
#('红香肠', '玉子烧') -- a tuple

#python 真的很数学啊，whereas JS是真的很网页制作啊

##
class North_america_resident:
    def __init__(self, name, origin, current_base): # (parameters) are what JS takes right after class Name()
        self.name = name
        self.origin = origin
        self.current = current_base

    def has_roots(self):
        print(self.name + ' has roots in ' + self.origin)

    def current_area(self):
        print(self.name + ' is now living in ' + self.current)

person1 = North_america_resident('LadyStephani', 'Fujian', 'PNW')
# person1.current_area()

for i in range(9):
    if i % 2 == 0:
        continue
    print(i)