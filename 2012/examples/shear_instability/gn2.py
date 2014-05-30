from scipy.optimize import fsolve
import scipy as s
import pickle


x=s.linspace(0,100,1001)
dx=x[1]

h1=2
h2=18

r1=1000.-1.1
r2=1000.+1.1


g=9.81

c0=s.sqrt(g*h1*h2*(r2-r1)/(r1*h2+r2*h1))

c=0.328


q1=-c**2/g-h1+h2
q2=h1*h2*(c**2/c0**2-1.0)

A=h1*h2*(r1*h1+r2*h2)/(r1*h1**2+r2*h2**2)


r=(-q1+s.sqrt(q1**2-4.0*q2))/2

print r


y=s.zeros(len(x))
y[0]=r

k=(3.0*g*(r2-r1)/(c**2*(r1*h1**2-r2*h2**2)))

def G(a):
    return k*a**2*(a**2+q1*a+q2)/(a-A)

def dG(a):
    return k*(2.0*a*(a**2+q1*a+q2)+a**2*(2.0*a+q1))/(a-A)-k*a**2*(a**2+q1*a+q2)/(a-A)**2



y[0]=r

              
for kk,xx in enumerate(x[1:]):
    y[kk+1]=y[kk]+dx*s.sqrt(G(y[kk]))+dx**2*dG(y[kk])/4.0
    
f=open('data.dat','w')

pickle.dump(x,f)
pickle.dump(y,f)
pickle.dump(c,f)

x=x[::20]
y=y[::20]


f.close()
f=open('tank_int.geo','w')

f.write('Point(1)={-100,10,0};\n')
f.write('Point(2)={100,10,0};\n')
f.write('Point(3)={100,-10,0};\n')
f.write('Point(4)={-100,-10,0};\n')

for k,(X,Y) in enumerate(reversed(zip(x,y))):
    f.write('Point(%s)={%s,%s,0};\n'%(k+5,X,8+Y))
    f.write('L[]+=%s;\n'%(k+5))


K=k+5

for k,(X,Y) in enumerate(zip(x[1:],y[1:])):
    f.write('Point(%s)={%s,%s,0};\n'%(k+K+1,-X,8+Y))
    f.write('L[]+=%s;\n'%(k+K+1))

N=k+K+1

for k in range(2*len(x)-2):
    f.write('Line(%s)={%s,%s};\n'%(7+k,k+5,k+6))
    f.write('R[]+=%s;\n'%(7+k))


f.write('Line(1)={1,2};\n')
f.write('Line(2)={2,5};\n')
f.write('Line(3)={5,3};\n')
f.write('Line(4)={3,4};\n')
f.write('Line(5)={4,%s};\n'%N)
f.write('Line(6)={%s,1};\n'%N)


#f.write('Line Loop(1)=R1;\n')
f.write('Line Loop(1)={1,2,R[],6};\n')
f.write('Line Loop(2)={R[],-5,-4,-3};\n')

f.write('Periodic Line (2)= {-6};\n')
f.write('Periodic Line (3)= {-5};\n')


f.write('Physical Line(1)={1};')
f.write('Physical Line(2)={2};')
f.write('Physical Line(3)={3};')
f.write('Physical Line(4)={4};')
f.write('Physical Line(5)={5};')
f.write('Physical Line(6)={6};')

f.write('Field[1]=Attractor;\n')
f.write('Field[1].NodesList={L[]};\n')

f.write('Field[2]=MathEval;\n')
f.write('Field[2].F="0.5+0.03*F1*F1";\n')

f.write('Background Field=2;\n')

f.write('Plane Surface(1)={1};\n')
f.write('Plane Surface(2)={2};\n')
f.write('Physical Surface(1)={1};\n')
f.write('Physical Surface(2)={2};\n')

f.close
