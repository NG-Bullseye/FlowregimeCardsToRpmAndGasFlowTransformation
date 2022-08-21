import random
import scipy
import numpy as np
import math
import matplotlib.pyplot as plt

g = 9.81# erbeschleunigung
D = 0.1# meter reaktor durchmesser innen
m=15.68627450980392
n=0.1686274509803922
def getFrOfDispToTransFromFl(Fl, margin=0):
    fr = np.power(10,(m*(np.power(10,Fl-margin))+n))

    return fr
maximumDisp = {
    "FrChart": 2,#np.power(1000 * 60, 2) * D / g,
    "FlChart": 1 ,#150 / (1000 * np.power(D, 3) * 60000)
    "FrBig": 2,
    "FlBig": 1}
minimumDisp = {
    "FrChart": 0.2, #np.power(100*60, 2)*D/g,
    "FlChart": 0.002}#10/(100*np.power(D, 3)*60000)
def getRpm(Fr):
    return np.sqrt(Fr*g/D)*60 #N*60=rpm
def getGasflow(Fl,Fr):
    return Fl * np.sqrt(Fr*g/D)*D*D*D*60000 #VS= Q*60000





FlDisp=np.linspace(minimumDisp.get("FlChart"),maximumDisp.get("FlBig"))
FrDisp=getFrOfDispToTransFromFl(FlDisp)
xRpmDisp=getRpm(FrDisp)
yvsDisp=getGasflow(FlDisp,FrDisp)
plt.plot(FlDisp,FrDisp,color='g')
plt.show()
exit(0)

