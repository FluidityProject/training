from PIL import Image
import pylab as p


# This should work for any photo, but greyscale is probably better
F=Image.open('MDP.jpg').convert('L')
arr=p.flipud(p.array(F))

NY,NX=arr.shape
x=p.arange(NX)
y=p.arange(NY)

p.gray()

X,Y=p.meshgrid(x,y)



def plot(sx,sy,n,**kwargs):

    print range(*sx.indices(NX))

    arr_n=p.array([[p.mean(arr[x:x+n,y:y+n]) for x in range(*sx.indices(NY))]
                   for y in range(*sy.indices(NX))])

    print arr_n

    p.pcolormesh(X[sx,sy],Y[sx,sy],arr_n.T,vmin=0,vmax=255,**kwargs)


# offsets to make specifying the "refined" areas easier

ym1=3
xm1=5

def ml(a,b,c):
    return [(r,c) for r in range(a,b)]

# set up the various levels

M1=(ml(1,6,0)+
    ml(0,7,1)+
    ml(-1,8,2)+
    ml(-1,9,3)+
    ml(-1,8,4)+
    ml(-1,7,5)+
    ml(0,7,6)+
    ml(0,6,7))

M2=(ml(2,12,2)+
    ml(1,12,3)+
    ml(-0,13,4)+
    ml(-1,14,5)+
    ml(-2,15,6)+
    ml(-2,15,7)+
    ml(-2,14,8)+
    ml(-2,13,9)+
    ml(-1,12,10)+
    ml(-1,12,11)+
    ml(-1,12,12)+
    ml(-1,11,13))

M3=(ml(5,18,5)+
    ml(4,20,6)+
    ml(3,20,7)+
    ml(2,21,8)+
    ml(1,22,9)+
    ml(0,22,10)+
    ml(0,22,11)+
    ml(0,22,12)+
    ml(-1,22,13)+
    ml(-2,22,14)+
    ml(-2,21,15)+
    ml(-1,21,16)+
    ml(0,21,17)+
    ml(0,20,18)+
    ml(1,20,19)+
    ml(2,20,20)+
    ml(2,19,21)+
    ml(2,18,22)+
    ml(2,18,23)+
    ml(2,15,24))
    

for k in range(5):

    p.figure(figsize=(10,6))
    p.clf()
    p.hold(True)
    p.axes([0.05,0.05,0.45,0.95])
    p.axis('off')
    p.axis([0,NY,0,NY])
    plot(slice(0,NY,16),slice(0,NX,16),16,edgecolor='k')


    if (k>0):
        
        for i,j in M1:
            plot(slice(xm1*16+i*16,xm1*16+(i+1)*16+1,8),
                 slice(ym1*16+j*16,ym1*16+(j+1)*16+1,8),8,edgecolor='r')

        if (k>1):
            for i,j in M2:
                plot(slice(xm1*16+i*8,xm1*16+(i+1)*8+1,4),
                     slice(ym1*16+j*8,ym1*16+(j+1)*8+1,4),4,edgecolor='b')

            if (k>2):
                for i,j in M3:
                    plot(slice(xm1*16+i*4,xm1*16+(i+1)*4+1,2),
                         slice(ym1*16+j*4,ym1*16+(j+1)*4+1,2),2,edgecolor='y')



    p.axes([0.55,0.05,0.45,0.95])
    p.axis('off')
    p.axis([0,NY,0,NY])

    if (k<4):
        plot(slice(0,NY,16),slice(0,NX,16),16)
        if (k>0):
            for i,j in M1:
                plot(slice(xm1*16+i*16,xm1*16+(i+1)*16+1,8),
                     slice(ym1*16+j*16,ym1*16+(j+1)*16+1,8),8)
            if (k>1):
                for i,j in M2:
                    plot(slice(xm1*16+i*8,xm1*16+(i+1)*8+1,4),
                         slice(ym1*16+j*8,ym1*16+(j+1)*8+1,4),4)
                if(k>2):
                    for i,j in M3:
                        plot(slice(xm1*16+i*4,xm1*16+(i+1)*4+1,1),
                             slice(ym1*16+j*4,ym1*16+(j+1)*4+1,1),1)
    else:
        plot(slice(0,16*(NY/16),1),slice(0,16*(NX/16),1),1)


    p.savefig('MDP_%02d.png'%k)
        



            



