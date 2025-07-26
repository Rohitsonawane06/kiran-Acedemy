'''
iterator
iterable
iteration=>out of the list is  called iteration
l=[11,22,44] iterable
for num in l:iterator
    print (num)
    11 iteration
    22
    44
'''
# l=[11,22,44] #iterable
# for num in l:#iterator
#     print (num)

#iter function is return of the object
# l=[1,2,3,4] #iterable
# print(type(l))#<class 'list'>
# iter_obj=iter(l)#iterator
# print(type(iter_obj))#<class 'list_iterator'>
# #iteration
# #next=>Return the next item from the iterator.
# print(next(iter_obj))
# print(next(iter_obj))
l=[11,22,33]

# def check(obj):
#     list_of_method=dir(obj)
#     if '__iter__' in list_of_method and '__next__'in list_of_method :
#         return 'iterator'
#     elif '__iter__' in list_of_method:
#         return 'iterable'
#     else:
#         return 'nothig'
# print(check(l))

class myrange:
    def __init__(self,start,stop,step):
        self.start=start
        self.stop=stop
        self.step=step
    def __iter__(self):
        return myrange_iterator(self)



class myrange_iterator:
    def __init__(self,iterable_obj):
        self.iterable_obj=iterable_obj
    def __iter__(self):
        return self
    def __next__(self):
        result=self.iterable_obj.start
        if self.iterable_obj.start<self.iterable_obj.stop:
            self.iterable_obj.start=self.iterable_obj.start+self.iterable_obj.step
            return result
        else:
            raise StopIteration
for i in myrange(2,21,2):
    print(i)