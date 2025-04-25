# Termo pesquisado: “eeg education”
## Internal Distraction Detection Utilizing EEG Data in an Educational VR Environment

### Voluntários
- 21 voluntários, sendo 7 mulheres e 12 homens
- entre 18 e 28 anos

### Processo
- Os dados foram coletados em um ambiente educacional relacionado a uma usina solar, onde complementando a experiencia do estudo, havia um avatar (representando o professor), representações, textos, audios
- uma tarefa, como contar quantas vezes o avatar mexia a mão era dada, a fim de distrair a mente do foco principal, a aula
- baseado em estudos, foram escolhidos os sensores  do lobo occipital (responsavel pelo processamento da visão), lobo parietal (responsavel pelas demandas de atenção) e o cortex pré-frotal (pensamento lógico)
- os dados foram normalizados e usados 3 métodos de machine learning (Random forest, Support Vector Machine, K Nearest Neighbors)
- os dados de 18 pessoas foram usados para treinar e de 3 foram usados para testar

### Resultado
- O KNN foi o mais eficiente chegando a pouco mais de 64% de acertividade
- também foi visto que uma janela de 20 segundos após o inicio da distração foi mais eficiente em relação a de 30

### Link
- https://dl.acm.org/doi/10.1145/3605495.3605790

