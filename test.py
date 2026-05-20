import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
dict= {"roll":[1,2,3,4,5], "names":["a","b","c","d","e"]}
df=pd.DataFrame(dict)
print(dict)
mean=np.mean(dict["roll"])
print(mean)
x= [1,2,3,4,5,6]
y=[0,5,10,15,20,25]
plt.plot(x,y)
plt.savefig("graph.png")
print("graph saved")