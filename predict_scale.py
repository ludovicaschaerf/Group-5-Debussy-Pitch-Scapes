def predict_scale(score, hor_ratio=(0,1), ver_ratio=(0,1)):
    ''' Function that takes the filepath of a MIDI file, the height range (how high up the triangle)
        and the horizontal range (how far into the piece), where 0 is the beginnning and 1 is the end, 
        and finds the most fitting scale/chord for that range of that piece based on how similar the 
        DFT is to the coefficients identified by Cédric 
    '''
        coeffs = []
        arr1 = produce_pitch_class_matrix_from_filename(score, aw_size=10)
        utm = np.abs(apply_dft_to_pitch_class_matrix(arr1))
        for i in range(utm.shape[0]):
            utm[i,:][utm[i,:] == 0] = np.mean(utm[i,:][utm[i,:] != 0])
        sel = utm[int(utm.shape[0] * hor_ratio[0]):
                  int(utm.shape[0] * hor_ratio[1])-1][int(utm.shape[1] * ver_ratio[0]):
                                                      int(utm.shape[1] * ver_ratio[1])-1]
        coeffs = np.mean(np.mean(sel[1:], axis=1), axis=0)[1:] / np.max(np.abs(sel))
        sim = []
        for scale in orig_coeffs:
            sim_ = np.abs(coeffs - np.array(scale))
            sim.append(np.sum(sim_))
        print(score, 'is a', dic[np.argmin(sim[1:15]) + 1])