import streamlit as st
import pandas as pd
from src.predict import predict

st.set_page_config(page_title="Motor de Decisão de Crédito", layout="wide")

def to_csv(df: pd.DataFrame):
    return df.to_csv(index=False).encode("utf-8")

st.title("🏦 Motor de Decisão de Crédito")
st.write("Faça upload de um arquivo CSV para análise em lote.")

arquivo = st.file_uploader("Envie o arquivo CSV", type=["csv"])

if arquivo is not None:
    try:
        df = pd.read_csv(arquivo)

        st.subheader("Prévia do arquivo")
        st.dataframe(df.head(), use_container_width=True)

        resultado = predict(df)

        aprovados = resultado[resultado["decisao"] == "Aprovar"].copy()
        revisar = resultado[resultado["decisao"] == "Revisar"].copy()
        negados = resultado[resultado["decisao"] == "Negar"].copy()

        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        # -------------------
        # APROVADOS
        # -------------------
        with col1:
            st.markdown("## ✅ Aprovados")
            st.write(f"Quantidade: **{len(aprovados)}**")
            st.write(f"Valor total: **R$ {aprovados['valor_solicitado'].sum():,.2f}**")

            st.download_button(
                "Baixar aprovados",
                data=to_csv(aprovados),
                file_name="aprovados.csv",
                mime="text/csv"
            )

        # -------------------
        # REVISAR
        # -------------------
        with col2:
            st.markdown("## 🟡 Revisar")
            st.write(f"Quantidade: **{len(revisar)}**")
            st.write(f"Valor total: **R$ {revisar['valor_solicitado'].sum():,.2f}**")

            st.download_button(
                "Baixar revisão",
                data=to_csv(revisar),
                file_name="revisar.csv",
                mime="text/csv"
            )

        # -------------------
        # NEGADOS
        # -------------------
        with col3:
            st.markdown("## ⛔ Negados")
            st.write(f"Quantidade: **{len(negados)}**")
            st.write(f"Valor total: **R$ {negados['valor_solicitado'].sum():,.2f}**")

            st.download_button(
                "Baixar negados",
                data=to_csv(negados),
                file_name="negados.csv",
                mime="text/csv"
            )

        st.markdown("---")

        st.subheader("💰 Visão Financeira")
        valor_total = resultado["valor_solicitado"].sum()
        valor_aprovado = aprovados["valor_solicitado"].sum()
        valor_revisao = revisar["valor_solicitado"].sum()
        valor_negado = negados["valor_solicitado"].sum()

        f1, f2, f3, f4 = st.columns(4)
        f1.metric("Valor total da carteira", f"R$ {valor_total:,.2f}")
        f2.metric("Valor aprovado", f"R$ {valor_aprovado:,.2f}")
        f3.metric("Valor em revisão", f"R$ {valor_revisao:,.2f}")
        f4.metric("Valor negado", f"R$ {valor_negado:,.2f}")

        st.markdown("---")
        st.subheader("Resultado completo")
        st.dataframe(resultado, use_container_width=True)

        st.download_button(
            "Baixar resultado completo",
            data=to_csv(resultado),
            file_name="resultado_completo.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error("Erro ao processar o arquivo.")
        st.exception(e)