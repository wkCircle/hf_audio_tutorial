import numpy as np

def generate_example_signal(dur=1, Fs=100):
    """Generate example signal

    Notebook: PCP_08_signal.ipynb

    Args:
        dur: Duration (in seconds) of signal (Default value = 1)
        Fs: Sampling rate (in samples per second) (Default value = 100)

    Returns:
        x: Signal
        t: Time axis (in seconds)
    """
    N = int(Fs * dur)
    t = np.arange(N) / Fs
    # superimpose 3 different sine waves with different amplitudes
    x = 1 * np.sin(2 * np.pi * (1.9 * t - 0.3))
    x += 0.5 * np.sin(2 * np.pi * (6.1 * t - 0.1))
    x += 0.1 * np.sin(2 * np.pi * (20 * t - 0.2))
    return x, t



def generate_sinusoid(dur=1, amp=1, freq=1, phase=0, Fs=100):
    """Generation of sinusoid

    Notebook: PCP_08_signal.ipynb

    Args:
        dur: Duration (in seconds) of sinusoid (Default value = 1)
        amp: Amplitude of sinusoid (Default value = 1)
        freq: Frequency (in Hertz) of sinusoid (Default value = 1)
        phase: Phase (relative to interval [0,1)) of sinusoid (Default value = 0)
        Fs: Sampling rate (in samples per second) (Default value = 100)

    Returns:
        x: Signal
        t: Time axis (in seconds)
    """
    num_samples = int(Fs * dur)
    t = np.arange(num_samples) / Fs
    x = amp * np.sin(2 * np.pi * (freq * t - phase))
    return x, t
