import streamlit as st
import pandas as pd
import plotly.express as px
from src.predict import predict

st.set_page_config(
    page_title="Risco de Crédito",
    page_icon="💳",
    layout="wide"
)

st.sidebar.title("⚙️ Configurações")
st.sidebar.markdown("Upload de dados para análise de risco de crédito")

uploaded_file = st.sidebar.file_uploader("📂 Envie seu CSV", type=["csv"])

st.title("💳 Sistema de Classificação de Risco")
st.markdown("### Análise automatizada de clientes")

st.divider()


def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def gerar_download(df_download):
    return df_download.to_csv(index=False).encode("utf-8")


def gerar_metricas(df):
    total = len(df)
    aprovados = len(df[df["decisao"] == "Aprovar"])
    revisao = len(df[df["decisao"] == "Revisar"])
    negados = len(df[df["decisao"] == "Negar"])

    return total, aprovados, revisao, negados


def exibir_cards(total, aprovados, revisao, negados):
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📊 Total", total)
    col2.metric("✅ Aprovados", aprovados)
    col3.metric("⚠️ Revisão", revisao)
    col4.metric("❌ Negados", negados)


def exibir_impacto_financeiro(resultado):
    st.subheader("💰 Resumo Financeiro da Carteira")

    if "valor_solicitado" not in resultado.columns:
        st.warning("⚠️ A coluna 'valor_solicitado' não foi encontrada.")
        return

    aprovados = resultado[resultado["decisao"] == "Aprovar"]
    revisao = resultado[resultado["decisao"] == "Revisar"]
    negados = resultado[resultado["decisao"] == "Negar"]

    valor_total_aprovados = aprovados["valor_solicitado"].sum()
    valor_total_revisao = revisao["valor_solicitado"].sum()
    valor_total_negados = negados["valor_solicitado"].sum()
    valor_bloqueado = valor_total_revisao + valor_total_negados

    valor_total_carteira = resultado["valor_solicitado"].sum()
    ticket_medio = resultado["valor_solicitado"].mean()

    percentual_aprovado = (
        valor_total_aprovados / valor_total_carteira * 100
        if valor_total_carteira > 0 else 0
    )

    percentual_bloqueado = (
        valor_bloqueado / valor_total_carteira * 100
        if valor_total_carteira > 0 else 0
    )

    receita_estimada = valor_total_aprovados * 0.08

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("✅ Valor Aprovado", formatar_moeda(valor_total_aprovados))
    col2.metric("🚫 Valor Negado", formatar_moeda(valor_total_negados))
    col3.metric("⚠️ Valor em Revisão", formatar_moeda(valor_total_revisao))
    col4.metric("💼 Receita Estimada", formatar_moeda(receita_estimada))

    col5, col6, col7, col8 = st.columns(4)

    col5.metric("📊 Carteira Total", formatar_moeda(valor_total_carteira))
    col6.metric("🔒 Valor Bloqueado", formatar_moeda(valor_bloqueado))
    col7.metric("📈 % Valor Aprovado", f"{percentual_aprovado:.1f}%")
    col8.metric("💳 Ticket Médio", formatar_moeda(ticket_medio))


if uploaded_file:

    df = pd.read_csv(uploaded_file)

    with st.spinner("🔄 Processando dados..."):
        resultado = predict(df)

    if "decisao" not in resultado.columns:
        st.error("A coluna 'decisao' não foi encontrada no resultado.")
        st.write("Colunas encontradas:", resultado.columns.tolist())
        st.stop()

    st.success("✔️ Classificação concluída!")

    total, aprovados, revisao, negados = gerar_metricas(resultado)

    exibir_cards(total, aprovados, revisao, negados)

    st.divider()

    exibir_impacto_financeiro(resultado)

    st.divider()

    st.subheader("🔍 Filtros")

    decisao_filtro = st.multiselect(
        "Filtrar por decisão:",
        options=resultado["decisao"].unique(),
        default=resultado["decisao"].unique()
    )

    df_filtrado = resultado[resultado["decisao"].isin(decisao_filtro)]

    cores = {
        "Aprovar": "green",
        "Revisar": "orange",
        "Negar": "red"
    }

    col1, col2 = st.columns(2)

    with col1:
        fig_pizza = px.pie(
            resultado,
            names="decisao",
            title="Distribuição das Decisões",
            color="decisao",
            color_discrete_map=cores
        )
        st.plotly_chart(fig_pizza, use_container_width=True)

    with col2:
        contagem = resultado["decisao"].value_counts().reset_index()
        contagem.columns = ["Decisão", "Quantidade"]

        fig_bar = px.bar(
            contagem,
            x="Decisão",
            y="Quantidade",
            color="Decisão",
            title="Quantidade por Decisão",
            color_discrete_map=cores
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    st.divider()

    st.subheader("📋 Dados Filtrados")
    st.dataframe(df_filtrado, use_container_width=True)

    st.subheader("⬇️ Exportar Resultados")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.download_button(
            "📥 Aprovados",
            gerar_download(resultado[resultado["decisao"] == "Aprovar"]),
            "aprovados.csv",
            "text/csv"
        )

    with col2:
        st.download_button(
            "📥 Revisão",
            gerar_download(resultado[resultado["decisao"] == "Revisar"]),
            "revisao.csv",
            "text/csv"
        )

    with col3:
        st.download_button(
            "📥 Negados",
            gerar_download(resultado[resultado["decisao"] == "Negar"]),
            "negados.csv",
            "text/csv"
        )

    with col4:
        st.download_button(
            "📥 Resultado Completo",
            gerar_download(resultado),
            "resultado_completo.csv",
            "text/csv"
        )

else:
    st.info("📂 Envie um arquivo CSV para começar")