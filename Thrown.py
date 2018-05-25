import numpy as np

retList = []

def Thrown(n):
    n = n*2
    while n > 0:
        retList.append(np.random.randint(0, 500))
        n -= 1
        
    return(retList)
    
    
    