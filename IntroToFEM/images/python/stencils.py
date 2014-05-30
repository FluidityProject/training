import sympy

import pylab as p

cmap=p.cm.coolwarm
norm=p.Normalize(vmin=-5,vmax=5)

h=sympy.var('h')

N=6

p.figure(figsize=(10,6))

R=6*20
S=(R,7*R/3)
p.subplot2grid(S,(0,0),R,R)

a=p.zeros((N+1,N))

for i in range(N):
    a[i,i]=-1

for i in range(N):
    a[i+1,i]=1


b=p.zeros((7,7),int)

for i in range(N+1):
    for j in range(N+1):
        b[i,j]=-sum(a[i,:]*a[j,:])
p.imshow(b[1:,1:],interpolation='none',aspect='equal',norm=norm,cmap=cmap)

for i in range(1,N+1):
    for j in range(1,N+1):
        p.text(i-1,j-1,'$%s$'%(sympy.latex(b[i,j]/h)),
               horizontalalignment='center',
               verticalalignment='center',fontsize='26')


p.xticks([])
p.yticks([])


v=p.axis()
p.axis('tight')


p.subplot2grid(S,(0,R+5),R,int(R/6))

Z=p.ones((N,1,3))
p.imshow(Z,aspect='equal')
for j in range(1,N+1):
        p.text(0,j-1,'$\\psi_%d$'%j,
               horizontalalignment='center',
               verticalalignment='center',fontsize='22')

p.xticks([])
p.yticks([])
p.axis('tight')


p.subplot2grid(S,(0,R+6+int(R/6)),R,int(R/6))


p.text(0,0,'$=$',
               horizontalalignment='center',
               verticalalignment='center',fontsize='22')

p.axis([-0.5,0.5,-0.5,0.5])
p.axis('off')

p.subplot2grid(S,(0,R+7+2*int(R/6)),R,int(6*R/6))
Z=p.ones((N,1,3))

strg=['$\\nicefrac{h}{3}\\hat{f}_0+\\frac{h}{6}\\hat{f}_1+\\frac{1}{h}a(0)$',
      r'$\frac{h}{6}\hat{f}_0+\frac{2h}{3}\hat{f}_1+\frac{h}{6}\hat{f}_2-\frac{1}{h}a(0)$',
      '$\\frac{h}{6}\\hat{f}_1+\\frac{2h}{3}\\hat{f}_2+\\frac{h}{6}\\hat{f}_3$',
      '$\\frac{h}{6}\\hat{f}_2+\\frac{2h}{3}\\hat{f}_3+\\frac{h}{6}\\hat{f}_4$',
      '$\\frac{h}{6}\\hat{f}_3+\\frac{2h}{3}\\hat{f}_4+\\frac{h}{6}\\hat{f}_5$',
      '$\\frac{h}{6}\\hat{f}_4+\\frac{2h}{3}\\hat{f}_5+\\frac{h}{6}\\hat{f}_6$',
      '$\\frac{h}{6}\\hat{f}_5+\\frac{h}{3}\\hat{f}_6$-b(1)',]

#strg=['$\\int_0^h (1-{x}/{h})f[x] dx$',
#      '',
#      '',
#      '',
#      '',
#      '',
#      '']

p.imshow(Z,aspect='equal')
for j in range(1,N+1):
        p.text(0,j-1,strg[j],
               horizontalalignment='center',
               verticalalignment='center',fontsize='22')
p.xticks([])
p.yticks([])
p.axis('tight')

p.savefig('FEmatrix.png')

p.figure(figsize=(10,6))
p.subplot2grid(S,(0,0),R,R)

a=p.zeros((N+1,N))

for i in range(N):
    a[i,i]=-1

for i in range(N):
    a[i+1,i]=1


b=p.zeros((7,7),int)

for i in range(N+1):
    for j in range(N+1):
        b[i,j]=-sum(a[i,:]*a[j,:])
p.imshow(b[1:,1:],interpolation='none',aspect='equal',norm=norm,cmap=cmap)


for i in range(1,N+1):
    for j in range(1,N+1):
        if b[i,j]:
            p.text(i-1,j-1,'$\\frac{%s}{%s}$'%(sympy.latex(b[i,j]),sympy.latex(h**2)),
               horizontalalignment='center',
               verticalalignment='center',
                   fontsize='26')
        else:
            p.text(i-1,j-1,'0',
                   horizontalalignment='center',
                   verticalalignment='center',
                   fontsize='26')


p.xticks([])
p.yticks([])


v=p.axis()
p.axis('tight')


p.subplot2grid(S,(0,R+5),R,int(R/6))

Z=p.ones((N,1,3))
p.imshow(Z,aspect='equal')
for j in range(1,N+1):
        p.text(0,j-1,'$\\psi_%d$'%j,
               horizontalalignment='center',
               verticalalignment='center',
               fontsize='22')

p.xticks([])
p.yticks([])
p.axis('tight')


p.subplot2grid(S,(0,R+6+int(R/6)),R,int(R/6))


p.text(0,0,'$=$',
               horizontalalignment='center',
               verticalalignment='center',)

p.axis([-0.5,0.5,-0.5,0.5])
p.axis('off')

p.subplot2grid(S,(0,R+7+2*int(R/6)),R,int(6*R/6))
Z=p.ones((N,1,3))

strg=['$\\hat{f}_1$',
      r'$\hat{f}_2-\frac{a(0)}{h^2}$',
      '$\\hat{f}_3$',
      '$\\hat{f}_4$',
      '$\\hat{f}_5$',
      '$\\hat{f}_6$',
      '$\\frac{1}{2}\\hat{f}_6$-b(1)',]

#strg=['$\\int_0^h (1-{x}/{h})f[x] dx$',
#      '',
#      '',
#      '',
#      '',
#      '',
#      '']

p.imshow(Z,aspect='equal')
for j in range(1,N+1):
        p.text(0,j-1,strg[j],
               horizontalalignment='center',
               verticalalignment='center',
               fontsize='22')
p.xticks([])
p.yticks([])
p.axis('tight')

p.savefig('FDmatrix.png')

p.figure(figsize=(10,6))

R=6*20
S=(R,7*R/3)
p.subplot2grid(S,(0,0),R,R)

a=p.zeros((N+1,N))

for i in range(N):
    a[i,i]=-1

for i in range(N):
    a[i+1,i]=1


b=p.zeros((7,7),int)

for i in range(N+1):
    for j in range(N+1):
        b[i,j]=-sum(a[i,:]*a[j,:])


b[1,1]=-3

p.imshow(b[1:,1:],interpolation='none',aspect='equal',norm=norm,cmap=cmap)


for i in range(1,N+1):
    for j in range(1,N+1):
        if b[i,j]:
            p.text(i-1,j-1,'$\\frac{%s}{%s}$'%(sympy.latex(b[i,j]),sympy.latex(h)),
                   horizontalalignment='center',
                   verticalalignment='center',
                   fontsize='26')
        else:
            p.text(i-1,j-1,'0',
                   horizontalalignment='center',
                   verticalalignment='center',
                   fontsize='26')


p.xticks([])
p.yticks([])


v=p.axis()
p.axis('tight')


p.subplot2grid(S,(0,R+5),R,int(R/6))

Z=p.ones((N,1,3))
p.imshow(Z,aspect='equal')
print 'One'
for j in range(1,N+1):
        p.text(0,j-1,r'$\psi_{\frac{%d}{2}}$'%(2*j-1),
               horizontalalignment='center',
               verticalalignment='center',
               fontsize='22')
        

p.xticks([])
p.yticks([])
p.axis('tight')


p.subplot2grid(S,(0,R+6+int(R/6)),R,int(R/6))


p.text(0,0,'$=$',
               horizontalalignment='center',
               verticalalignment='center',
               fontsize='22')

p.axis([-0.5,0.5,-0.5,0.5])
p.axis('off')

p.subplot2grid(S,(0,R+7+2*int(R/6)),R,int(6*R/6))
Z=p.ones((N,1,3))

strg=['',
      '$h\\hat{f}_{1/2}-2\\frac{a(0)}{h}$',
      '$h\\hat{f}_{3/2}$',
      '$h\\hat{f}_{5/2}$',
      '$h\\hat{f}_{7/2}$',
      '$h\\hat{f}_{9/2}$',
      '$h\\hat{f}_{11/2}-b(1)$',]

#strg=['$\\int_0^h (1-{x}/{h})f[x] dx$',
#      '',
#      '',
#      '',
#      '',
#      '',
#      '']

p.imshow(Z,aspect='equal')

print 'Two'

for j in range(1,N+1):
        p.text(0,j-1,strg[j],
               horizontalalignment='center',
               verticalalignment='center',
               fontsize='22')
p.xticks([])
p.yticks([])
p.axis('tight')

p.savefig('FVmatrix.png')
