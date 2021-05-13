from scipy.spatial import distance
from wavescapes import *
import numpy as np

scales={
    'CM':([1,0,1,0,1,1,0,1,0,1,0,1], [0]),
    'GM':([1,0,1,0,1,0,1,1,0,1,0,1], [0]),
    'DM':([0,1,1,0,1,0,1,1,0,1,0,1], [0]),
    'AM':([0,1,1,0,1,0,1,0,1,1,0,1], [0]),
    'EM':([0,1,0,1,1,0,1,0,1,1,0,1], [0]),
    'BM':([0,1,0,1,1,0,1,0,1,0,1,1], [0]),
    'FsM':([0,1,0,1,0,1,1,0,1,0,1,1], [0]),
    'Cs':([1,1,0,1,0,1,1,0,1,0,1,0], [0]),
    'AbM':([1,1,0,1,0,1,0,1,1,0,1,0], [0]),
    'EbM':([1,0,1,1,0,1,0,1,1,0,1,0], [0]),
    'BbM':([1,0,1,1,0,1,0,1,0,1,1,0], [0]),
    'FM':([1,0,1,0,1,1,0,1,0,1,1,0], [0]),
    
     'CPe': ([1,0,1,0,1,0,0,1,0,1,0,0], [0]),
     'GPe': ([0,0,1,0,1,0,0,1,0,1,0,1], [0]),
     'DPe': ([0,0,1,0,1,0,1,0,0,1,0,1], [0]),
     'APe': ([0,1,0,0,1,0,1,0,0,1,0,1], [0]),
     'EPe': ([0,1,0,0,1,0,1,0,1,0,0,1], [0]),
     'BPe': ([0,1,0,1,0,0,1,0,1,0,0,1], [0]),
      'FsPe': ([0,1,0,1,0,0,1,0,1,0,1,0], [0]),
      'CsPe': ([0,1,0,1,0,1,0,0,1,0,1,0], [0]),
      'AbPe': ([1,0,0,1,0,1,0,0,1,0,1,0], [0]),
      'EbPe': ([1,0,0,1,0,1,0,1,0,0,1,0], [0]),
      'BbPe': ([1,0,1,0,0,1,0,1,0,0,1,0], [0]),
     'FPe': ([1,0,1,0,0,1,0,1,0,1,0,0], [0])
}

def predict_penta_dia_2(score, aw_size=4):
    tag = {} # eg. {'CM':([1.234],[1,1,-1])}
    for key in scales.items():
        fourier_mat = apply_dft_to_pitch_class_matrix([key[1][0]])
        top_coefficients = fourier_mat[fourier_mat.shape[0]-1][fourier_mat.shape[1]-1][1:]
        phase = np.angle(top_coefficients)
        tag[key[0]] = (phase[4],[np.sign(phase[1]),np.sign(phase[3]),np.sign(phase[5])])
    

    phase5_tag = [values[0] for values in tag.values()]
    sign_tag = [values[1] for values in tag.values()]


    dia_penta = {0:"Diatonic",1:"Pentatonic"}

    candidates = [] # candidate scales for current piece
    full = produce_pitch_class_matrix_from_filename(score, aw_size=aw_size)
    fourier_mat = apply_dft_to_pitch_class_matrix(full)
    top_coefficients = fourier_mat[fourier_mat.shape[0]-1][fourier_mat.shape[1]-1][1:]
    
    phase = np.angle(top_coefficients)
    
    phase5 = phase[4]
    interested_phase_sign = np.array([np.sign(phase[1]),np.sign(phase[3]),np.sign(phase[5])])
    
    # check phase in 5th coefficient and narrow down to penta/dia
    #print(phase5, interested_phase_sign)
    ind = np.argmin(np.abs(phase5-np.array(phase5_tag)[0:12])) # index of the diatonic, +12 -> index of pentatonic
    candidates.append(distance.euclidean(interested_phase_sign, sign_tag[ind]))
    candidates.append(distance.euclidean(interested_phase_sign, sign_tag[ind+12]))
    
    if(np.argmin(candidates)==1):
        ind += 12
    
    #print(score, "is", dia_penta[np.argmin(candidates)], "and corresponding scale is", list(tag)[ind])
    return dia_penta[np.argmin(candidates)], list(tag)[ind]
