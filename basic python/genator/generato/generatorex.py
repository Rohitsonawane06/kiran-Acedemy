''''
A generator in Python is a function that returns an iterator, which produces a sequence of values one at a time when iterated over.  

The yield keyword in Python is used to create generator functions. These functions, when called, return a generator object, which is a type of iterator. Instead of computing all values at once and storing them in memory like a regular function, a generator yields values one at a time, on demand.

'''

# def myfun(s,e):
#     for i in range(s,e):
#         yield i
# gobj=myfun(1,6)
# print(next(gobj))
# print(next(gobj))

# using a list compresion
# number=[num for num in range(1,11)]
# print(number)
# number1=(num for num in range(1,11))
# print(number1)
# print(next(number1))
# print(next(number1))
# print(next(number1))
# print(next(number1))
# print(next(number1))
# print(next(number1))
# print(next(number1))
# print(next(number1))
# print(next(number1))
# print(next(number1))

# usinga file 
def read_data(file):
    f=open(file,'r')
    data=f.read()
    return(data)
print(read_data('data.txt'))

#using the generator function

def my_gen(file):
    f=open(file,'r')
    for line in f:
        yield line
obj=my_gen('data.txt')
print(next(obj))
print(next(obj))
print(next(obj))
