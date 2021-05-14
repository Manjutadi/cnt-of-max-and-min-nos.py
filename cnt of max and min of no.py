#cnt of max and min of no
n=int(input())
temp=n
max=0
min=9
c=d=0
while n:
    r=n%10
    n=n//10
    if r>max:
        max=r
    elif r<min:
        min=r
n=temp        
while n:
    r=n%10
    n=n//10
    if r==max:
        c+=1
    elif r==min:
        d+=1
print(max,c)
print(min,d)
