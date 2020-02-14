import numpy as np
import pandas as pd

oo=pd.DataFrame(np.arange(0,10).reshape(2,5),
                 index=["x","y"],
                 columns=["p","q","r","s","t"]
                 )
print(oo)
print(oo.mean(axis=1))
a=np.arange(120).reshape(2,3,4,5)
print(a)

oo1=pd.DataFrame(np.arange(0,9).reshape(3,3),
                 index=["x","y","z"],
                 columns=["p","q","r"]
                 )
print(oo1)
print(oo1.mean(axis=1))