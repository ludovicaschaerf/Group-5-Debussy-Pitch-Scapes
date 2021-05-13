from wavescapes import *
import numpy as np 

dic = {0:'pentatonic scale', 1:'diatonic scale'}

orig_coeffs = [[0.054, 0.2, 0.2, 0.2, 0.75, 0.2],
               [0.038, 0.14, 0.14, 0.14, 0.53, 0.14]]

def predict_penta_dia(score, hor_ratio=(0,1), ver_ratio=1, aw_size=4):
    ''' Function that takes the filepath of a MIDI file, the height range (how high up the triangle)
        and the horizontal range (how far into the piece), where 0 is the beginnning and 1 is the end, 
        and finds the most fitting scale/chord for that range of that piece based on how similar the 
        DFT is to the coefficients identified by Cédric 
    '''
    coeffs = []
    
    arr1 = produce_pitch_class_matrix_from_filename(score, aw_size=aw_size)
    utm = np.abs(apply_dft_to_pitch_class_matrix(arr1))
    for i in range(utm.shape[0]):
        utm[i,:,:][utm[i,:,:] == 0] = np.nan  
    sel = utm[int(utm.shape[0] * ver_ratio)-1, int(utm.shape[1] * hor_ratio[0]):int(utm.shape[1] * hor_ratio[1]),:]
    coeffs = np.nanmean(sel, axis=0)[1:] / np.nanmean(sel, axis=0)[0]
    sim = []
    #print('the most resonant coefficient is: ', np.argmax(coeffs) + 1)
    for scale in orig_coeffs:
        norm1 = np.linalg.norm(coeffs)
        norm2 = np.linalg.norm(np.array(scale))
        sim_ = np.abs(coeffs - np.array(scale))
        sim.append(np.sum(sim_))
    #print(score, 'is a', dic[np.argmin(sim)])
    return np.argmax(coeffs) + 1, dic[np.argmin(sim)], coeffs