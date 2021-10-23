from typing import AnyStr
from numpy.core.fromnumeric import reshape
from numpy.core.numeric import Inf
from scipy import optimize as op
import numpy as np
# 首先先介绍一下numpy.array模块
a=[[1,2,3],[4,5,6],[7,8,9]]
b=np.array(a)
a[2]=1
c=np.array(a)
print(a)
print(b)
print(c)
#然后下面进行线性规划
target=np.array([15,17])
a_ub=np.array([[4,3],[2,4],[2,3]])
b_ub=np.array([150,120,140])
x1=(0,Inf)
x2=(0,Inf)
ans=op.linprog(-target,a_ub,b_ub,bounds=(x1,x2))
print(ans)