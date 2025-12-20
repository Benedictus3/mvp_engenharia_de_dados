import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="IA Impacto 2030", layout="wide")

st.title("🤖 Impacto da IA no Mercado de Trabalho (2030)")
st.markdown("Dashboard interativo baseado na análise de dados em PySpark.")

# Carregar dados
@st.cache_data
def load_data():
    df = pd.read_csv("ia_jobs_full.csv")
    top10 = pd.read_csv("ia_jobs_top10.csv")
    skills = pd.read_csv("ia_jobs_skills.csv")
    return df, top10, skills

df, top10, skills = load_data()Habilidade,Correlacao_Exposicao_IA
Skill_1,0.0005070675636830737
Skill_2,0.015080200632369907
Skill_3,-0.010471451355445357
Skill_4,0.029349762762284473
Skill_5,-0.007859855849107804
Skill_6,0.017070457688319152
Skill_7,0.016865169271144682
Skill_8,-0.009689529167043354
Skill_9,0.006829393041423888
Skill_10,0.0009640271716601548

Job_Title,Automation_Probability_2030
Retail Worker,0.8347096774193548
Security Guard,0.8330519480519482
Construction Worker,0.8259615384615385
Customer Support,0.8252631578947369
Truck Driver,0.8186274509803921
Graphic Designer,0.529
Software Engineer,0.5086857142857143
Data Scientist,0.4962874251497006
Chef,0.4956737588652482
Marketing Manager,0.49477611940298505


# Sidebar para Filtros
st.sidebar.header("Filtros")
escolaridade = st.sidebar.multiselect("Nível de Escolaridade", options=df["Education_Level"].unique(), default=df["Education_Level"].unique())

df_filtrado = df[df["Education_Level"].isin(escolaridade)]

# Layout de Colunas (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Risco Médio", f"{df_filtrado['Automation_Probability_2030'].mean():.2%}")
col2.metric("Salário Médio", f"${df_filtrado['Average_Salary'].mean():,.0f}")
col3.metric("Qtd. Ocupações", len(df_filtrado))

# Gráficos
row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("Top 10 Ocupações por Risco")
    fig_bar = px.bar(top10, x="Risk", y="Job_Title", orientation='h', color="Risk", color_continuous_scale="Reds")
    st.plotly_chart(fig_bar, use_container_width=True)

with row2_col2:
    st.subheader("Salário vs Risco de Automação")
    fig_scatter = px.scatter(df_filtrado, x="Average_Salary", y="Automation_Probability_2030", 
                             color="Risk_Category", hover_name="Job_Title", trendline="ols")
    st.plotly_chart(fig_scatter, use_container_width=True)

st.subheader("Análise de Correlação por Habilidade")
fig_skills = px.bar(skills, x="Habilidade", y="Correlacao_Exposicao_IA", color="Correlacao_Exposicao_IA")
st.plotly_chart(fig_skills, use_container_width=True)
