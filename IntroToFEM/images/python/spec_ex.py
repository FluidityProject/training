import pylab as p
import sympy as s


x=s.var('x')

f=x*(x-2)*(x-0.4)*(x-s.pi)


a0=s.integrate(f,(x,0,s.pi))/s.pi

a=[a0]
b=[0]


for k in range(1,11):
    a.append(1.0*s.integrate(f*s.cos(k*x),(x,0,s.pi))/s.pi)
    b.append(1.0*s.integrate(f*s.sin(k*x),(x,0,s.pi))/s.pi)

p.figure()

xx=p.linspace(0.0,p.pi,201)
y=[f.evalf(subs={x:X}) for X in xx]
y1=a[0]+a[1]*p.cos(xx)+b[1]*p.sin(xx)
y2=y1+a[2]*p.cos(2.*xx)+b[2]*p.sin(2.*xx)
y3=y2+a[3]*p.cos(3.*xx)+b[3]*p.sin(3.*xx)
yr=y3+0
for k in range(4,11):
    yr+=a[k]*p.cos(k*xx)+b[k]*p.sin(k*xx)

p.plot(xx,y,'k',label='$f(x)$',lw=4)
p.plot(xx,y1,'b:',label='$N=1$',lw=2)
p.plot(xx,y2,'y-',label='$N=2$',lw=2)
p.plot(xx,y3,'r--',label='$N=3$',lw=2)
p.plot(xx,yr,'g--',label='$N=10$',lw=2)

p.legend(loc=0)

p.yticks([])
p.ylabel('$f(x)$',fontsize='large')
p.xlabel('$x$',fontsize='large')
p.xticks([0,p.pi],[r'0',r'$L$'],fontsize='large')

v=p.axis()
p.axis([0,p.pi,v[2],v[3]])

p.savefig('spec_ex.png')
p.figure()

p.plot(xx,y,'k',label='$f(x)$',lw=4)

p.legend(loc=0)

p.yticks([])
p.ylabel('$f(x)$',fontsize='large')
p.xlabel('$x$',fontsize='large')
p.xticks([0,p.pi],[r'0',r'$L$'],fontsize='large')

v=p.axis()
p.axis([0,p.pi,v[2],v[3]])

p.savefig('spec_ex_0.png')

p.figure()

p.plot(xx,y,'k',label='$f(x)$',lw=3)
p.plot(xx,y1,'b:',label='$N=1$',lw=4)

p.legend(loc=0)

p.yticks([])
p.ylabel('$f(x)$',fontsize='large')
p.xlabel('$x$',fontsize='large')
p.xticks([0,p.pi],[r'0',r'$L$'],fontsize='large')

v=p.axis()
p.axis([0,p.pi,v[2],v[3]])

p.savefig('spec_ex_1.png')


p.figure()

p.plot(xx,y,'k',label='$f(x)$',lw=3)
p.plot(xx,y1,'b:',label='$N=1$',lw=2)
p.plot(xx,y2,'y-',label='$N=2$',lw=4)

p.legend(loc=0)

p.yticks([])
p.ylabel('$f(x)$',fontsize='large')
p.xlabel('$x$',fontsize='large')
p.xticks([0,p.pi],[r'0',r'$L$'],fontsize='large')

v=p.axis()
p.axis([0,p.pi,v[2],v[3]])

p.savefig('spec_ex_2.png')

p.figure()

p.plot(xx,y,'k',label='$f(x)$',lw=3)
p.plot(xx,y1,'b:',label='$N=1$',lw=3)
p.plot(xx,y2,'y-',label='$N=2$',lw=2)
p.plot(xx,y3,'r--',label='$N=3$',lw=4)

p.legend(loc=0)

p.yticks([])
p.ylabel('$f(x)$',fontsize='large')
p.xlabel('$x$',fontsize='large')
p.xticks([0,p.pi],[r'0',r'$L$'],fontsize='large')

v=p.axis()
p.axis([0,p.pi,v[2],v[3]])

p.savefig('spec_ex_3.png')

