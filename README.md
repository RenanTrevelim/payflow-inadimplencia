# 🏦 Previsão de Inadimplência e Motor de Decisão de Crédito

Projeto desenvolvido com foco na análise de risco de crédito e construção de um sistema capaz de **antecipar inadimplência** e **otimizar decisões financeiras na concessão de crédito**.

---

## 🎯 Objetivo do Projeto

O objetivo deste projeto é identificar os principais fatores que influenciam a inadimplência e desenvolver uma abordagem baseada em dados para **avaliar risco de crédito e apoiar decisões operacionais**.

A partir disso, busca-se:

- Entender os principais drivers de inadimplência  
- Identificar padrões de comportamento financeiro  
- Estimar a probabilidade de default  
- Apoiar decisões de crédito com base em risco  
- Maximizar retorno financeiro da carteira  

---

## 📂 Descrição da Base de Dados

O dataset contém informações financeiras e comportamentais dos clientes, utilizadas para avaliar o risco de crédito.

As variáveis podem ser agrupadas da seguinte forma:

### 👤 Perfil do Cliente
- idade  
- estado civil  
- dependentes  

### 💼 Financeiro
- renda mensal  
- valor do empréstimo  
- taxa de juros  
- valor da parcela  

### 📊 Comportamento de Crédito
- histórico de crédito  
- tempo de relacionamento  
- score de crédito  

### ⚠️ Variável Alvo
- inadimplente (0 = não, 1 = sim)  

---

## 🧠 Metodologia Utilizada

O projeto foi desenvolvido em etapas, seguindo um fluxo estruturado de análise e modelagem.

---

### 1. Entendimento do problema

Análise do contexto de concessão de crédito, com foco no desafio de reduzir perdas financeiras causadas por inadimplência sem limitar o crescimento da carteira.

---

### 2. Análise Exploratória de Dados (EDA)

Foram investigados padrões e relações entre variáveis com foco em risco financeiro.

Principais análises realizadas:

- Distribuição da inadimplência  
- Relação entre renda e risco  
- Impacto do valor do empréstimo  
- Análise da relação parcela/renda  
- Avaliação do histórico de crédito  

👉 Principais insights identificados:

- Clientes com maior comprometimento de renda apresentam maior risco  
- Valores de parcela elevados aumentam a probabilidade de inadimplência  
- Histórico de crédito é um forte indicador de comportamento futuro  
- Relação parcela/renda é um dos principais drivers de risco  

---

### 3. Definição da variável alvo

A variável alvo foi definida como:

- 1 → Cliente inadimplente  
- 0 → Cliente adimplente  

O problema foi tratado como **classificação binária**, com foco na previsão de risco.

---

### 4. Preparação dos Dados e Pipeline

Os dados passaram por etapas de pré-processamento para garantir consistência e evitar vieses:

- Tratamento de variáveis numéricas e categóricas  
- Padronização de variáveis  
- Codificação de categorias (OneHotEncoder)  
- Uso de `ColumnTransformer`  
- Separação entre treino e teste  

---

### 5. Feature Engineering

Com base nos insights do EDA, foram criadas variáveis derivadas:

- comprometimento_renda → parcela / renda  
- valor_parcela_estimado  
- indicadores de risco financeiro  

Essas features melhoram a capacidade do modelo de capturar comportamento de crédito.

---

### 6. Modelagem Preditiva

O problema foi tratado como classificação, com foco na previsão de inadimplência.

Modelo utilizado:

- Logistic Regression  

Motivação da escolha:

- Interpretabilidade  
- Estabilidade  
- Probabilidade calibrada (`predict_proba`)  

---

### 7. Avaliação do Modelo

O modelo foi avaliado considerando métricas alinhadas ao problema de crédito:

- Recall → identificar inadimplentes  
- Precision → evitar negar bons clientes  
- F1-score → equilíbrio entre erro e acerto  
- ROC-AUC → capacidade de separação  

👉 O foco principal foi reduzir falsos negativos (clientes inadimplentes aprovados).

---

### 8. Camada de Decisão

A probabilidade prevista foi convertida em decisões operacionais:

- Probabilidade ≥ 0.65 → Negar  
- 0.40 ≤ Probabilidade < 0.65 → Revisar  
- Probabilidade < 0.40 → Aprovar  

👉 Essa estratégia permite equilibrar automação com análise manual.

---

### 9. Camada de Negócio

O modelo foi traduzido em impacto financeiro da carteira:

- Valor aprovado → capital exposto  
- Valor negado → risco evitado  
- Receita estimada → retorno potencial  
- Perdas evitadas → proteção financeira  
- Custo de oportunidade → clientes bons negados  

👉 O modelo deixa de ser apenas técnico e passa a gerar valor mensurável.

---

## 📊 Resultados do Modelo

A aplicação do modelo gerou impacto financeiro relevante:

### 💰 Impacto Financeiro

- Calotes evitados: 90  
- Perda evitada: R$ 1.006.969,18  
- Prejuízo com falsos negativos: R$ 358.033,49  
- Custo de oportunidade: R$ 288.216,96  
- Impacto líquido estimado: R$ 360.718,74  

---

### 🎯 Interpretação

- O modelo evitou mais de R$ 1 milhão em perdas  
- Mesmo com erros inevitáveis, o saldo foi positivo  
- Geração líquida de valor significativa  

👉 O modelo gera impacto financeiro direto, não apenas métricas técnicas.

---

## 🖥️ Aplicação (Streamlit)

Foi desenvolvida uma aplicação interativa para uso prático.

### Funcionalidades:

- Upload de CSV  
- Previsão em lote  
- Classificação automática  
- Segmentação por risco  
- Visualização financeira  
- Download dos resultados  

👉 Interface orientada à tomada de decisão.

---

## 🏁 Conclusão

O projeto evolui de uma análise exploratória para um sistema completo de decisão em crédito.

Mais do que prever inadimplência, a solução permite:

- Reduzir perdas financeiras  
- Melhorar decisões de concessão  
- Maximizar retorno da carteira  
- Apoiar estratégias baseadas em risco  

👉 Resultado: Machine Learning aplicado diretamente à estratégia de crédito, conectando dados, risco e impacto financeiro.

---

## ▶️ Como Reproduzir os Resultados

### 1. Clone o repositório

```bash
git clone https://github.com/RenanTrevelim/payflow-inadimplencia.git
cd payflow-inadimplencia
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
#source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate    # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
streamlit run main.py
```

---

## 🐳 Como rodar com Docker

### 1. Build da imagem

```bash
docker build -t payflow-inadimplencia .
```

### 2. Executar o container

```bash
docker run -p 8501:8501 payflow-inadimplencia
```
