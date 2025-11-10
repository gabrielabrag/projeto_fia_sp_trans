# Databricks notebook source
df = spark.table("sp_trans.raw.trips")

# COMMAND ----------

import unicodedata
import re
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

# Função para limpar texto
def limpar_texto(texto):
    if texto is None:
        return None
    # Normaliza (remove acentos)
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    # Remove caracteres não ASCII
    texto = re.sub(r'[^\x00-\x7F]+', '', texto)
    # Remove espaços extras
    texto = re.sub(r'\s+', ' ', texto)
    return texto.strip()

# Registrar UDF
limpar_texto_udf = udf(limpar_texto, StringType())

# COMMAND ----------

for c, tipo in df.dtypes:
    if tipo == "string":
        df = df.withColumn(c, limpar_texto_udf(col(c)))

# COMMAND ----------

display(df)

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("sp_trans.trusted.trips")
