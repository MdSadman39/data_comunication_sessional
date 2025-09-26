# _am_pm_fm.py
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Signal Parameters
# -----------------------------
fs = 1000       # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)   # Time vector (1 second duration)

fc = 1000         # Carrier frequency (Hz)
fm = 10           # Message signal frequency (Hz)

Am = 1            # Amplitude of message signal
Ac = 1            # Amplitude of carrier signal

# -----------------------------
# Message Signal (sine wave)
# -----------------------------
m_t = Am * np.sin(2 * np.pi * fm * t)

# -----------------------------
# Carrier Signal
# -----------------------------
c_t = Ac * np.sin(2 * np.pi * fc * t)

# -----------------------------
# Modulation Techniques
# -----------------------------

# 1. Amplitude Modulation (AM)
ka = 0.5   # Modulation index
am_signal = (Ac + ka * m_t) * np.sin(2 * np.pi * fc * t)

# 2. Frequency Modulation (FM)
kf = 50    # Frequency sensitivity
fm_signal = Ac * np.sin(2 * np.pi * fc * t + kf * np.cumsum(m_t) / fs)

# 3. Phase Modulation (PM)
kp = np.pi/2   # Phase sensitivity
pm_signal = Ac * np.sin(2 * np.pi * fc * t + kp * m_t)

# -----------------------------
# Plotting Results
# -----------------------------
plt.figure(figsize=(10,7))

plt.subplot(4,1,1)
plt.plot(t[:1000], m_t[:1000])
plt.title("Message Signal (10 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(4,1,2)
plt.plot(t[:1000], am_signal[:1000])
plt.title("Amplitude Modulation (AM)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(4,1,3)
plt.plot(t[:1000], fm_signal[:1000])
plt.title("Frequency Modulation (FM)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(4,1,4)
plt.plot(t[:1000], pm_signal[:1000])
plt.title("Phase Modulation (PM)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()