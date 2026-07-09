a=1
b=2
c=3

temp=a
a=b
b=c
c=temp 

print(a,b,c)
print("a:", a)
print("b:", b)
print("c:", c)
 
if a>b and a>c:
    print("a is the largest")

elif b>a and b>c:
    print("b is the largest")

elif c>a and c>b:
    print("c is the largest")