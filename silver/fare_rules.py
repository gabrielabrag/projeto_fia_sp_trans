# Databricks notebook source
df = spark.table("sp_trans.raw.fare_rules")
# display(df)

# COMMAND ----------

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import unicodedata
def remover_acentos(texto):
    if texto is not None:
        return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    return texto
remover_acentos_udf = udf(remover_acentos, StringType())

# COMMAND ----------

from pyspark.sql.functions import col

for c in df.columns:
    if dict(df.dtypes)[c] == 'string':
        df = df.withColumn(c, remover_acentos_udf(col(c)))


# COMMAND ----------

# display(df)

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("sp_trans.trusted.fare_rules")
