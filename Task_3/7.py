
# 7.calling a function with new name
def displaystudent(name,age):
    print("The age of {} is:\n".format(name),age)
    
displaystudent("sree\n",23)
showstudent=displaystudent
showstudent("gita\n",24)