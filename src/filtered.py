import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.signal import butter, sosfiltfilt


#Leitura do arquivo
df=pd.read_csv("../data/ecg_100_physical.csv")

#Confirmar qual coluna contém os valores em volts/mV.
print(df.head())
print(df.info())

#------------Função para criar filtro passa banda-----------------------------
#Cria um filtro passa-banda butterworth no formato SOS (second-Order Section)

def butter_bandpass_sos(lowcut, highcut, fs, order=3): 
    nyquist = 0.5 * fs 
    low = lowcut / nyquist 
    high = highcut / nyquist 
    sos = butter(order, [low, high], btype='band', output='sos') 
    return sos

#-------------------Configurações do filtro-------------------------------

lowcut = 0.5 # Hz 
highcut = 40 # Hz 
order = 3 
fs = 360

#-----------------Aplicando o filtro---------------------------------------

sos = butter_bandpass_sos(lowcut, highcut, fs, order)

df['ecg_filtrado'] = sosfiltfilt(sos, df['v5'])

#----------------Selecionar intervalo de zoom------------------------------

indice_inicial = 10000
indice_final   = 11000
ecg_zoom = df.iloc[indice_inicial:indice_final]

#----------------Plot: Sinal físico (original)------------------------------

