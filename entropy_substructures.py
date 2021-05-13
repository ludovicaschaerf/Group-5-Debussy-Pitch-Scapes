import antropy as ent
from wavescapes import *
import numpy as np
from scipy.signal import find_peaks

def compute_magnitude_entropy(score, ver_ratio=0.2, hor_ratio=(0,1), aw_size=4):
    arr1 = produce_pitch_class_matrix_from_filename(score, aw_size=aw_size)
    utm = np.abs(apply_dft_to_pitch_class_matrix(arr1))
    vec = []
    for i in range(7):
        vec.append(utm[int(utm.shape[0] * ver_ratio)-1,:,i][utm[int(utm.shape[0] * ver_ratio)-1,:,i] != 0])
    sel = np.array([ve[int(utm.shape[1] * hor_ratio[0]):int(utm.shape[1] * hor_ratio[1])] for ve in vec])
    entr = ent.spectral_entropy(sel, 1, method='fft')
    return entr[1:]

def compute_magnitude_5(score, ver_ratio=0.2, hor_ratio=(0,1), aw_size=4):
    arr1 = produce_pitch_class_matrix_from_filename(score, aw_size=aw_size)
    utm = np.abs(apply_dft_to_pitch_class_matrix(arr1))
    vec = []
    for i in range(7):
        vec.append(utm[int(utm.shape[0] * ver_ratio)-1,:,i][utm[int(utm.shape[0] * ver_ratio)-1,:,i] != 0])
    sel = [ve[int(utm.shape[1] * hor_ratio[0]):int(utm.shape[1] * hor_ratio[1])] for ve in vec]
    return sel[4]


def compute_peaks(score, ver_ratio=0.2, hor_ratio=(0,1), aw_size=4):
    arr1 = produce_pitch_class_matrix_from_filename(score, aw_size=aw_size)
    utm = np.abs(apply_dft_to_pitch_class_matrix(arr1))
    vec = []
    for i in range(7):
        vec.append(utm[int(utm.shape[0] * ver_ratio)-1,:,i][utm[int(utm.shape[0] * ver_ratio)-1,:,i] != 0])
    sel = [ve[int(utm.shape[1] * hor_ratio[0]):int(utm.shape[1] * hor_ratio[1])] for ve in vec]
    return [len(find_peaks(list(magnitudes))[0]) for magnitudes in sel]


def compute_entropy_phase(score, ver_ratio=0.2, aw_size=4):
    arr1 = produce_pitch_class_matrix_from_filename(score, aw_size=aw_size)
    utm = np.round(np.angle(apply_dft_to_pitch_class_matrix(arr1)), 2)
    vec = []
    coeffs = []
    height = int(utm.shape[0] * ver_ratio)-1
    sel = np.array(utm[height,:,:]).T
    entr = ent.spectral_entropy(sel, 1, method='fft')
    return entr[1:]