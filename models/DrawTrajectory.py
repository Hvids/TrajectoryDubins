import ModelTrajectory as Tr
import os
import matplotlib.pyplot as plt
import numpy as np
import math

def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath='../templates/img'.format(name,fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name,fmt),fmt='png')
    os.chdir(pwd)

def drawArc(pointStar,phi,R,u):
    z=Tr.circlePiont(pointStar,R,u)
    plt.scatter(z.x_1,z.x_2,color = 'black')
    plt.scatter(pointStar.x_1,pointStar.x_2,color='green')
    step=1/100
    vector_ZS=Tr.Vector(pointStar - z)

    phi0 =math.atan2(vector_ZS.x_2, vector_ZS.x_1)
    print (phi0)
    print(phi)
    if u==1:

        phi +=phi0

        while phi0 <= phi:
            x=z.x_1+math.cos(phi0)
            y=z.x_2+math.sin(phi0)
            scatter1=plt.scatter(x,y,color='red',linewidth=0.01)
            phi0+=step


    elif u==-1:

        phi-=phi0
        while phi0>= phi:
            x=z.x_1+R*math.cos(phi0)
            y=z.x_2+R*math.sin(phi0)
            scatter1=plt.scatter(x,y,color='blue',linewidth=0.01)
            phi0-=step

def drawLine(pointStart,pointEnd):
    plt.plot([pointStart.x_1,pointEnd.x_1],[pointStart.x_2,pointEnd.x_2])

def drawTrajectory(start,end):
    trajectory = Tr.Trajectory(start,end)
    print (start, end, trajectory.T)
    list = trajectory.T
    if list[1]=='D':
        drawArc(start,list[2],1,list[5])
    if list[3] =='D':
        drawArc(list[4],list[5],1,list[6])

    if list[3] == 'O':

        drawLine(list[4],end)
    save("trajectory")


if __name__ == '__main__':
    start = Tr.Position(0,0,0)
    end = Tr.Position(1,1,math.pi/2)
    drawTrajectory(start,end)
    plt.show()
