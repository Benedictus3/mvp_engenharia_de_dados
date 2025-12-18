# MVP_Engenharia_De_Dados

# Análise de Impacto da IA no Mercado de Trabalho (2030)

Este projeto é um MVP de Engenharia de Dados desenvolvido no **Databricks** utilizando **PySpark** e **Spark SQL** para analisar como a automação impactará diferentes ocupações.

## 🛠️ Tecnologias Utilizadas
* **Linguagens:** SQL, Python (PySpark)
* **Plataforma:** Databricks (Community Edition)
* **Arquitetura:** Medalhão (Camadas RAW e CURATED)
* **Modelagem:** Star Schema (Esquema Estrela)

## 📊 Insights Principais
* **Correlação Salário x Risco:** Identificada uma correlação de **-0.0133**, demonstrando que o salário não é um fator de proteção contra a automação.
* **Habilidades:** A proficiência em habilidades técnicas isoladas apresentou correlação próxima de zero com a exposição à IA, sugerindo que a resiliência reside em competências socioemocionais complexas.
* **Ranking de Risco:** Ocupações técnicas como 'AI Engineer' aparecem com riscos inesperados de automação (~50%), indicando mudanças na própria área de tecnologia.

## 🏗️ Estrutura do Projeto
1. **Ingestão:** Carga de dados brutos para a camada RAW.
2. **Transformação:** Criação de Tabelas de Dimensão e Fato na camada CURATED.
3. **Análise:** Execução de consultas analíticas e cálculos de correlação de Pearson.
