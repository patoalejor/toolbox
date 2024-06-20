from scipy.signal import butter, filtfilt

# # Here, the distance function (distance and normalize arguments)
fs = 1000  # Sampling frequency (Hz)

def lowpass_filter(data, cutOff, fs, order=4):
    nyq = 0.5 * fs
    normalCutoff = cutOff / nyq
    b, a = butter(order, normalCutoff, btype='low', analog = True)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

# Design a Butterworth high-pass filter
def highpass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs  # Nyquist frequency
    normal_cutoff = cutoff / nyquist  # Normalize the frequency
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data
