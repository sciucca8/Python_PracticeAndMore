import numpy as np

np.random.seed(6)
vec = np.round(np.random.normal(size=20), 2)
print(vec)

#Create a vector y such that y[i] is equal to "small" if the corresponding x[i]<-1, "large" if x[i]>1 and "medium" otherwise.
vec2 = np.where(vec>1, "large", "small")
print(vec2)


print(vec)
new_vec1 = vec[((vec > -2) & (vec < -1)) | ((vec > 1) & (vec < 2))]                    # 1) Print all values in vec [-2,-1] U [2, 1]
new_vec1 = vec[(abs(vec) > 1) & (abs(vec) < 2)]
print(new_vec1)

pos_vec = vec[vec > 0]                                                                 # 2) Print negative values and the ratio of non-negative values in vec
neg_vec = vec[vec < 0]
print(neg_vec, len(pos_vec) / len(neg_vec))

print(np.mean(abs(vec)))                                                               # 3) Compute arithmetic mean of absolute values

stand_div = 0                                                                          # 4) Closest and furthest from 0
vec_min = np.abs(vec - stand_div).argmin()
vec_max = np.abs(vec - stand_div).argmax()
print(vec[vec_min], vec[vec_max])

new_vec2 = vec.copy()                                                                  # 5) the 3 elements that are the most distant from arithmetic mean of vec
max3_vec = []                                          
for x in range(3):
    max3_vec.append(new_vec2[np.abs(new_vec2 - np.mean(vec)).argmax()])
    new_vec2 = np.delete(new_vec2, np.abs(new_vec2 - np.mean(vec)).argmax())
print(max3_vec)

sum = 0
for x in vec:
    sum += x
print(sum / len(vec))
print(np.mean(vec))
print(np.median(vec))