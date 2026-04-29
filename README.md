# 🛡️ RetailData-SafeFlow: Pipeline de Integridade Financeira

![Banner](img/banner.png)

## 📝 Sobre o Projeto
O **RetailData-SafeFlow** é uma solução de engenharia de dados desenvolvida para enfrentar o desafio de dados inconsistentes em ambientes de varejo. O foco principal é a **integridade financeira**, garantindo que métricas estratégicas não sejam distorcidas por registros duplicados ou valores inválidos.

Este projeto demonstra a construção de um pipeline de dados end-to-end, unindo automação, tratamento de dados e práticas de governança.

## 🎯 Objetivos de Negócio
*   **Confiabilidade**: Garantir que o time de marketing e finanças trabalhe com dados 100% validados.
*   **Automação**: Eliminar processos manuais de limpeza de dados, reduzindo o risco de erro humano através da orquestração.
*   **Escalabilidade**: Estrutura modular preparada para crescer conforme o volume de vendas aumenta.

## 🛠️ Tecnologias Utilizadas
*   **Python & Pandas**: Extração e transformação robusta de dados.
*   **Apache Airflow**: Orquestração e agendamento dos workflows.
*   **Docker**: Conteinerização para garantir um ambiente de execução isolado e estável.
*   **SQL**: Consultas e estruturação para persistência de dados.

## 🛡️ Garantia de Qualidade e Integridade (Data Quality)

| Verificação | Descrição | Status |
| :--- | :--- | :--- |
| **Deduplicação** | Garante que não existam registros idênticos no pipeline. | ✅ Ativo |
| **Validação de Preço** | Filtra e corrige valores negativos ou inconsistentes. | ✅ Ativo |
| **Schema Check** | Verifica se as colunas estão no formato correto para o banco. | ✅ Ativo |
| **Orquestração** | Fluxo automatizado via Airflow para evitar erro humano. | ✅ Ativo |

## 🚀 Como Executar
1. Certifique-se de ter o **Docker** instalado.
2. Clone o repositório: `git clone https://github.com/YasmimLoppes/RetailData-SafeFlow.git`
3. Execute o comando: `docker-compose up` para iniciar o ambiente do Airflow.
4. Acesse a interface do Airflow e ative a DAG `retail_safeflow_pipeline`.

---
Desenvolvido por **Yasmim Lopes** — Focada em transformar dados brutos em inteligência de negócio robusta.