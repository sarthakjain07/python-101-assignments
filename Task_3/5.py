
# 5.summation using inner and outerfunctions.
def outerfun(x,y):
    def innerfun(a,b):
        sum=a+b
        return sum
    finalsum=5+innerfun(x,y)
    return finalsum
sum=outerfun (2,3)
print("sum:",sum)