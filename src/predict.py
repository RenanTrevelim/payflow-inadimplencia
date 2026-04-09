import joblib
import pandas as pd

preprocessador = joblib.load('models/pre-processamento.pkl')
modelo = joblib.load('models/modelo.pkl')
colunas_modelo = joblib.load('models/colunas_modelo.pkl')

COLUNAS_ENTRADA = ["idade", "renda_mensal", "tempo_emprego_anos", "autonomo", "score_credito", "valor_solicitado", "prazo_meses",
                    "juros_mensal_pct","qtde_cartoes", "qtde_contratos_abertos", "utilizacao_credito", "inadimplencias_anteriores",
                    "dias_atraso_max_12m", "reclamacoes_6m", "possui_avalista", "canal_aquisicao", "regiao", "tipo_produto"]


def classificar_decisao(probabilidade):
    if probabilidade >= 0.65:
        return "Negar"
    elif probabilidade >= 0.40:
        return "Revisar"
    return "Aprovar"

def predict(dados):

    df = pd.DataFrame(dados)
    df = df[COLUNAS_ENTRADA]

    # feature engineering
    df["comprometimento_renda"] = df["valor_solicitado"] / df["renda_mensal"]
    df["parcela_estimada"] = df["valor_solicitado"] / df["prazo_meses"]
    df["parcela_renda"] = df["parcela_estimada"] / df["renda_mensal"]

    resultado = df.copy()

    df_transformado = preprocessador.transform(df)

    df_transformado = pd.DataFrame(df_transformado, columns=colunas_modelo)

    previsao = modelo.predict(df_transformado)
    probabilidades = modelo.predict_proba(df_transformado)[:, 1]

    resultado['previsao'] = previsao
    resultado['probabilidade'] = probabilidades
    resultado['decisao'] = resultado['probabilidade'].apply(classificar_decisao)

    return resultado

    