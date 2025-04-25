import numpy as np
import matplotlib.pyplot as plt

def ideal_bandpass_kernel(lowcut, highcut, fs, num_taps):
    t = np.arange(-(num_taps // 2), num_taps // 2 + 1)  # Isso gera (num_taps + 1)
    h_low = np.sinc(2 * highcut * t / fs)
    h_high = np.sinc(2 * lowcut * t / fs)
    print(h_low)
    print()
    print(h_high)
    kernel = h_low - h_high

    window = np.hamming(len(kernel))  # <--- ALTERAÇÃO AQUI
    kernel *= window
    kernel /= np.sum(kernel)
    return kernel


# Simulando um sinal com ruído
fs = 256
t = np.linspace(0, 2, 2 * fs)
sinal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 60 * t)  # 10 Hz + ruído de 60 Hz

# Gerar o filtro FIR
kernel = ideal_bandpass_kernel(1, 40, fs, num_taps=101)

# Aplicar filtro via convolução
sinal_filtrado = np.convolve(sinal, kernel, mode='same')

# Plotar antes e depois
plt.figure(figsize=(10, 4))
plt.plot(t, sinal, label="Original")
plt.plot(t, sinal_filtrado, label="Filtrado", color='orange')
plt.legend()
plt.title("Filtro Passa-Banda FIR Manual (1-40 Hz)")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.tight_layout()
plt.show()
