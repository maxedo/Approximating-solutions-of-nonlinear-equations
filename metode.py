import numpy as np
from sympy import *
from scipy.optimize import minimize_scalar, fsolve
def bisectie_er(f,a,b,err):
    z=Symbol("x")
    f=lambdify(z,f)#f=functie
    while (b-a)/2>err:
        x=(a+b)/2
        if f(x)==0:
            return x
        elif f(a)*f(x)<0:
            b=x
        else: a=x
    return x


def bisectie_it(f,a,b,it):
    z=Symbol("x")
    f=lambdify(z,f)#f=functie
    for i in range(it):
        x=(a+b)/2
        if f(x)==0:
            return x
        elif f(a)*f(x)<0:
            b=x
        else: 
            a=x
    return x




def coarda_err(f,a,b,err):
    x=Symbol('x')
    f1=diff(f,x)
    f2=diff(f,x,2)
    f=lambdify(x,f)
    abs_f1='abs(' +str(f1)+')'
    f1l=lambdify(x, f1)
    f2l=lambdify(x,f2)
    abs_f1l=lambdify(x, abs_f1)
    m=minimize_scalar(abs_f1l,bounds=(a,b),method='bounded')
    m1=m.fun
    if f(a)*f2l(a)<0:
        x=a
        while (abs(f(x))/m1)>err:
            x=x-f(x)/(f(x)-f(b))*(x-b)
            
    else:
        x=b
        while (abs(f(x))/m1)>err:
            x=x-f(x)/(f(x)-f(a))*(x-a)
            
    return x



def coarda_itr(f, a, b, n):
    x=Symbol('x')
    f2=diff(f,x,2)
    f=lambdify(x,f)
    f2l=lambdify(x,f2)
    if f(a)*f2l(a)<0:
        x=a
        for i in range (1,n):
            x=x-f(x)/(f(x)-f(b))*(x-b)
            
    else:
        x=b
        for i in range(1,n):
            x=x-f(x)/(f(x)-f(a))*(x-a)
            
    return x


def contractii_itr(f, a, b, x0, n):
    x=Symbol('x')
    f=lambdify(x,f)

    x=x0
    for i in range(1, n):
        x = f(x)
    
    return x

def contractii_err(f, a, b,x0,err):
    x = Symbol('x')
    f = lambdify(x, f) 
    x = x0
    termen = 1
    contractii=0.9
    while(contractii**termen) *(b-a) > err:
        termen+=1
        x = f(x)
    return x


def tangenta_eroare(f, a, b, err):
    x = Symbol('x')
    f1 = diff(f, x) #f'
    f2 = diff(f, x, 2) #f''
    f = lambdify(x, f) 
    abs_f1 = 'abs('+str(f1)+')'
    abs_f2 ='(-1)*abs('+str(f2)+')'
    f1l = lambdify(x, f1)
    f2l = lambdify(x, f2)
    abs_f1l = lambdify(x, abs_f1)
    abs_f2l = lambdify(x, abs_f2)
    m = minimize_scalar(abs_f1l, bounds = (a, b), method = 'bounded')
    m1 = m.fun
     
    m = minimize_scalar(abs_f2l, bounds = (a, b), method = 'bounded')
    m2 = (-1)*m.fun
    x=np.random.rand()*(b-a)+a
    x_ant = 0
    i=0
    while f(x)*f1l(x)<=0:
        x=np.random.rand()*(b-a)+a
        while m2/(2*m1)*abs(x-x_ant)**2 > err:
            x_ant = x
            x = x - f(x)/f1l(x)
            i+=1
    return x


def tangenta_iter(f, a, b, n):
    x = Symbol('x')
    f1 = diff(f, x) 
    f2 = diff(f, x, 2) 
    f = lambdify(x, f) 
    abs_f1 = 'abs('+str(f1)+')'
    
    f1l = lambdify(x, f1)
    f2l = lambdify(x, f2)
    abs_f1l = lambdify(x, abs_f1)
    
    x_ant = 0
    if f(a)*f2l(a) > 0:
        x = a
        for i in range (1,n):
            x_ant = x
            x = x - f(x)/f1l(x)
    else:
        x=b
        for i in range(1,n):
            x_ant = x
            x = x - f(x)/f1l(x)
    return x

