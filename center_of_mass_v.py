from wavescapes import *
import numpy as np

def center_of_mass_v(score, aw_size_input, coeff):
    arr1 = produce_pitch_class_matrix_from_filename(score, aw_size=aw_size_input)
    utm = np.abs(apply_dft_to_pitch_class_matrix(arr1))

    for i in range(utm.shape[0]):
        for j in range(utm.shape[0]):
            if(utm[i,j,0]!=0):
                utm[i,j] = utm[i,j]/utm[i,j,0] # normalize magnitude as in master thesis
    utm = utm[:,:,coeff]

    #ignore x axis
    utm = np.sum(utm, axis=1) #shape (N,)
    
    weight_sum = 0
    nomi = 0
    for i in range(utm.shape[0]):
        nomi += i*utm[i]
        weight_sum += utm[i]
    y = nomi/weight_sum
    
    return y/(utm.shape[0]-1)