import os
import matplotlib.pyplot as plt
import numpy as np
import math

def sign (a):
    if a>0:
        return 1
    elif a==0:
        return 0
    else:
        return -1


class Point:
    def __init__(self,x_1,x_2):
        self.x_1 = x_1
        self.x_2 = x_2

    def __repr__(self):
        return '({} ,{})'.format(self.x_1,self.x_2)
    def __sub__(self,other):
        result = Point(self.x_1-other.x_1,self.x_2-other.x_2)
        return result
    def size (self):
        sz = math.sqrt(self.x_1**2 + self.x_2**2)
        return sz

class Position(Point):
    def __init__(self,x_1,x_2,gamma):
        self.x_1 = x_1
        self.x_2 = x_2
        self.gamma = gamma

class Vector(Point):
    def __init__(self,vect):
        self.x_1 = vect.x_1
        self.x_2 = vect.x_2



def circlePiont(point, R,u ):
    z = Point(point.x_1-sign(u)*R*math.sin(point.gamma),point.x_2+sign(u)*R*math.cos(point.gamma))
    return z;

def pairingPoint(point,R,phi):
    z=Point(point.x_1 + R*math.cos(phi),point.x_2 + R*math.sin(phi))
    return z

def anglePhi_1(vector,R,u):
    phi = vector.size() -sign(u)*math.acos(R/vector.size())
    return phi

def anglePhi_2(vector,R,u):
    phi = vector.size() +sign(u)*math.acos((3*R**2+vector.size()**2)/(4*R*vector.size()))
    return phi

def anglePhi_3(vector,R,u):
    phi = vector.size() - sign(u)*math.acos((3*R**2+vector.size()**2)/(4*R*vector.size()))
    return phi


def modAngle(angle):
    angle=math.fabs(angle)
    while angle>=2*math.pi:
        angle-=2*math.pi
    return angle

def tTraject1(self,R,u):

        Z=circlePiont(point=self.start,R=R,u=u)

        vector=Vector(self.end - Z)
        phi = anglePhi_1(vector=vector,R=R,u=u)
        Y=pairingPoint(point=Z,R=R,phi=phi)
        vectZY = Vector(Y-Z)
        vectX_oZ = Vector(Z-self.start)
        angleXZY = math.atan2(vectZY.x_2 - vectX_oZ.x_2,vectZY.x_1 - vectX_oZ.x_1)
        angleXZY = modAngle(angleXZY)
        vectYX_t = Vector(self.end-Y)
        T=angleXZY+vectYX_t.size()
        list_T = [T,'D',angleXZY,'O',Y,u]
        #print(list_T)
        return list_T


def tTraject2(self,R,u):

        Z=circlePiont(point=self.start,R=R,u=u)
        Z2=circlePiont(point=self.start,R=R,u=-u)
        vector=Vector(self.end - Z)
        phi = anglePhi_2(vector=vector,R=R,u=u)
        Y=pairingPoint(point=Z,R=R,phi=phi)
        vectZY = Vector(Y-Z)
        vectX_oZ = Vector(Z-self.start)
        angleXZY = math.atan2(vectZY.x_2 - vectX_oZ.x_2,vectZY.x_1 - vectX_oZ.x_1)
        angleXZY = modAngle(angleXZY)
        vectX_tZ2=Vector(self.end - Z2)
        vectZY2 = Vector(Y-Z2)
        angleYZX_t = math.atan2(vectX_tZ2.x_2-vectZY2.x_2,vectX_tZ2.x_2-vectZY2.x_2)
        angleYZX_t = modAngle(angleYZX_t)
        T=angleXZY+angleYZX_t
        list_T = [T,'D',angleXZY,'D',Y,angleYZX_t,u]
        #print(list_T)
        return list_T


def tTraject3(self,R,u):

        Z=circlePiont(point=self.start,R=R,u=u)
        Z2=circlePiont(point=self.start,R=R,u=-u)
        vector=Vector(self.end - Z)
        phi = anglePhi_3(vector=vector,R=R,u=u)
        Y=pairingPoint(point=Z,R=R,phi=phi)
        vectZY = Vector(Y-Z)
        vectX_oZ = Vector(Z-self.start)
        angleXZY = math.atan2(vectZY.x_2 - vectX_oZ.x_2,vectZY.x_1 - vectX_oZ.x_1)
        angleXZY = modAngle(angleXZY)
        vectX_tZ2=Vector(self.end - Z2)
        vectZY2 = Vector(Y-Z2)
        angleYZX_t = math.atan2(vectX_tZ2.x_2-vectZY2.x_2,vectX_tZ2.x_2-vectZY2.x_2)
        angleYZX_t = modAngle(angleYZX_t)
        T=angleXZY+angleYZX_t
        list_T = [T,'D',angleXZY,'D',Y,angleYZX_t,u]
        #print(list_T)
        return list_T



class Trajectory():
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.R=1
        self.traject()

    def traject(self):

        T=[]
        for step in [1,2,3]:
            promT=[]
            if step==1:
                tlist1 = tTraject1(self=self,R=self.R,u=1)

                tlist2 = tTraject1(self=self,R=self.R,u=-1)
                promT=tlist2[:]
                if tlist1[0]<tlist2[0]:
                    promT=tlist1[:]
            if step ==2:
                tlist1 = tTraject2(self=self,R=self.R,u=1)
                tlist2 = tTraject2(self=self,R=self.R,u=-1)
                promT=tlist2[:]
                if tlist1[0]<tlist2[0]:
                    promT=tlist1[:]
            if step ==3:
                tlist1 = tTraject3(self=self,R=self.R,u=1)
                tlist2 = tTraject2(self=self,R=self.R,u=-1)
                promT=tlist2[:]
                if tlist1[0]<tlist2[0]:
                    promT=tlist1[:]

            if len(T)==0:

                T=promT[:]
            else:
                if( promT[0]>promT[0]):
                    T=promT[:]
        #print(T)
        self.T = T[:]


def main():
    start = Position(0,0,0)
    end = Position(1,1,math.pi/2)
    traject =Trajectory(start,end)
    print (traject.T)


if __name__ == '__main__':
    main()
