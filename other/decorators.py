
#ex-1
"""
def func1():
    print("Akshat Chourey")
    
def dec1(a):
    def nowexe():
        print("---------------")
        a()
        print("---------------")
    return nowexe

func1=dec1(func1)
func1()
"""
#ex-2 == error
"""
def dec1(a):
    print("----------------")
    a()
    print("----------------")

def func1():
    print("Akshat Chourey")

func1=dec1(func1)
func1()
"""
#ex-3 == devision
"""
a,b=2,6
def divide(a,b):
    print(a/b)
def swap(divide):
    def final(a,b):
        if a<b:
            a,b=b,a
        divide(a,b)
    return final
swap(divide)(a,b)
"""
#ex-4 == recursion in python
"""
a=10
def exa(a):
    print(a)
    if a>0:
        a -=1
        return exa(a)
exa(a)
"""

a=input("enter to exit")
