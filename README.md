# 🏦 Motor de Decisão de Crédito com Machine Learning

Projeto completo de **modelagem de risco de inadimplência** com aplicação prática em concessão de crédito, incluindo:

- Análise exploratória (EDA)
- Feature engineering
- Modelagem e validação
- Simulação financeira
- Interface interativa com **Streamlit**

---

## 📌 Objetivo

Desenvolver um modelo capaz de prever a **probabilidade de inadimplência** e transformá-lo em uma **ferramenta de apoio à decisão de crédito**, permitindo:

- Reduzir perdas financeiras  
- Automatizar aprovações de baixo risco  
- Priorizar análises manuais  
- Apoiar decisões estratégicas  

---

## 🧠 Problema de Negócio

Instituições financeiras precisam equilibrar dois objetivos:

- Aprovar bons clientes → gerar receita  
- Evitar inadimplentes → reduzir prejuízo  

Uma decisão incorreta pode gerar:

- ❌ **Calote direto**
- ⚠️ **Perda de oportunidade (bom cliente recusado)**

Este projeto propõe uma solução **data-driven** para otimizar esse processo.

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

---

## 📤 Saída do Modelo

O modelo retorna:

- `previsao` → classificação (0 ou 1)  
- `probabilidade` → risco de inadimplência  
- `decisao` → ação recomendada  

---

## 🧠 Regras de Decisão

Transformação da probabilidade em ação prática:

- 🔴 **≥ 0.65 → Negar**  
- 🟡 **≥ 0.40 → Revisar**  
- 🟢 **< 0.40 → Aprovar**  

📌 Aproxima o modelo da operação real de crédito.

---

## 🖥️ Aplicação com Streamlit

A interface permite:

- Upload de base em lote (.csv)  
- Classificação automática dos clientes  
- Segmentação em:
  - Aprovados  
  - Revisar  
  - Negados  
- Download dos resultados  
- Resumo financeiro da carteira  

📌 O modelo deixa de ser teórico e vira uma ferramenta prática.

![ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/1975f5dc-2d09-4012-9954-3b8febde9491)


---

## 📊 Etapas do Projeto

### 🔍 1. Análise Exploratória (EDA)

- Análise estatística  
- Tratamento de dados  
- Identificação de padrões  

**Principais insights:**

- Atrasos recentes são fortes indicadores de risco  
- Comprometimento de renda impacta inadimplência  
- Score de crédito tem relação inversa com risco  

---

### ⚙️ 2. Feature Engineering

Criação de variáveis relevantes:

- `comprometimento_renda`  
- `parcela_estimada`  
- `parcela_renda`  

---

### 🧪 3. Pré-processamento

- Padronização (`StandardScaler`)  
- Codificação (`OneHotEncoder`)  
- Pipeline com `ColumnTransformer`  

---

### 🤖 4. Modelagem

Modelos utilizados:

- Regressão Logística (principal)  
- Random Forest (comparação)  

📌 Uso de `class_weight='balanced'`

---

### 🎯 5. Ajuste de Threshold

- 0.3 → mais conservador  
- 0.4 → equilíbrio  
- 0.5 → melhor trade-off  

---

### 🔁 6. Validação

- Técnica: Stratified K-Fold  
- Recall: 0.64  
- Precision: 0.28  
- F1-score: 0.39  

📌 Modelo consistente e generalizável.

---

### ⭐ 7. Interpretabilidade

Principais drivers de risco:

- Comprometimento da renda  
- Dias de atraso  
- Histórico de inadimplência  

📌 Modelo explicável e alinhado ao negócio.

---

### 💰 8. Avaliação Financeira

- Perda evitada: **R$ 951 mil**  
- Impacto líquido: **R$ 350 mil**  

📌 Geração de valor real.


## 🧱 Estrutura do Projeto

```text
payflow-inadimplencia/
├── data/
│   ├── payflow_credit_risk.csv
│   └── teste.csv
├── models/
│   ├── modelo.pkl
│   ├── pre-processamento.pkl
│   └── colunas_modelo.pkl
├── notebooks/
│   ├── EDA_projeto_PayFlow.ipynb
│   └── PayFlow_Projeto_de_Inadimplencias.ipynb
├── src/
│   └── predict.py
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## 🛠️ Tecnologias Utilizadas

- Python  
- Pandas  
- Scikit-learn  
- Streamlit  
- Joblib  
- Jupyter Notebook  

---

## 📌 Possíveis Melhorias

- Deploy da aplicação (Streamlit Cloud / AWS)  
- Monitoramento de drift do modelo  
- Testes automatizados  
- Dockerização  
- API com FastAPI  
- Calibração de probabilidades  

---

## 👤 Autor

**Renan Trevelim**

- GitHub: https://github.com/RenanTrevelim  
- LinkedIn: https://www.linkedin.com/in/renan-trevelim/  
