# Dicionário de Dados

Este dicionário de dados documenta as tabelas relacionadas a linhas de ônibus e veículos ativos, incluindo colunas, tipos de dados e comentários explicativos.

---

## Tabela 1: dm_linhas

| col_name       | data_type | comment |
|----------------|-----------|---------|
| regiao         | string    | Região associada à linha de ônibus específica. |
| bairro_busca   | string    | Bairro associado à busca da linha de ônibus específica. |
| linha_id       | bigint    | Identificador único associado à linha de ônibus. |
| sentido        | bigint    | Direção ou rota que a linha de ônibus segue, identificada por um valor numérico. |
| numero_linha   | string    | Código numérico que identifica uma linha de ônibus específica. |
| letra_linha    | bigint    | Letra associada ao código da linha de ônibus. |
| origem         | string    | Ponto de partida ou local de onde a linha de ônibus inicia sua rota. |
| destino        | string    | Local onde a linha de ônibus termina sua rota. |

---

## Tabela 2: fato_posicao

| col_name           | data_type | comment |
|-------------------|-----------|---------|
| linha_id          | int       | Identificador único para cada linha. |
| linha_cod         | string    | Código identificador da linha. |
| sentido_linha     | int       | Direção da linha de transporte público representada numericamente. |
| letreiro_principal| string    | Letreiro principal da linha de transporte público. |
| letreiro_secundario| string   | Letreiro secundário da linha de transporte público. |
| fl_acessivel      | boolean   | Indica se a linha de transporte é acessível para pessoas com deficiência (true/false). |
| veiculo_prefixo   | string    | Prefixo do veículo na linha de transporte público. |
| timestamp_api     | string    | Data e hora em que a informação foi registrada pela API. |
| lat               | double    | Latitude da localização do veículo na linha de transporte público. |
| lon               | double    | Longitude da localização do veículo na linha de transporte público. |

---

## Tabela 3: fato_veiculos_ativos

| col_name       | data_type | comment |
|----------------|-----------|---------|
| linha_id       | bigint    | Identificador único para a linha do veículo. |
| qtd_veiculos   | bigint    | Quantidade total de veículos ativos. |
| hora_consulta  | string    | Data e hora da consulta para a linha do veículo. |

---

*Este dicionário de dados pode ser usado como referência para consultas, relatórios ou integração com sistemas de transporte público.*

