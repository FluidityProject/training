import pylab as p
import sympy as s


x=s.var('x')
xd=p.linspace(0,10,401)

f=s.sin(x)+0.5*s.sin(3*x)-0.25*s.sin(4*x)
g=s.cos(x)+0.2*s.cos(4*x)+0.4*s.sin(2*x)

def fmake(f,X=x):
    F=lambda y:f.evalf(subs={X:y})
    return lambda y:p.array(map(F,y))

F=fmake(f)
G=fmake(g)

p.figure()
p.plot(xd,F(xd),'r',label='$f(x)$',lw=4)
p.plot(xd,G(xd),'m.',label='$g(x)$',lw=4)
p.legend(loc=1,frameon=False)
p.xticks([])
p.yticks([])
p.hlines(0,0,10,linestyles='dashed')
p.vlines(5,-6,6,linestyles='dashed')
p.savefig('add_fns_0.png')

p.figure()
p.plot(xd,F(xd),'r',label='$f(x)$',lw=2)
p.plot(xd,G(xd),'m.',label='$g(x)$',lw=2)
m=p.plot(xd,F(xd)+G(xd),'k',label='$(f+g)(x)$',lw=4)
p.legend(loc=1,frameon=False)
p.xticks([])
p.yticks([])
p.hlines(0,0,10,linestyles='dashed')
p.vlines(5,-6,6,linestyles='dashed')
p.savefig('add_fns_1.png')

p.figure()
p.plot(xd,F(xd),'r',label='$f(x)$',lw=2)
p.plot(xd,G(xd),'m.',label='$g(x)$',lw=2)
p.plot(xd,2*F(xd),'y',label='$2f(x)$',lw=4)
p.legend(loc=1,frameon=False)
p.xticks([])
p.yticks([])
p.hlines(0,0,10,linestyles='dashed')
p.vlines(5,-6,6,linestyles='dashed')
p.savefig('add_fns_2.png')
