import numpy as np
import matplotlib.pyplot as plt
A=np.array([[0,1,0],
            [0,0,1],
            [-1,-2,-3]])
k=(np.linalg.eigvals(A)) #eigen values of A are the poles of the transfer function
print(k)
  
