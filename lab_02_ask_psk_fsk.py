# ask_psk_fsk.py
import numpy as np
import matplotlib.pyplot as plt

data = input("Enter binary data (e.g., 1010101): ")

bit_duration = 1
sampling_rate = 1000
t = np.linspace(0, bit_duration, int(sampling_rate * bit_duration), endpoint=False)

f1 = 5
f2 = 10

fc = 10
A1 = 1
A0 = 0.3

ask_signal = []
psk_signal = []
fsk_signal = []
bit_waveform = []

for bit in data:
    # Bit waveform (rectangular pulse: 1 or 0)
    bit_waveform.extend([int(bit)] * len(t))

    # ASK
    ask = (A1 if bit == '1' else A0) * np.sin(2 * np.pi * fc * t)
    ask_signal.extend(ask)

    # FSK
    freq = f2 if bit == '1' else f1
    fsk = np.sin(2 * np.pi * freq * t)
    fsk_signal.extend(fsk)

    # BPSK (2-PSK)
    phase = 0 if bit == '1' else np.pi
    psk = np.sin(2 * np.pi * fc * t + phase)
    psk_signal.extend(psk)

# Time axis
total_time = np.linspace(0, len(data) * bit_duration, len(data) * len(t), endpoint=False)

# Plotting
plt.figure(figsize=(12, 12))

plt.subplot(4, 1, 1)
plt.title("Input Bit Waveform")
plt.plot(total_time, bit_waveform, drawstyle="steps-pre")
plt.ylim(-0.5, 1.5)
plt.grid(True)

plt.subplot(4, 1, 2)
plt.title("Amplitude Shift Keying (ASK)")
plt.plot(total_time, ask_signal)
plt.grid(True)

plt.subplot(4, 1, 3)
plt.title("Phase Shift Keying (BPSK / 2-PSK)")
plt.plot(total_time, psk_signal)
plt.grid(True)

plt.subplot(4, 1, 4)
plt.title("Frequency Shift Keying (FSK)")
plt.plot(total_time, fsk_signal)
plt.grid(True)

plt.tight_layout()
plt.show()