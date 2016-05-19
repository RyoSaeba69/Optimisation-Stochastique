import math,pylab

x0 = float(input('Enter beginning of interval: ')) #start of interval
xf = float(input('Enter endpoint of interval: ')) #end of interval
a = float(input('Enter a value for a: '))
#x = float(input('Enter a value for x: '))
e = float(input('Enter desired error tolerance: '))
n = int(input('Enter number of iterations: '))

def wer(a, x, e): # a is givin number, e is error tolerance

    Sum1 = 0
    Sum2 = 0
    k = 1

    while(True):
        #sine of pi times k to the a times x over pi times k to the a
        Sum1 = math.sin((math.pi)*pow(k,a)*(x))/((math.pi)*(pow(k,a)))
        Sum2 = Sum1 + math.sin((math.pi)*pow((k+1),a)*(x))/((math.pi)*pow((k+1),a))

        if (abs(Sum2-Sum1) < e):
            break
        else:
            k+=1
    return Sum1

def append(x0, xf, n):

    xl = [] #list containing x values
    yl = [] #corresponding y values
    dx = (xf-x0)/n #length of each subinterval

    for i in range (0, (n+1)):
        xval = x0 + (i * dx)
        yval = wer(a, (xval), e) #ERROR HERE

        xl.append(xval)
        yl.append(yval)
        #print i,':',xl
    return xl, yl


append(x0, xf, n)
pylab.plot(xl,yl)
