# Projeto SPTrans Data Pipeline

📋 Visão Geral

O projeto nos possibilita monitorar em tempo quase real a quantidade de veículos disponíveis em operação,na cidade de São Paulo, com foco inicial na região central.
Pcoloque ermitindo análises estratégicas e intervenções operacionais na frota de ônibus.
Com esses dados, é possível identificar desequilíbrios na distribuição dos veículos, detectar situações de superlotação e otimizar a alocação da frota de forma mais eficiente, melhorando a qualidade do serviço e a experiência dos passageiros.
Este projeto tem como objetivo coletar, processar e disponibilizar dados da SPTrans (Olho Vivo API) em um ambiente Databricks.
A arquitetura foi construída seguindo o modelo Lakehouse com as camadas Bronze, Silver e Gold, garantindo qualidade, segurança e confiabilidade dos dados.

O pipeline captura informações em tempo quase real sobre:

📍 Posição dos veículos

🚍 Veículos ativos no momento

🗺️ Linhas de ônibus

📁 Arquivos de carga fria (GTFS ou estáticos)

Esses dados são usados para monitoramento operacional, análises de mobilidade urbana e visualizações no Power BI.

⚙️ Arquitetura

O projeto segue a arquitetura Medallion (Bronze → Silver → Gold):

Camada	Descrição
Bronze (Raw)	Dados brutos extraídos diretamente da API SPTrans e arquivos de carga fria.
Silver (Trusted)	Dados limpos, normalizados e com tipos tratados (ex: data/hora, coordenadas, status).
Gold (Refined)	Dados analíticos prontos para dashboards e relatórios, integrados com o Power BI.
🧠 Tecnologias Utilizadas

Databricks (PySpark / Workflows / Secret Scopes)

API Olho Vivo (SPTrans)

Power BI (visualização dos dados Gold)

Python (requests, pandas, pyspark.sql)

Delta Lake (armazenamento otimizado)

Git Integration (versionamento de notebooks)

🔐 Segurança

O token de autenticação da API SPTrans é armazenado em um Databricks Secret Scope, garantindo que o código não exponha credenciais sensíveis.
Nos notebooks, o token é acessado da seguinte forma:

token = dbutils.secrets.get(scope="sptrans_scope", key="api_token")

🕒 Workflows e Agendamentos

| **Job**              | **Descrição**                                                 | **Frequência**        |
|-----------------------|---------------------------------------------------------------|------------------------|
| `api_posicao`         | Coleta a posição de todos os veículos em operação.            | ⏱️ A cada **2 minutos** |
| `api_veiculos_ativos` | Calcula o número de veículos ativos por horário.              | ⏱️ A cada **15 minutos** |
| `carga_fria`          | Escuta o volume; ao detectar atualização, dispara a ingestão. | ⚡ **Sob demanda**     |
| `api_linhas`          | Atualiza a dimensão de linhas de ônibus.                      | 📅 **1 vez por mês**   |

🚀 Próximos Passos / Melhorias

🌎 Expansão do monitoramento para demais regiões da cidade de São Paulo.

📊 Expandir dashboards para espelhar esses dadios near real time.

