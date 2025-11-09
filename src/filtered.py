# =======================================================
# Arquivo: filtragem_ecg.py
# =======================================================

import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfiltfilt

# ======== 1. Leitura do arquivo com o sinal ========
df = pd.read_csv("../data/ecg_100_physical.csv")

# ======== 2. Função para criar o filtro passa-banda ========
def butter_bandpass_sos(lowcut, highcut, fs, order=3):
    """
    Cria um filtro passa-banda Butterworth no formato SOS (Second-Order Sections).
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    sos = butter(order, [low, high], btype='band', output='sos')
    return sos

# ======== 3. Configurações do filtro ========
lowcut = 0.5    # Hz
highcut = 40    # Hz
order = 3
fs = 360        # taxa de amostragem do MIT-BIH (ajuste conforme seu sinal)

# ======== 4. Aplicar o filtro ========
sos = butter_bandpass_sos(lowcut, highcut, fs, order)
df['ecg_filtrado'] = sosfiltfilt(sos, df['V5'])

# ======== 5. Selecionar um intervalo para zoom ========
indice_inicial = 10000
indice_final = 11000
ecg_zoom = df.iloc[indice_inicial:indice_final]

# ======== 6. Plot 1: Sinal físico (original) ========
plt.figure(figsize=(8, 4))
plt.plot(ecg_zoom['Time_s'], ecg_zoom['V5'], color='gray')
plt.title(f"ECG Físico - Seção ampliada ({df['Time_s'].iloc[indice_inicial]:.2f}s - {df['Time_s'].iloc[indice_final]:.2f}s)")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (mV)')
plt.grid(True)
plt.show()

# ======== 7. Plot 2: Sinal filtrado ========
plt.figure(figsize=(8, 4))
plt.plot(ecg_zoom['Time_s'], ecg_zoom['ecg_filtrado'], color='blue')
plt.title(f"ECG Filtrado - Seção ampliada ({df['Time_s'].iloc[indice_inicial]:.2f}s - {df['Time_s'].iloc[indice_final]:.2f}s)")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (mV)')
plt.grid(True)
plt.show()

# ======== 8. Plot 3: Comparação entre original e filtrado ========
plt.figure(figsize=(10, 4))
plt.plot(ecg_zoom['Time_s'], ecg_zoom['V5'], label='ECG Físico', color='gray', alpha=0.7)
plt.plot(ecg_zoom['Time_s'], ecg_zoom['ecg_filtrado'], label='ECG Filtrado', color='orange')
plt.title(f"Comparação: ECG Físico vs Filtrado ({df['Time_s'].iloc[indice_inicial]:.2f}s - {df['Time_s'].iloc[indice_final]:.2f}s)")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (mV)')
plt.legend()
plt.grid(True)
plt.show()

