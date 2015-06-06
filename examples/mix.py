def getval2():
    localvariable2 = 1
    localvariable = 1
    localvariable2 = 2
    return 4
    
def getval(a):
    return 5-a

def lam(z):
    return lambda x: z+x
z = 1 + 2 + getval2(getval())
z = [1,2,3]