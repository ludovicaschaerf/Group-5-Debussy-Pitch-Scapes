from wavescapes import *
import numpy as np 

dic = {0:'single tone', 1:'tritone', 2:'major/minor triad', 3:'augmented triad', 4:'M7 chord', 5:'m7 chord',
      6:'half dim chord', 7:'dim chord', 8:'pentatonic scale', 9:'guidos hexachord', 10:'wholetone scale',
       11:'6 chromatic tones', 12:'diatonic scale', 13:'3 chromatic tritones', 14:'hexatonic scale', 
       15:'octatonic scale', 16:'all tones'}

orig_coeffs = [[1,1,1,1,1,1], [0,1,0,1,0,1], [0.17, 0.33, 0.75, 0.58, 0.64, 0.33], 
               [0,0,1,0,0,1], [0.13, 0.43, 0.71, 0.25, 0.48, 0],
               [0.18, 0, 0.5, 0.5, 0.68, 0], [0.13, 0.25, 0.35, 0.66, 0.48, 0.5],
               [0,0,0,1,0,0], [0.054, 0.2, 0.2, 0.2, 0.75, 0.2],
               [0.17, 0, 0.24, 0, 0.64, 0], [0,0,0,0,0,1],
               [0.64, 0, 0.24, 0, 0.17, 0], [0.038, 0.14, 0.14, 0.14, 0.53, 0.14],
               [0, 0.64, 0,0,0, 0.33], [0,0,0.71,0,0,0],
               [0,0,0,0.5,0,0], [0,0,0,0,0,0]]

def predict_scale(score, hor_ratio=(0,1), ver_ratio=1):
    ''' Function that takes the filepath of a MIDI file, the height range (how high up the triangle)
        and the horizontal range (how far into the piece), where 0 is the beginnning and 1 is the end, 
        and finds the most fitting scale/chord for that range of that piece based on how similar the 
        DFT is to the coefficients identified by Cédric 
    '''
    coeffs = []
    
    arr1 = produce_pitch_class_matrix_from_filename(score, aw_size=1)
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
    #print(score, 'is a', dic[np.argmin(sim[1:15]) + 1])
    return np.argmax(coeffs) + 1, dic[np.argmin(sim[1:15]) + 1], coeffs