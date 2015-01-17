import numpy
import random
import matplotlib.pyplot as pyplot
def myplot(x,y,omega,b,iter):
    for i in range(x.shape[0]):
        if y[i]==-1:
            pyplot.plot(x[i][0],x[i][1],'mo')
        else:
            pyplot.plot(x[i][0],x[i][1],'k*')
    if (omega[1]==0.0)&(omega[0]==0.0):
        return
    elif omega[1]==0:
        xline=[-b/omega[0]]*100
        yline =numpy.linspace(0,5,100)
    elif omega[0]==0:
        xline =numpy.linspace(0,5,100)
        yline=[-b/omega[1]]*100
    else:
        xline=numpy.linspace(0,5,100)
        yline=(-b-omega[0]*xline)/omega[1]
    pyplot.plot(xline,yline,'b-')
    pyplot.xlim(0,4)
    pyplot.ylim(0,4)
    pyplot.xlabel('x(1)')
    pyplot.ylabel('x(2)')
    pyplot.title('The perception example')
    pyplot.savefig('./pic/perception1/'+str(iter)+'.jpg');
    pyplot.close('all')
x=numpy.array([[0.5,1.9],[2,3],[2,2],[1,1],[1,2],[2,0.5],[3,2],[1.5,0.6],[3,1.5],[2.5,1]])
y=numpy.array([-1,1,1,-1,1,-1,1,-1,1,1])
omega=numpy.array([0,0])
b=0
eta=0.03145
errorset=[]
for i in range(x.shape[0]):
    if((x[i].dot(omega)+b)*y[i]<=0):
        errorset.append(i)
iter=0        
while len(errorset)>0:
    errornum=len(errorset)
    num=random.randrange(0,errornum)
    loc=errorset[num]
    omega =omega+eta*y[loc]*x[loc]
    b =b+eta*y[loc]
    print eta*y[loc]*x[loc],y[loc],x[loc],omega,b
    myplot(x,y,omega,b,iter)
    iter+=1
    errorset=[]
    for i in range(x.shape[0]):
        if((x[i].dot(omega)+b)*y[i]<=0):
            errorset.append(i)
            
    
    


        
    

