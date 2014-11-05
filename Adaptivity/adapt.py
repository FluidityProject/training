import sympy as s
import pylab as p


x=s.var('x')

def adapt(f,X):
    ddf=f.diff(x).diff(x)
    print ddf
    DDF=lambda a:abs(ddf.evalf(subs={x:a}))
    XX=p.linspace(X[0],X[-1],1001)
    h=XX[1]-XX[0]
    M=p.zeros(1001)
    for k,Y in enumerate(XX[:-1]):
        M[k+1]=M[k]+h/6.0*(DDF(Y)+4.0*DDF(Y+0.5*h)+DDF(Y+h))
    m=p.linspace(0,M[-1],len(X))
    return p.interp(m,M,XX)
    


def ele(i,j,X):
    h=X[j+1]-X[j]
    if i-j==1:
        return (x-X[j])/h
    elif i-j==0:
        return (X[j+1]-x)/h
    else:
        return 0*x

def nintegrate(F,G,t):
    a=t[1]
    b=t[2]
    X=p.linspace(a,b,21)
    out=0
    for k in range(len(X)-1):
        out+=(X[k+1]-X[k])*0.5*(F.evalf(subs={x:X[k]})*G(X[k])+F.evalf(subs={x:X[k+1]})*G(X[k+1]))
    return out



def enint(a,b,X):
    out=0.0
    for i in range(len(X)-1):
        if a[i]==0 or b[i]==0:
            continue
        else:
            out+=nintegrate(a[i],b[i],(x,X[i],X[i+1]))
    return out

def eint(a,b,X):
    out=0.0
    for i in range(len(X)-1):
        if a[i]==0 or b[i]==0:
            continue
        else:
            out+=s.integrate(a[i]*b[i],(x,X[i],X[i+1]))
    return out

def project(f,X):
#    N=len(X)-1
#    G=[g for k in p.zeros(N)]
#    A=s.Matrix(N+1,N,lambda i,j:ele(i,j,X))
#    M=s.Matrix(N+1,N+1, lambda i,j:eint(A[i,:],A[j,:],X))
#    F=s.Matrix(N+1,1,lambda i,j:enint(A[i,:],G,X))
#    return p.array(map(float,M.inv()*F))

    return p.array([f.subs(x,a).evalf() for a in X])

    



def do(f,XX):
    return p.array(map(float,[f.evalf(subs={x:X}) for X in XX]))

f=s.sin(2*s.pi*x)+2*s.cos(2*s.pi*x)+s.exp(-(x-0.3)**2)+2
g=lambda X:f.evalf(subs={x:X})




X=p.linspace(0,1,201)
X0=p.linspace(0,1,7)
X1=adapt(f,X0)
X2=p.concatenate((X0[0:2],(0.5*(X0[1]+X0[2]),),(X0[2],),(0.5*(X0[2]+X0[3]),),
            (X0[3],),(0.5*(X0[3]+X0[4]),),X0[4:]))
D2=[1,2,2,2,1,1]

F0=project(f,X0)
F1=project(f,X1)
F2=project(f,X2)


def myPlot(X,fun,X0,funp,c1,c2):
    p.figure(figsize=(10,6))
    F=do(f,X)
    p.plot(X0,funp,c1+'o-',lw=2,)
    p.vlines(X0,0,funp,linestyle='dotted')
    p.hlines(0,0,1)
    p.xticks(X0,['$x_{%s}$'%i for i in range(len(X0))],fontsize='large')
    p.yticks([])
    p.ylabel('$f(x)$',fontsize='large')
    p.axis([X0[0],X0[-1],0,F.max()+0.1])

def myPlot2(X,fun,X0,funp,D,c1,c2):
    p.figure(figsize=(10,6))
    F=do(f,X)
    d=0
    dr=[0]
    for DD in D:
        if DD==1:
            p.plot(X0[d:d+2],funp[d:d+2],c1+'o-',lw=2,)
        elif DD==2:
            yr=p.linspace(0,1,100)
            xr=X0[d]+(X0[d+2]-X0[d])*yr
            fr=funp[d]+(funp[d+1]-funp[d])*(4.*yr*(1.0-yr))+2.0*(funp[d+2]-funp[d])*yr*(yr-0.5)
            p.plot(X0[d],funp[d],c1+'o',lw=2,)
            p.plot(xr,fr,c1+'-',lw=2,)
            p.plot(X0[d],funp[d],c1+'o-',lw=2,)
        dr.append(dr[-1]+DD)
        d=d+DD
    p.hlines(0,0,1)
    p.vlines(X0[dr],0,funp[dr],linestyle='dotted')
    p.xticks(X0[dr],['$x_{%s}$'%i for i in range(len(X0[dr]))],fontsize='large')
    p.yticks([])
    p.ylabel('$f(x)$',fontsize='large')
    p.axis([X0[0],X0[-1],0,F.max()+0.1])


myPlot(X,f,X0,F0,'k','c')
p.savefig('adapt_0.png')
myPlot(X,f,X1,F1,'b','y')
p.savefig('adapt_r1.png')
myPlot(X,f,X2,F2,'b','y')
p.savefig('adapt_h1.png')
myPlot2(X,f,X2,F2,D2,'b','y')
p.savefig('adapt_p1.png')

