# 🏦 Motor de Decisão de Crédito com Machine Learning

Projeto completo de análise e modelagem de risco de inadimplência, com aplicação prática em concessão de crédito, incluindo EDA, feature engineering, modelagem, validação, simulação financeira e interface interativa com Streamlit.

---

## 📌 Objetivo

Desenvolver um modelo capaz de prever a probabilidade de inadimplência de clientes e transformá-lo em uma ferramenta de apoio à decisão de crédito, permitindo:

- Reduzir perdas financeiras
- Automatizar aprovações de baixo risco
- Priorizar análises manuais
- Apoiar decisões estratégicas

---

## 🧠 Problema de Negócio

Instituições financeiras lidam diariamente com o desafio de equilibrar:

- Aprovar clientes bons (gerar receita)
- Evitar clientes inadimplentes (reduzir prejuízo)

Uma decisão ruim pode gerar:
- **Calote direto**
- **Perda de oportunidade (cliente bom recusado)**

Este projeto propõe uma solução baseada em dados para otimizar esse processo.

---

## 📊 Etapas do Projeto

### 🔍 1. Análise Exploratória de Dados (EDA)

- Análise estatística das variáveis
- Identificação de padrões de inadimplência
- Tratamento de valores nulos
- Verificação de distribuição da variável alvo
- Análise de variáveis numéricas e categóricas

📌 Principais insights:
- Atrasos recentes e histórico de inadimplência são fortes indicadores
- Comprometimento de renda impacta diretamente o risco
- Score de crédito tem relação inversa com inadimplência

---

### ⚙️ 2. Feature Engineering

Criação de variáveis relevantes:

- `comprometimento_renda`
- `parcela_estimada`
- `parcela_renda`

📌 Objetivo: aproximar o modelo da lógica real de crédito.

---

### 🧪 3. Pré-processamento

- Padronização de variáveis numéricas (`StandardScaler`)
- Codificação de variáveis categóricas (`OneHotEncoder`)
- Pipeline completo com `ColumnTransformer`

---

### 🤖 4. Modelagem

Modelos utilizados:

- Regressão Logística (principal)
- Random Forest (comparação)

📌 Destaque:
- Uso de `class_weight='balanced'` para lidar com desbalanceamento

---

### 🎯 5. Ajuste de Threshold

Avaliação de diferentes limiares:

- 0.3 → alto recall (mais conservador)
- 0.4 → equilíbrio
- **0.5 → melhor trade-off (escolhido)**

---

### 🔁 6. Validação Cruzada

- Técnica: Stratified K-Fold
- Métricas:
  - Recall: 0.64
  - Precision: 0.28
  - F1-score: 0.39

📌 Modelo consistente e generalizável.

---

### ⭐ 7. Interpretabilidade

Análise dos coeficientes da regressão logística:

Principais fatores de risco:

- Comprometimento da renda
- Dias de atraso
- Inadimplências anteriores

📌 O modelo é explicável e alinhado com regras de negócio.

---

### 💰 8. Avaliação Financeira

Simulação baseada na matriz de confusão:

- Perda evitada: **R$ 951 mil**
- Impacto líquido: **R$ 350 mil**

📌 O modelo gera valor financeiro real.

---

### 🧠 9. Regras de Decisão

Transformação das probabilidades em ação:

- **≥ 0.65 → Negar**
- **≥ 0.40 → Revisar**
- **< 0.40 → Aprovar**

📌 Aproxima o modelo da operação real de crédito.

---

## 🖥️ Aplicação com Streamlit

Interface interativa com:

- Upload de base em lote (.csv)
- Classificação automática
- Separação por:
  - Aprovados
  - Revisar
  - Negados
- Download dos resultados
- Resumo financeiro da carteira

📌 Transforma o modelo em ferramenta prática.

---

## 📂 Estrutura do Projeto
