# 🤖 Análise de Impacto da IA no Mercado de Trabalho (2030)

Este projeto apresenta um pipeline de dados completo desenvolvido no **Databricks**, utilizando **PySpark** para processar e analisar o impacto da automação em diversas ocupações.

## 📊 Principais Insights (Visualizações)

### 1. Ocupações de Maior Risco
A análise identificou que o risco de automação não afeta apenas tarefas manuais, mas atinge áreas técnicas como Engenharia de IA.
![Ranking de Risco](grafico de barra.png)

### 2. Relação Salário vs. Risco
Descobrimos uma correlação de **-0.0133**, provando que o salário elevado não é uma barreira contra a automação.
![Dispersão Salário x Risco](salario_vs_risco.png)

---

## 🛠️ Arquitetura Técnica
O projeto segue a arquitetura de medalhão e boas práticas de modelagem:

* **Camada RAW:** Dados brutos ingeridos no DBFS.
* **Camada CURATED:** Dados limpos e modelados em **Esquema Estrela (Star Schema)**.
* **Modelagem:** Separação entre Tabela Fato (`fato_risco_automacao`) e Dimensão (`dim_ocupacao`).
* **Tecnologias:** PySpark, Spark SQL, Delta Lake.

## 📈 Conclusões
O estudo demonstra que a resiliência profissional para 2030 depende menos de habilidades técnicas quantificáveis e mais da adaptabilidade humana, dado que a exposição à IA é transversal a quase todos os níveis salariais e de escolaridade.
