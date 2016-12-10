from sympy import *
import numpy as np
def PO(G):
    for i in range(G.__len__()):
        if G[i]<0:

            return False
    return True
def absdf(df):
    return sqrt((df[0]**2)+df[1]**2)
x1=symbols('x1')
x2=symbols('x2')
print("Function:")
f=eval(input())
print("X01:")
x01=input()
print("X02:")
x02=input()
X1=Matrix([[x01],[x02]])
print("eps:")
eps=float(input())
G=Matrix([[diff(f,x1,x1),diff(f,x1,x2)],[diff(f,x2,x1),diff(f,x2,x2)]])
print("Gesse Matrix: ",G)
InvG=G.inv()

df=Matrix([[diff(f,x1)],[diff(f,x2)]])

Gsubs=G.subs([(x1,X1[0]),(x2,X1[1])])
dfsubs=df.subs([(x1,X1[0]),(x2,X1[1])])
while absdf(dfsubs)>eps :


    Xk=X1-InvG.subs([(x1,X1[0]),(x2,X1[1])])*df.subs([(x1,X1[0]),(x2,X1[1])])
    X1=Xk

    Gsubs = G.subs([(x1, X1[0]), (x2, X1[1])])
    dfsubs = df.subs([(x1, X1[0]), (x2, X1[1])])

print("Xmin = ",(round(float(Xk[0]),2),round(float(Xk[1]),2)))