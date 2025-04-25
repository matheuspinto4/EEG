| **Banda** | **Frequência (Hz)** | **Associada a...**                  |
|----------|---------------------|-------------------------------------|
| Delta    | 0.5 – 4 Hz          | Sono profundo                       |
| Theta    | 4 – 8 Hz            | Sonolência, devaneio                |
| Alpha    | 8 – 13 Hz           | Relaxamento                         |
| Beta     | 13 – 30 Hz          | Atenção, concentração               |
| Gamma    | > 30 Hz             | Processamento cognitivo intenso     |


# **Modelo para previsão:**
- Relizar o pré-processamento dos dados:
    - Remoção de artefatos (Piscar olhos, movimentos faciais, entre outros.)
    - Filtragem das frequências 
- Talvez separar a leitura dos eletrodos em vetores:
    - Com uma taxa de amostragem de 250 Hz teríamos em 10 segundos 2500 pontos de um vetor em cada eletrodo:
- Para decidir em qual banda de frequência estamos, podemos então realizar a transformada rápida de Fourier para converter o sinal do domínio do tempo para o domínio da frequência.
-   


# **Equipamento:**
- Resetar caso railed