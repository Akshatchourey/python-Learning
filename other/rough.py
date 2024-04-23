# impli cit type convertion

'''a=int(input("enter the value of a"))
b=int(input("ehter the value of b"))
sum =a/b
print("the sum is",sum)
print("the data type of the sum is",type(sum))'''


'''a=3
b=4
print(a is not b)'''


'''gat=39
b=35
c=gat
print(c+b)

a="akshat"
print([0:6])'''

'''=5
y=10
x=20
z=30
d=str(input("enter the value of d"))

if(d=='v'):
    d=v
elif(d=='x'):
    d=x
elif(d=='z'):
    d=z
else:
    d=y

a=int(input("how many do you want"))
d*=a
f=bool(input("do you want to continew,yes or \n if not click Enter"))
while(f==1):
    b=str(input("\nnext please"))
    if(b=='v'):
        b=v
    elif(b=='x'):
        b=x
    elif(b=='z'):
        b=z
    else:
        b=y
    a=int(input("how many do you want"))
    b*=a
    d+=b
    print(d)
    f=bool(input("do you want to continew\nif not click enter"))
    if(f==0):
        break
print("thaankyu")
print(d)
'''




# Merge the Tools! Question HackerRank:-
"""
def merge_the_tools(s, k):
    arr = []
    n = len(s) / k
    n = int(n)
    a = 0
    b = k
    for i in range(n):
        arr.append(s[a:b])
        a = b
        b += k

    for i in range(n):
        s1 = arr[i]
        s2 = ""
        for k in s1:
            if k in s2:
                continue
            s2 += k
        print(s2)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
"""
