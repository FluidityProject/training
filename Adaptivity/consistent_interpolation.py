import pylab as p

def fn(xx,F,X):
    FF=[]
    for x in xx:
        I=0
        if x==X[0]:
            FF.append(F[0])
        else:
            for i in range(I,len(X)-1):
                if x > X[i] and x<=X[i+1]:
                    FF.append( F[i]+(F[i+1]-F[i])*(x-X[i])/(X[i+1]-X[i]))
                    break 
            I=i
        print x, X, I, FF[-1]

    return p.array(FF)

def f(x):
    return p.sin(2*p.pi*x)+2*p.cos(2*p.pi*x)+p.exp(-(x-0.3)**2)+2
    


X=p.array([0.,0.2,0.4,0.6,0.8,1.0])

X2=p.array([0,0.3,0.45,0.5,0.6,0.7,1.0])

p.figure(figsize=(12,4))

p.plot(X,f(X),'bo-',lw=2)
p.scatter(X,f(X),c='b',s=100)
f2=fn(X2,f(X),X)
p.plot(X2,f2,'ro--',lw=2)

p.axis([0,1,0,f(X).max()+0.1])
p.vlines(X,0,f(X),linestyle='dotted')
p.vlines(X2,0,f2,linestyle='dotted',colors='r')

p.yticks([])
p.ylabel('$f(x)$',fontsize='large')
p.xticks(X,['$x_{%s}$'%i for i in range(len(X))],fontsize='large')

p.savefig('ConsistentInterpolation.png')

