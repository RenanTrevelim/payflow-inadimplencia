# 🏦 Motor de Decisão de Crédito com Machine Learning

Sistema de apoio à decisão que utiliza Machine Learning para **avaliar risco de crédito em lote** e traduzir previsões em **impacto financeiro direto para o negócio**.

> 📊 O foco não é apenas prever inadimplência — é **maximizar retorno financeiro da carteira**.

---

## 📊 Resultados Financeiros (Destaque do Projeto)

Aplicando o modelo em uma base de teste, foi possível simular o impacto financeiro da carteira:

### 💰 Impacto Financeiro

- 🚫 **Calotes evitados:** 90  
- 🛡️ **Perda evitada:** R$ 1.006.969,18  
- ⚠️ **Prejuízo com falsos negativos:** R$ 358.033,49  
- 📉 **Custo de oportunidade (bons clientes negados):** R$ 288.216,96  
- 💼 **Impacto líquido estimado:** **R$ 360.718,74**  

---

### 🎯 Interpretação

- O modelo conseguiu **evitar mais de R$ 1 milhão em perdas potenciais**  
- Mesmo considerando erros (falsos negativos e falsos positivos), o resultado final foi **positivo**  
- O impacto líquido de **R$ 360 mil** mostra que o modelo gera valor real para o negócio  

👉 Isso demonstra que o modelo não apenas prevê risco, mas **melhora diretamente o resultado financeiro da operação de crédito**

---

### 🧠 Conclusão

O modelo permite:

- Reduzir perdas com inadimplência  
- Controlar erros críticos de decisão  
- Balancear risco e retorno  
- Tomar decisões orientadas a valor  

👉 Transformando Machine Learning em uma **ferramenta estratégica de negócio**

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
4. **Resumo financeiro em tempo real**

---

## ⚙️ Motor de Decisão

A decisão é baseada na probabilidade prevista pelo modelo:

```text
probabilidade ≥ 0.65 → Negar  
0.40 ≤ probabilidade < 0.65 → Revisar  
probabilidade < 0.40 → Aprovar  
```
📌 Implementado diretamente no código (predict.py)

--- 

## 📤 Saída do Modelo

Para cada cliente:

- 📊 **probabilidade** → risco de inadimplência  
- 🔢 **previsao** → classificação binária  
- 🧠 **decisao** → ação recomendada  

---

## 💰 Camada de Negócio (Principal Diferencial)

O sistema traduz decisões em métricas financeiras reais da carteira:

### 📊 Indicadores disponíveis

- 💵 **Valor aprovado** → capital exposto ao risco  
- 🚫 **Valor negado** → risco evitado  
- ⚠️ **Valor em revisão** → incerteza / análise manual  
- 💼 **Receita estimada** → retorno esperado (juros)  
- 🔒 **Valor bloqueado** → proteção contra risco  
- 📊 **% aprovado** → nível de agressividade do modelo  
- 💳 **Ticket médio** → risco médio por cliente  

📌 Implementado na aplicação Streamlit  

---

## 📈 Interpretação Financeira

A análise permite responder perguntas críticas:

- Quanto dinheiro estou colocando em risco?  
- Quanto estou deixando de perder?  
- Meu modelo está conservador ou agressivo?  
- Estou priorizando crescimento ou proteção?  

👉 O modelo passa a ser avaliado como um **ativo financeiro**, não apenas técnico.

---

## 🖥️ Aplicação (Streamlit)

Interface interativa para uso em lote:

- Upload de arquivo `.csv`  
- Classificação automática dos clientes  
- Segmentação:
  - ✅ Aprovados  
  - ⚠️ Revisão  
  - ❌ Negados  
- Visualização de métricas financeiras  
- Download dos resultados  

📌 Implementação disponível na aplicação principal  

---

## 🔍 Pipeline de Machine Learning

### 1. Feature Engineering

Criação de variáveis de risco:

- comprometimento de renda  
- parcela estimada  
- relação parcela/renda  

📌 Implementado no `predict.py`

---

### 2. Pré-processamento

- Normalização (`StandardScaler`)  
- Codificação (`OneHotEncoder`)  
- Pipeline com `ColumnTransformer`  

---

### 3. Modelagem

- Regressão Logística (modelo principal)  
- Saída probabilística (`predict_proba`)  

---

### 4. Decisão

Conversão da probabilidade em ação:

- Aprovar  
- Revisar  
- Negar  

---

## 📊 Resultado na Prática

A aplicação permite simular uma carteira real e obter:

- Volume financeiro aprovado  
- Valor de risco bloqueado  
- Receita estimada da operação  
- Perfil de risco da carteira  

👉 Isso transforma o modelo em uma **ferramenta de decisão executiva**.

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