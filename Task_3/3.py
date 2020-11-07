# 3.Removing duplicates elements
x=[8,1,2,9,8,7,3,4,4,7,8]
print("list:",x)
for i in x:
    count=0
    for j in x:
        if(i==j):
            count=count+1
    if count>1:
        x.pop(x.index(i))
    
print("unique items:",x)
print("In tuple:",tuple(x))
x.sort()
print("min:",x[0])
print("max:",x[-1])