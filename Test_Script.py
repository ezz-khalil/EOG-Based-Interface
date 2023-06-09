import pickle
from tkinter.filedialog import LoadFileDialog
import numpy as np
import os
import pandas as pd
from helper import strToNp
from preprocess import Preprocess
from sklearn.preprocessing import StandardScaler
from FeatureExtraction import FeatureExtraction


class TestMethods:
    def __init__(self):
        self.data_csv = "test_combined_dataset.csv"
        self.dataset = "combined dataset"
        self.preprocess = Preprocess()
        self.featureExtraction = FeatureExtraction()

    def LoadFromPickle(self, pickleFile):
        with open(pickleFile, "rb") as file:
            object = pickle.load(file)
        return object

    def SVM_with_Wavelets_Features(self, signal):
        model = self.LoadFromPickle("svm_model_Wavelet.pkl")
        EOG_SIGNAL = np.loadtxt(os.path.join(self.dataset, signal))
        EOG_SIGNAL = self.preprocess.fullPreprocess(EOG_SIGNAL)
        EOG_SIGNAL = np.array(
            self.featureExtraction.extract_wavelet_features(EOG_SIGNAL)
        )
        EOG_SIGNAL = EOG_SIGNAL.reshape(len(EOG_SIGNAL), -1)
        scaler = self.LoadFromPickle("scaler_Wavelet.pkl")
        EOG_SIGNAL = scaler.transform(EOG_SIGNAL)
        PredicatedMove = model.predict(EOG_SIGNAL)
        return PredicatedMove

    def RF_with_Wavelets_Features(self, signal):
        model = self.LoadFromPickle("rf_model_Wavelet.pkl")
        EOG_SIGNAL = np.loadtxt(os.path.join(self.dataset, signal))
        EOG_SIGNAL = self.preprocess.fullPreprocess(EOG_SIGNAL)
        EOG_SIGNAL = np.array(
            self.featureExtraction.extract_wavelet_features(EOG_SIGNAL)
        )
        EOG_SIGNAL = EOG_SIGNAL.reshape(len(EOG_SIGNAL), -1)
        scaler = self.LoadFromPickle("scaler_Wavelet.pkl")
        EOG_SIGNAL = scaler.transform(EOG_SIGNAL)
        PredicatedMove = model.predict(EOG_SIGNAL)
        return PredicatedMove

    def SVM_with_PSD_Features(self, signal):
        model = self.LoadFromPickle("svm_model_PSD.pkl")
        EOG_SIGNAL = np.loadtxt(os.path.join(self.dataset, signal))
        EOG_SIGNAL = self.preprocess.fullPreprocess(EOG_SIGNAL)
        EOG_SIGNAL = np.array(self.featureExtraction.extract_psd_features(EOG_SIGNAL))
        EOG_SIGNAL = EOG_SIGNAL.reshape(1, -1)
        scaler = self.LoadFromPickle("scaler_PSD.pkl")
        EOG_SIGNAL = scaler.transform(EOG_SIGNAL)
        PredicatedMove = model.predict(EOG_SIGNAL)
        return PredicatedMove

    def RF_with_PSD_Features(self, signal):
        model = self.LoadFromPickle("rf_model_PSD.pkl")
        EOG_SIGNAL = np.loadtxt(os.path.join(self.dataset, signal))
        EOG_SIGNAL = self.preprocess.fullPreprocess(EOG_SIGNAL)
        EOG_SIGNAL = np.array(self.featureExtraction.extract_psd_features(EOG_SIGNAL))
        EOG_SIGNAL = EOG_SIGNAL.reshape(1, -1)
        scaler = self.LoadFromPickle("scaler_PSD.pkl")
        EOG_SIGNAL = scaler.transform(EOG_SIGNAL)
        PredicatedMove = model.predict(EOG_SIGNAL)
        return PredicatedMove


Test = TestMethods()
print(Test.SVM_with_PSD_Features("yukari1.txt"))
print(Test.RF_with_PSD_Features("yukari1.txt"))
