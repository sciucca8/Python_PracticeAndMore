import numpy as np 
import math

"""y = np.array([3,5,8])                # calcolo manuale della deviazione standard
media = (3+5+8) / 3
print(media)
y2 = y - media
print(y2)
y2 = y2**2
print(y2)
y2 = sum(y2)
print(y2)
result = math.sqrt(y2 / len(y))
print(result, y.std())"""

np.random.seed(6)

x = np.round(np.random.normal(size=20), 2)

"""2. Write a function which standardizes the values in a given numeric vector, i.e., rescales its elements
so that the resulting vector is of mean and standard deviation of 1. Note: this is also called “Z-score
computing”."""  

"""#print(x)
x_mean = np.mean(x)
x_std = np.std(x)
#print(x_mean, x_std)
x_norm = (x - x_mean) / x_std 
print(x_norm)
print(np.mean(x_norm), np.std(x_norm))"""

"""3. Write a function which clamps all values in a given vector to the unit interval, i.e., set all values less
than 0 to be equal to 0 and all values greater than 1 to be equal to 1."""

def clamp_vector(vector, above= 0, below= 1):
    return [max(above, min(below, i)) for i in vector]

clamped_vector = clamp_vector(x)
print(clamped_vector)


    
