''''

predfine the alternative of the using the keyword

'''

from collections import namedtuple,Counter,defaultdict,deque

# student=namedtuple('student',['name','age','percentage'])
# s1=student(name='rohit',age=21,percentage=89)
# print(s1)

# l=[11,22,33,44,55,11,33,22,44,55,66,44,22,55,66]
# c=Counter(l)
# print(c)


# chap={'python':['intro python','functional'],'java':['intro java','oop']}
# print(chap['python'])
# print(chap['c'])
# student=defaultdict(list)
# student['python']=['intro python','functional']
# student['java']=['intro java','oop']
# print(student['c'])

# l=[11,22,33,44]
# d=deque(l)
# d.appendleft(10)
# print(d)

# sub=['python','java','c']
# marks=[89,98,67]
# print(dict(zip(sub,marks)))

l=[11,22,33,44,55]
obj=enumerate(l)
for index,element in obj:
    print(f'{index}==>{element}')
