import numpy as np



def vec_std(vector):
    mysum = 0
    
    for x in vector:
        mysum += x
    vec_mean = mysum / len(vector)

    stand_vec = (vector - vec_mean)
    return stand_vec

stand = vec_std([-2, 4, 65, 12, 3, 7])

    
def vector_standardizer(vector):           #standardizes a vector 
    vec_mean = np.mean(vector)
    vec_std = np.std(vector)

    stand_vec = (vector - vec_mean) / vec_std 
    print(np.mean(stand_vec), np.std(stand_vec) )
    return stand_vec

ls = [-2, 4, 65, 12, 3, 7]
stand_vec = vector_standardizer(ls)
print(stand_vec)

