import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


# Enhanced encoding functions with transition markers
def unipolar_nrz(binary_data):
    time, voltage = [], []
    for t, bit in enumerate(binary_data):
        time.extend([t, t + 1])
        voltage.extend([int(bit), int(bit)])
    return time, voltage, []


def nrz_l(binary_data):
    time, voltage, markers = [], [], []
    for t, bit in enumerate(binary_data):
        time.extend([t, t + 1])
        val = -1 if bit == '1' else 1
        voltage.extend([val, val])
        markers.append((t, val, 'red' if bit == '1' else 'blue'))
    return time, voltage, markers


def nrz_i(binary_data):
    time, voltage, markers = [], [], []
    current = 1
    for t, bit in enumerate(binary_data):
        time.extend([t, t + 1])
        if bit == '1':
            current *= -1
            markers.append((t, current, 'gold'))
        voltage.extend([current, current])
    return time, voltage, markers


def rz(binary_data):
    time, voltage, markers = [], [], []
    for t, bit in enumerate(binary_data):
        time.extend([t, t + 0.5, t + 0.5, t + 1])
        val = 1 if bit == '1' else -1
        voltage.extend([val, val, 0, 0])
        markers.append((t + 0.5, 0, 'green'))
    return time, voltage, markers


def manchester(binary_data):
    time, voltage, markers = [], [], []
    for t, bit in enumerate(binary_data):
        time.extend([t, t + 0.5, t + 0.5, t + 1])
        if bit == '1':
            voltage.extend([-1, -1, 1, 1])
        else:
            voltage.extend([1, 1, -1, -1])
        markers.append((t + 0.5, 0, 'purple'))
    return time, voltage, markers


def diff_manchester(binary_data):
    time, voltage, markers = [], [], []
    current = 1
    for t, bit in enumerate(binary_data):
        if bit == '0':
            current *= -1
            markers.append((t, current, 'orange'))
        time.extend([t, t + 0.5])
        voltage.extend([current, current])
        current *= -1
        markers.append((t + 0.5, current, 'cyan'))
        time.extend([t + 0.5, t + 1])
        voltage.extend([current, current])
    return time, voltage, markers


# Visualization setup
binary_data = "0100110"
encodings = [
    ("Unipolar NRZ", unipolar_nrz, "black"),
    ("NRZ-L (Polar)", nrz_l, "blue"),
    ("NRZ-I (Inverted)", nrz_i, "green"),
    ("RZ (Return-to-Zero)", rz, "red"),
    ("Manchester", manchester, "purple"),
    ("Diff Manchester", diff_manchester, "orange")
]

plt.figure(figsize=(16, 10))
# plt.style.use('seaborn-darkgrid')

# Create offset axes for each encoding
axes = []
for i in range(len(encodings)):
    ax = plt.subplot2grid((len(encodings), 1), (i, 0))
    axes.append(ax)

# Plot each encoding with enhanced features
for idx, (name, func, color) in enumerate(encodings):
    time, voltage, markers = func(binary_data)
    ax = axes[idx]

    # Main waveform
    ax.plot(time, voltage, drawstyle='steps-post',
            color=color, linewidth=2.5, label=name)

    # Transition markers
    for x, y, mcolor in markers:
        ax.plot(x, y, 'o', color=mcolor, markersize=8, alpha=0.7)

    # Bit indicators
    for i, bit in enumerate(binary_data):
        ax.text(i + 0.5, 1.5, bit, ha='center', va='center',
                bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round'))

    # Formatting
    ax.set_ylim(-2.2, 2.2)
    ax.set_yticks([-1, 0, 1])
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.grid(True, which='both', linestyle=':', alpha=0.7)
    ax.legend(loc='upper right', fontsize=10)

    if idx != len(encodings) - 1:
        ax.set_xticklabels([])
    else:
        ax.set_xlabel("Bit Periods", fontsize=12)

# Add clock signal at bottom
clock_ax = plt.subplot2grid((len(encodings) + 1, 1), (len(encodings), 0))
clock_time = np.linspace(0, len(binary_data), 500)
clock_signal = np.sin(2 * np.pi * 2 * clock_time)  # Double frequency
clock_ax.plot(clock_time, clock_signal, 'm-', alpha=0.7)
clock_ax.set_title("Clock Signal Reference", fontsize=10)
clock_ax.grid(True, alpha=0.3)
clock_ax.set_xticklabels([])
clock_ax.set_yticklabels([])

plt.suptitle("Comparative Analysis of Line Encoding Schemes\nBinary Data: 0100110",
             fontsize=14, y=0.98)
plt.tight_layout()
plt.subplots_adjust(hspace=0.3)
plt.show()