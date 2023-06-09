import numpy as np
import pywt
import scipy


class FeatureExtraction:
    def extract_wavelet_features(self, signal, wavelet_name="db4", levels=2):
        max_len = 0
        coeffs = pywt.wavedec(signal, wavelet_name, level=levels)
        max_len = max(max_len, sum(len(c) for c in coeffs))

        features = []
        coeffs = pywt.wavedec(signal, wavelet_name, level=levels)
        padded_coeffs = []
        for c in coeffs:
            pad_len = max_len - len(c)
            if pad_len > 0:
                pad_width = ((0, pad_len),)
                c = np.pad(c, pad_width, mode="constant")
            padded_coeffs.append(c)
        features.append(np.hstack(padded_coeffs))
        return features

    def extract_psd_features(self, X, fs=100):
        features = []
        for x in X:
            f, psd = scipy.signal.periodogram(x, fs=fs, scaling="density")
            features.append(psd)
        return np.array(features)
