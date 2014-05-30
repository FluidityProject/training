import pylab as p
import sympy as s

x=s.var('x')
ff=(1.0+s.sin(4*x)-2*s.sin(5*x+2))

def f(xx,fn=ff):
    try:
        len(xx)
        return p.array([fn.evalf(subs={x:X}) for X in xx],float)
    except:
        return fn.evalf(subs={x:xx})

def df(xx):
    return ff.diff(x).evalf(subs={x:xx})


xp=p.linspace(0.3,0.7,101)

xs=xp[slice(0,len(xp),20)]


p.figure(figsize=(6,4))
p.plot(xp,f(xp),lw=2)


def tanline(x,f,df,a,b):
    return [f+(a-x)*df,f+(b-x)*df]

a=xs[1]
b=xs[5]
c1=xs[3]
c0=xs[2]
c2=xs[4]
p.plot([a,b],tanline(c0,f(c0),(f(c2)-f(c0))/(c2-c0),a,b),'k--',lw=2)
p.plot([a,b],tanline(c1,f(c1),df(c1),a,b),'r--',lw=2)

#p.text(f(c1)+0.3,3.2,r'$\frac{df}{dx}\approx \frac{\Delta f}{\Delta x} := \frac{ f_{i+1}-f_{i-1}}{x_{i+1}-x_{i-1}}$')

p.scatter(xs,f(xs),c='k',s=60)

p.xticks([])
p.yticks([])
p.xlabel('$x$',fontsize='xx-large')
p.ylabel('$f(x)$',fontsize='xx-large')

v=p.axis()
p.axis([xs[0]-0.05,xs[-1]+0.05,min(map(float,[f(xs[0]),f(xs[-1])])),v[3]])

p.savefig('images/fin_dif.png')

