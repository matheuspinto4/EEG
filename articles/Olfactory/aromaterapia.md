# Análise da Eficácia da Aromaterapia Usando EEG

##  1. Desenho Experimental Básico

**Objetivo**: Avaliar se certos aromas alteram padrões de EEG associados a relaxamento, atenção ou estresse.

- **Grupos**:
  - Controle (sem aroma ou aroma neutro)
  - Experimental (lavanda, hortelã, alecrim etc.)

- **Tarefa**:
  - Repouso com olhos fechados
  - Tarefas cognitivas leves (ex: Stroop)
  - Assistir a vídeos emocionais/neutros

- **Momentos de Medição**:
  - Pré-aroma (baseline)
  - Durante o estímulo aromático
  - Pós-aroma

---

##  2. Métricas EEG a Serem Exploradas

### a) Power Spectral Density (PSD)
Análise das principais bandas cerebrais:

- **Delta (0.5–4 Hz)**: Relaxamento profundo, sonolência
- **Theta (4–8 Hz)**: Calmaria, foco interno
- **Alfa (8–12 Hz)**: Relaxamento, fechamento dos olhos
- **Beta (13–30 Hz)**: Alerta, atenção
- **Gama (>30 Hz)**: Processamento cognitivo complexo

### b) Índices Combinados

- **Índice de Relaxamento**: Alfa / Beta
- **Índice de Engajamento Cognitivo**: (Beta + Gama) / (Alfa + Theta)

---

## 3. Abordagens Analíticas

### a) Estatística Tradicional

- **Testes t** para comparações entre dois momentos
- **ANOVA** para múltiplas condições e momentos

### b) Machine Learning

- Treinar classificadores (SVM, Random Forest etc.) para distinguir EEG com e sem aroma
- Usar **PCA** para redução de dimensionalidade antes do treino

### c) Análise de Conectividade Cerebral

- **Coerência** ou **correlação cruzada** entre eletrodos
- Verificar alterações em redes neurais funcionais (ex: DMN ou rede de atenção)

---

##  4. Protocolos Sugeridos por Aroma

###  Lavanda
- **Expectativa**: Aumento de Alfa → Relaxamento
- **Tarefa**: Repouso com olhos fechados

### Alecrim
- **Expectativa**: Aumento de Beta → Atenção
- **Tarefa**: Teste de atenção sustentada (ex: Stroop)

###  Hortelã
- **Expectativa**: Estímulo leve, foco
- **Tarefa**: Tarefas de reação simples

---

## 5. Outras Ideias Complementares

- Aplicar **questionários subjetivos** (ex: escala de estresse, foco, bem-estar)
- Medir **variabilidade da frequência cardíaca (HRV)** junto do EEG
- Realizar testes em **diferentes horários do dia** para observar efeitos do ritmo circadiano

