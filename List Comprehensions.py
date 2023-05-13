
x = int(input())
y = int(input())
z = int(input())
n = int(input())
list2 = []
for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if(a+b+c!=n):
                list1=[a,b,c]
                list2.append(list1)
print(list2)
                