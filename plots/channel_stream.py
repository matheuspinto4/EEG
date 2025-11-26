import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


file_path = '../data/BrainFlow-RAW_2025-10-24_15-48-34_0.csv'

brainflow_pd = pd.read_csv(file_path, sep='\t', header=None, usecols=range(0,9))

# Importações (assumindo que já as tem)
# import pandas as pd
# brainflow_pd = ... (seu DataFrame carregado)

# 1. Renomear a coluna do índice que reseta
brainflow_pd.rename(columns={0: 'Index_Reset'}, inplace=True)

# 2. Calcular a diferença entre as amostras. Onde o valor é negativo,
# é onde o reset (o 'wrap around') aconteceu.
# O .diff() calcula a diferença entre a linha atual e a linha anterior.
brainflow_pd['Index_Diff'] = brainflow_pd['Index_Reset'].diff()

# 3. Identificar os resets.
# Se o reset ocorre de 255 para 0, a diferença é -255.
# Vamos assumir que o reset é de 255 para 0, e a magnitude do salto é 256.
RESET_VALUE = 256

# Onde a diferença é negativa, crie um contador (cumulative sum) para
# registrar o número de vezes que o índice "resetou" (voltou para zero).
# Onde a diferença é < 0, atribua 1 (um reset), caso contrário 0.
brainflow_pd['Reset_Flag'] = (brainflow_pd['Index_Diff'] < 0).astype(int)

# O np.cumsum() soma cumulativamente, dando o número de vezes que o reset ocorreu
brainflow_pd['Reset_Count'] = brainflow_pd['Reset_Flag'].cumsum()

# 4. Criar o Índice Contínuo (o novo eixo X)
# Novo Índice = Índice que Reseta + (Contagem de Resets * Valor do Reset)
brainflow_pd['Index_Continuous'] = (
    brainflow_pd['Index_Reset'] + (brainflow_pd['Reset_Count'] * RESET_VALUE)
)

# 5. Criar a Coluna de Tempo (em segundos)
SAMPLING_RATE = 256 # Ajuste a taxa de amostragem do seu dispositivo BrainFlow (ex: Cyton/Daisy é 256 Hz)
brainflow_pd['Time_s'] = brainflow_pd['Index_Continuous'] / SAMPLING_RATE

print("Amostra da correção do índice:")
# Mostra o index que reseta, a contagem de resets, e o index contínuo
print(brainflow_pd[['Index_Reset', 'Reset_Count', 'Index_Continuous', 'Time_s']].tail(50))

# --- 1. Renomear Colunas (Repetindo para clareza) ---
col_names = {
    1: 'EEG_Ch1', 2: 'EEG_Ch2', 3: 'EEG_Ch3', 4: 'EEG_Ch4',
    5: 'EEG_Ch5', 6: 'EEG_Ch6', 7: 'EEG_Ch7', 8: 'EEG_Ch8'
}
brainflow_pd.rename(columns=col_names, inplace=True)
eeg_cols = list(col_names.values())

# --- 2. Transformação de Wide para Long ---
# Usando a nova coluna de tempo contínuo ('Time_s') como ID
df_long = brainflow_pd.melt(
    id_vars=['Time_s'],
    value_vars='EEG_Ch1',
    var_name='Channel',
    value_name='Voltage'
)

# --- 3. Plotagem com o Eixo X Corrigido ---
# Plotar o gráfico empilhado
g = sns.relplot(
    data=df_long,
    x='Time_s', # *** O EIXO X CORRIGIDO ***
    y='Voltage',
    row='Channel',
    kind='line',
    errorbar=None,
    legend=False
)

# Ajustar títulos e rótulos
g.set_titles("Canal: {row_name}")
g.set_axis_labels("Tempo Contínuo (s)", "Tensão ($\mu$V)")
g.fig.suptitle('Séries Temporais de Canais EEG (Índice Corrigido)', y=1.02)

plt.tight_layout()
plt.show()