import numpy as np
v1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) #9D Vector
v2 = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19]) #9D Vector
# Applying dot product
#v1 = Vector 1 with 9D component 
#v2 = Vector 2 with 9D component

#Dot product implementation in 9D Vector
sum_result = 0
for i in range(len(v1)):
    sum_result = sum_result + (v1[i]*v2[i])
print(sum_result)