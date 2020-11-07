# 2.dictionary showing count of elements
x=[11,45,8,11,23,45,23,45,89]
print("list:",x)
y={}
for i in x:
    count=0
    for j in x:
        if(i==j):
            count=count+1
    y[i]=count
print("count:",y)