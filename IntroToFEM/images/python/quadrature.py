import pylab as p




def f(x):
    return 5+p.sin(6*x+0.3)+2*p.cos(8.3*x+0.1)


x=p.linspace(0,1,101)

p.fill_between(x,0*x,f(x),zorder=2,color='lightblue')
p.plot(x,f(x),lw=3,color='k',zorder=5)
p.xticks([0,1],['$a$','$b$'],fontsize=18)
p.yticks([])

p.savefig('quad_func_0.eps')
p.savefig('quad_func_0.pdf')


def quad(pp,w):
    P=p.array([pp-w/2,pp+w/2])
    p.fill_between(P,0,[f(pp),f(pp)],
                   zorder=10,color='lightgreen')
    P=p.array([pp-w/2,pp-w/2,pp+w/2,pp+w/2])
    p.plot(P,[0,f(pp),f(pp),0],lw=3,color='k',ls='dotted',zorder=11)   
    p.scatter(pp,f(pp),c='r',s=80,zorder=12)


quad(0.2,0.4)
quad(0.5,0.3)
quad(0.8,0.4)


p.savefig('quad_func_1.eps')
p.savefig('quad_func_1.pdf')


