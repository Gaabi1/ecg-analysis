import wfdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#-------Leitura, visualização e exportação de um sinal de ECG ---------

#Usa função wfdb.drecord para ler o registro (MIT-BIH)
record = wfdb.rdrecord('100', pn_dir='mitdb')

#Extrair sinais
signal = record.p_signal
#Pega o sinal físico (mV) em vez de digital bruto 


#Verificar dimensões e derivação
print("Formato do sinal" , signal.shape)
print("Derivações disponiveis: ", record.sig_name)


#=========Montar Data frame sinal físico e plotar gráfico ==========

#Vetor de amostras 
n_samples= signal.shape[0]
samples= np.arange(n_samples)

#Frequência de amostra
fs = record.fs
print("Frequência de amostragem: ", fs, "Hz")


df = pd.DataFrame({
    'Time_s' : samples / fs,
    'V5' : signal[:,0]
})


df.plot(
    x= 'Time_s' , 
    y='V5', 
    figsize= (10, 4), 
    title= 'ECG - mV vs Time ',
    xlabel= 'Time(s)',
    ylabel= 'Amplitude (mV)'
)

plt.show()

#Salvar CSV
df.to_csv('ecg_100_physical.csv', index= False)
print("CSV criado com sucesso!")

