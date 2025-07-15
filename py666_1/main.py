'''class Vecor:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return self+other
v1=Vecor(1,2)
v2=Vecor(3,4)
print((v1+v2).x,(v1+v2).y)'''
'''class Mysequence:
    def __init__(self,data):
        self.data=list(data)
    def __getitem__(self,index):
        return self.data[index]
my=Mysequence([1,2,3,4,5])
print(my[-1])
class Mysequence:
    def __init__(self,data):
        self.data=data
    def __getitem__(self,index):'''
'''class Countdown:
    def __init__(self,start):
        self.start=start
        self.count=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.count<0:
            raise StopIteration
        else:
            value=self.count
            self.count-=1
            return value
for i in Countdown(3):
    print(i)'''
'''class Revers:
    def __init__(self,text):
        self.text=text
    def __reversed__(self):
        return self.text[::-1]
s='Python'
for char in reversed(s):
    print(char,end=' ')'''
'''class Matrix:
    def __init__(self,data):
        self.data=data
    def __add__(self,other):
                result=[(self.data[i][j]+other.data[i][j]) for j in range(len(self.data[0]))
                        for i in range(len(self.data)) ]
                return result
    def __mul__(self,other):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                result=[self.data[i][j]*other.data[i][j]]
    def __getitem__(self,indices):
        if isinstance(indices,tuple) and len(indices)==2:
            roe,col=indices
            return self.data[roe][col]
        else:
            raise TypeError('你妈')
a=Matrix([[1,2],[4,5]])
b=Matrix([[6,7],[9,10]])
print(b+a)'''
#getattr call
'''data=[frozenset([1,2,3])].append(4)
print(data)'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_vers(self):
        print(vars(self))
p=Person('Alice',25)
p.show_vers()


