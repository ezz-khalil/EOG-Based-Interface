import numpy as np
from scipy import signal


class Preprocess:
    def __init__(self, fs=1000):
        self.fs = fs

    def filter_eog_signal(self, eog_signal, f_low=0.1, f_high=30, order=4):
        b, a = signal.butter(
            order, [f_low / (self.fs / 2), f_high / (self.fs / 2)], btype="band"
        )

        filtered_signal = signal.filtfilt(b, a, eog_signal, axis=0)

        return filtered_signal

    def resample(self, eog_signal, new_fs):
        resampling_factor = new_fs / self.fs

        resampled_signal = signal.resample(
            eog_signal, int(len(eog_signal) * resampling_factor), axis=0
        )

        return resampled_signal

    def remove_baseline(self, eog_signal, baseline_window=10):
        baseline = np.mean(eog_signal[: int(self.fs * baseline_window), :], axis=0)

        baseline_corrected_signal = eog_signal - baseline

        return baseline_corrected_signal

    def remove_artifacts(self, eog_signal, artifact_threshold=75):
        diff_signal = np.abs(np.diff(eog_signal, axis=0))
        mad = np.median(diff_signal)
        artifact_segments = np.where(diff_signal > artifact_threshold * mad)[0]
        artifact_removed_signal = np.copy(eog_signal)

        for i in range(len(artifact_segments) // 2):
            start = artifact_segments[i * 2]
            end = artifact_segments[i * 2 + 1]

            if end - start > 1:
                interp_func = interp1d(
                    [start - 1, end],
                    [eog_signal[start - 1], eog_signal[end]],
                    kind="cubic",
                    fill_value="extrapolate",
                )
                artifact_removed_signal[start:end, :] = interp_func(
                    np.arange(start, end)
                )[None, :]

        return artifact_removed_signal

    def fullPreprocess(self, signal, f_low=0.5, f_high=20, order=3, new_fs=100):
        filtered_signal = self.filter_eog_signal(signal, f_low, f_high, order)
        resampled_signal = self.resample(filtered_signal, new_fs)

        baseline_corrected_signal = self.remove_baseline(
            resampled_signal, baseline_window=10
        )

        artifact_removed_signal = self.remove_artifacts(
            baseline_corrected_signal, artifact_threshold=75
        )

        return artifact_removed_signal
