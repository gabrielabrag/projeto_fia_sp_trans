# Databricks notebook source
df = spark.table("sp_trans.raw.stop_times")

# COMMAND ----------

df = (spark.read
                .option("header", "true")      # força sem header
                .option("inferSchema", "true")
                .option("delimiter", ",")
                .csv("/Volumes/sp_trans/raw/carga_fria/stop_times.txt"))
display(df)


# COMMAND ----------

df.write.mode("overwrite").saveAsTable("sp_trans.raw.stop_times")
