'''
The Karl Pearson’s product-moment correlation coefficient (or simply, the Pearson’s correlation coefficient) is a measure of the strength of a linear association between two variables and is denoted by r or rxy(x and y being the two variables involved).

This method of correlation attempts to draw a line of best fit through the data of two variables, and the value of the Pearson correlation coefficient, r, indicates how far away all these data points are to this line of best fit.


Karl Pearson Correlation Coefficient Formula

The coefficient of correlation rxy between two variables x and y, for the bivariate dataset (xi,yi) where i = 1,2,3…..N; is given by –

r(X,Y)=cov(X,Y)/(σX * σY)

where,
⇒ cov(X,Y) : the covariance between x and y
⇒ cov(X,Y) :1/n(Σ(XiYi) - Xmean*Ymean)

⇒ σX and σY are the standard deviations of the distributions x and y.

σX(sigmaX) : sqrt(ΣXi^2 - Xmean^2)
σY(sigmaX) : sqrt(ΣYi^2 - Ymean^2)

'''
import numpy as np
import math as m
xi=[]
yj=[]
x=int(input('Enter Number of values on X-axis :' ))
y=int(input('Enter Number of values on Y-axis :' ))
n=y=x
if(x!=y):
    print('X and Y coordinates must be same\nCannot calculate with the given values')
else:
    print('Enter X-coordinate values :')
    for i in range(x):
        print('Enter x[',i,'] value :')
        xaxis=int(input())
        xi.append(xaxis)
    for j in range(y):
        print('Enter y[',j,'] value :')
        yaxis=int(input())
        yj.append(yaxis)
    xi=np.array(xi)
    yj=np.array(yj)
    print('Values in x-coordinate are :',xi)
    print('Values in y-coordinate are :',yj)
    #print(type(xi),type(yj))
    #calculating mean
    sumX=0
    sumY=0
    for i in range(x):
        sumX+=xi[i]
    #print('SumX :',sumX)
    for j in range(y):
        sumY+=yj[j]
    #print('sumY :',sumY)
    x_mean=sumX/x
    y_mean=sumY/y
    #print(x_mean,y_mean)
    prod=[]
    sumP=0

    for k in range(n):
        prod.append(xi[k]*yj[k])
        sumP+=prod[k]
    sumXYn=sumP/n
    #print(prod)
    #print(sumP)
    #print(sumXYn)
    co_var=(sumXYn-(x_mean*y_mean))
    print('\nCoVariance of the given data :',co_var)
    sumX2=[]
    sumY2=[]
    sum1=0
    sum2=0
    for k in range(n):
        sumX2.append((xi[k]**2))
        sumY2.append((yj[k]**2))
        sum1+=sumX2[k]
        sum2+=sumY2[k]
    #print(sum1,sum2)
    
    sdX=(sum1/n-(x_mean**2))
    sdY=(sum2/n-(y_mean**2))
    print('\nSD of X :',m.sqrt(sdX))
    print('SD of Y :',m.sqrt(sdY))
    KP=co_var/(m.sqrt(sdX)*m.sqrt(sdY))
    
    print('\nkarl pearson correlation coeff :',KP)
