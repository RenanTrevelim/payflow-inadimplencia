# 🏦 Motor de Decisão de Crédito com Machine Learning

Sistema de apoio à decisão que utiliza Machine Learning para **avaliar risco de crédito em lote** e traduzir previsões em **impacto financeiro direto para o negócio**.

> 📊 O foco não é apenas prever inadimplência — é **maximizar retorno financeiro da carteira**.

---

## 🎯 Objetivo

Construir um motor capaz de:

- Estimar a **probabilidade de inadimplência**
- Converter essa probabilidade em **decisões operacionais**
- Gerar uma **visão financeira da carteira de crédito**
- Apoiar decisões com base em **risco vs retorno**

---

## 🧠 Problema de Negócio

Concessão de crédito envolve decisões com impacto direto no resultado financeiro:

| Situação | Impacto |
|--------|--------|
| Aprovar cliente inadimplente | ❌ Prejuízo direto |
| Negar cliente bom | ⚠️ Perda de receita |
| Aprovar cliente bom | ✅ Geração de lucro |

👉 O desafio é encontrar o **equilíbrio ideal entre risco e crescimento**.

---

## 💡 Solução

O projeto implementa um pipeline completo:

1. **Previsão de risco (probabilidade)**
2. **Classificação automática de clientes**
3. **Segmentação da carteira**
4. **Resumo financeiro da operação**

---

## ⚙️ Motor de Decisão

A decisão é baseada na probabilidade prevista pelo modelo:

```text
probabilidade ≥ 0.65 → Negar  
0.40 ≤ probabilidade < 0.65 → Revisar  
probabilidade < 0.40 → Aprovar  
```
---

## 💰 Camada de Negócio (Diferencial)

O sistema traduz decisões em métricas financeiras reais da carteira:

### 📊 Indicadores

- 💵 **Valor aprovado** → capital exposto ao risco  
- 🚫 **Valor negado** → risco evitado  
- ⚠️ **Valor em revisão** → análise manual  
- 💼 **Receita estimada** → retorno esperado  
- 🔒 **Valor bloqueado** → proteção contra risco  
- 📊 **% aprovado** → agressividade da estratégia  
- 💳 **Ticket médio** → risco médio por cliente  

---

## 📊 Resultados Financeiros

Aplicando o modelo em uma base de teste:

### 💰 Impacto Financeiro

- 🚫 **Calotes evitados:** 90  
- 🛡️ **Perda evitada:** R$ 1.006.969,18  
- ⚠️ **Prejuízo com falsos negativos:** R$ 358.033,49  
- 📉 **Custo de oportunidade (bons clientes negados):** R$ 288.216,96  
- 💼 **Impacto líquido estimado:** R$ 360.718,74  

---

### 🎯 Interpretação

- O modelo evitou **mais de R$ 1 milhão em perdas potenciais**  
- Mesmo com erros inevitáveis, o resultado final foi **positivo**  
- Geração líquida de **R$ 360 mil em valor**  

👉 O modelo gera **impacto financeiro real**, não apenas métricas técnicas  

---

## 📈 Aplicação (Streamlit)

Interface para uso em lote:

- Upload de arquivo `.csv`  
- Classificação automática  
- Segmentação:
  - ✅ Aprovados  
  - ⚠️ Revisão  
  - ❌ Negados  
- Visualização financeira  
- Download dos resultados  

---

## 📤 Saída do Modelo

Para cada cliente:

- 📊 **probabilidade** → risco de inadimplência  
- 🔢 **previsao** → classificação  
- 🧠 **decisao** → ação recomendada  

---

## 🔍 Pipeline de Machine Learning

### 1. Feature Engineering
- comprometimento de renda  
- parcela estimada  
- relação parcela/renda  

### 2. Pré-processamento
- `StandardScaler`  
- `OneHotEncoder`  
- `ColumnTransformer`  

### 3. Modelagem
- Regressão Logística  
- `predict_proba`  

### 4. Decisão
- Aprovar  
- Revisar  
- Negar  

---

## 📊 Resultado na Prática

A aplicação permite simular:

- Volume financeiro aprovado  
- Valor de risco bloqueado  
- Receita estimada  
- Perfil de risco da carteira  

👉 Transformando o modelo em uma **ferramenta de decisão executiva**

--- 

## 🚀 Como rodar localmente


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