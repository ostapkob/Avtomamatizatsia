

from matplotlib import pylab as plt
import math

def fc(x):
    return math.sqrt(625-x**2)

x=list (range(0,26, 1))
y=[fc(i) for i in x]
x1=[-i for i in x ]
y1=[-i for i in y]
print (x, "\n", y, "\n",x1,"\n",y1)

plt.plot (x,y)
plt.plot (x1,y)
plt.plot (x,y1)
plt.plot (x1,y1)
=======================
from matplotlib import pylab as plt
import math
%matplotlib inline
mm=-100
ii=[]
while mm<200:
    mm+=0.01
    ii.append(mm)
x=[math.cos(i) for i in ii]
y=[(math.sin(i)) + math.sqrt(math.fabs(math.cos(i)))  for i in ii]
print (math.pi)
plt.plot (x,y)