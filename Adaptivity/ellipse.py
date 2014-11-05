import pylab as p

d1=1.6
d2=1

theta=p.pi/3


T=p.linspace(0,2.0*p.pi,100)
q=p.linspace(0,theta,50)
r=0.3

p.figure(figsize=[4,5])

p.plot(d1*p.cos(T)*p.cos(theta)-d2*p.sin(T)*p.sin(theta),d2*p.sin(T)*p.cos(theta)+d1*p.cos(T)*p.sin(theta),'k--',lw=2)

p.plot([0,d1*p.cos(theta)],[0,d1*p.sin(theta)],'b',lw=2)
p.plot([0,-d2*p.sin(theta)],[0,d2*p.cos(theta)],'r',lw=2)

p.plot([0,d1/2.0],[0,0],'k:')

p.plot(r*p.cos(q),r*p.sin(q),'k')

p.text((1.2*r)*p.cos(theta/2.0),(1.2*r)*p.sin(theta/2.0),
       r'$\theta$',fontsize=18)


p.text(d1/2.0*p.cos(theta)-0.1,d1/2.0*p.sin(theta)+0.2,
       r'$d_1$',fontsize=18)
p.text(-d2/2.0*p.sin(theta)-0.2,d2/2.0*p.cos(theta)-0.2,
       r'$d_2$',fontsize=18)

p.scatter(0,0,c='k',s=20,zorder=5)

p.axis('off')
p.axis('equal')
p.axis([-1.15,1.15,-1.8,1.8])

p.savefig('MetricEllipse.png')
