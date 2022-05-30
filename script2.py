# for sth in ''
# for sth in []
# for sth in {'': value} #output: key
    # print(sth)
for letter in 'pokemon':
    print(letter)
#output
# p
# o
# k
# e
# m
# o
# n
# for sth in range(num)
# for sth in range(num1, num2)
# for sth in range(num1, num2, num3)

# for sth in {dict/object}: //Python has to have the {} here. JS can skip and just write for () { //... }
    # print(dict[sth]) # logs each key's corresponding value

## a = 0
# while a < 5:
    # a += 1
    # print(a) #as long as a is still <5, goes thru the loop

# != in python is !== in js

# bool()


a=1
b=3
list = [1,2]
if a in list:
    print('Yep')
if b not in list:
    print('yay')

# to end if statement without print(), can use break
for a in list:
    if a == 1:
        break

# the use of pass in python, is like only using if statement w/o else in JS
# JS
# //if () {
# }
if a:
    print('true')
else:
    pass

##
# use continue when you want to skip the rest of the loop in that condition 

##
# else statement can be used with loops in python, as if it's for () {
# } else {
# }

## to use similar function as  `` in JS, use formatting with placeholder %s, %d, %f
# print() can contain '' including a %? operator
    # where ? can be s for string, d for numbers, f for float
# then followed by %, and something
print('Hi %s' % 'name')