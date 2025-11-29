import numpy as np

a = np.array([1,2,3,4])
b = np.arange(0,10,2)         # [0,2,4,6,8]
c = np.linspace(0,1,5)        # 5 points between 0 and 1

print(a + 10)
print(b * 2)
print(np.mean(a), np.std(a))